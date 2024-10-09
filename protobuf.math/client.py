#!/usr/bin/python3
import sys
import socket
import math_pb2 as math


if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} <server_host> <op> <n1> <n2> ... <ni>")
    sys.exit(1)

operation = sys.argv[2]
if operation not in ["sum", "mul"]:
    print("Invalid operation")
    sys.exit(1)

ip = sys.argv[1]
numbers = [int(x) for x in sys.argv[3:]]

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    request = math.Request(operation=math.Request.SUM)
    request.numbers.extend(numbers)

    if operation == "mul":
        request.operation = math.Request.MULTIPLY

    print(f"Sending request to {ip}...")

    s.sendto(request.SerializeToString(), (ip, 1234))
    data = s.recv(4096)
    response = math.Response()
    response.ParseFromString(data)

    print(f"Result: {response.result}")
