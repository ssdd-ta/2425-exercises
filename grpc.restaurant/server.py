#!/usr/bin/python3

import sys

import coloredlogs
import logging
from concurrent import futures

import grpc
import reservations_pb2
import reservations_pb2_grpc


coloredlogs.install()
logging.StreamHandler(sys.stdout)


class ReservationsService(reservations_pb2_grpc.ReservationsServicer):
    def __init__(self):
        self.reservations = {}

    def makeReservation(self, request, context):
        if request.date in self.reservations:
            details = f'Reservation already exists for {request.date}'
            logging.error(f'Make reservation: {details}')

            return reservations_pb2.ReservationResponse(
                result = reservations_pb2.Result.ERROR,
                details = details
            )

        details = f'Reservation created for {request.date}'
        logging.info(f'Make reservation: {details}')

        self.reservations[request.date] = request
        return reservations_pb2.ReservationResponse(
            result = reservations_pb2.Result.OK,
            details = details
        )

    def checkReservation(self, request, context):
        if request.date not in self.reservations:
            details = f'Reservation not found for {request.date}'
            logging.error(f'Check reservation: {details}')

            return reservations_pb2.ReservationResponse(
                result = reservations_pb2.Result.ERROR,
                details = 'Reservation not found'
            )

        details = f'Reservation found for {request.date}'
        logging.info(f'Check reservation: {details}')

        return reservations_pb2.ReservationResponse(
            result = reservations_pb2.Result.OK,
            details = details,
            reservation = self.reservations[request.date]
        )

    def cancelReservation(self, request, context):
        if request.date not in self.reservations:
            details = f'Reservation not found for {request.date}'
            logging.error(f'Cancel reservation: {details}')

            return reservations_pb2.ReservationResponse(
                result = reservations_pb2.Result.ERROR,
                details = details
            )

        details = f'Reservation canceled for {request.date}'
        logging.info(f'Cancel reservation: {details}')

        del self.reservations[request.date]
        return reservations_pb2.ReservationResponse(
            result = reservations_pb2.Result.OK,
            details = details
        )

    def listReservations(self, request, context):
        logging.info('List reservations')
        return reservations_pb2.ReservationsList(
            reservations = list(self.reservations.values())
        )


server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
reservations_pb2_grpc.add_ReservationsServicer_to_server(ReservationsService(), server)
server.add_insecure_port('0.0.0.0:2000')
server.start()

try:
    server.wait_for_termination()

except KeyboardInterrupt:
    server.stop(0)
