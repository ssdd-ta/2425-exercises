#!/usr/bin/python3
import socket
import math_pb2 as math


def mul(numbers):
    result = 1
    for n in numbers:
        result *= n
    return result


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind(('', 1234))
    print("Server started")

    while 1:
        data, client = s.recvfrom(4096)
        print(f'Request from {client}')
        request = math.Request()
        request.ParseFromString(data)

        if request.operation == math.Request.SUM:
            result = sum(request.numbers)
        else:
            result = mul(request.numbers)

        response = math.Response(result=result)
        print(result)
        s.sendto(response.SerializeToString(), client)
