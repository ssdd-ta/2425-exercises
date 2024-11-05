#!/usr/bin/python3

import random
import argparse
from datetime import datetime, timedelta

import grpc
import reservations_pb2
import reservations_pb2_grpc


class ReservationClient:
    def __init__(self, stub):
        self.stub = stub

    def makeReservation(self):
        def randomDate():
            today = datetime.now()
            one_year_later = today + timedelta(days=365)
            random_number = random.random()
            from_to_days = (one_year_later - today).days

            return today + timedelta(days=random_number * from_to_days)

        request = reservations_pb2.Reservation(
            date = randomDate().strftime('%Y-%m-%d'),
            time = random.randint(19, 23),
            number_of_diners = random.randint(1, 10),
            client_name = 'John Doe',
            contact_phone = '555-555-555'
        )

        response = self.stub.makeReservation(request)
        print(response.details)

    def checkReservation(self, date):
        response = self.stub.checkReservation(
            reservations_pb2.ReservationId(date=date)
        )

        if response.result == reservations_pb2.Result.ERROR:
            print(response.details)
            return

        print(response.reservation)

    def cancelReservation(self, date):
        response = self.stub.cancelReservation(
            reservations_pb2.ReservationId(date=date)
        )

        print(response.details)

    def listReservations(self):
        response = self.stub.listReservations(
            reservations_pb2.ListRequest()
        )

        for reservation in response.reservations:
            print(reservation)


parser = argparse.ArgumentParser()

parser.add_argument('server', type=str)
parser.add_argument('port', type=str)

parser.add_argument('-m', '--make', action='store_true')
parser.add_argument('-c', '--check', type=str, action='store')
parser.add_argument('-r', '--remove', type=str, action='store')
parser.add_argument('-l', '--list', action='store_true')
args = parser.parse_args()

channel = grpc.insecure_channel(f'{args.server}:{args.port}')
stub = reservations_pb2_grpc.ReservationsStub(channel)
client = ReservationClient(stub)

if args.make:
    client.makeReservation()
elif args.check:
    client.checkReservation(args.check)
elif args.remove:
    client.cancelReservation(args.remove)
else:
    client.listReservations()
