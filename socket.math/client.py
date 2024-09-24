#!/usr/bin/python3
import socket
import struct
import sys

if len(sys.argv) < 2:
    print(
        f"Usage: {sys.argv[0]} <server_host> <op> <n1> <n2> ... <ni>")
    sys.exit(1)

operation = sys.argv[2]
if operation not in ["sum", "mul"]:
    print("Invalid operation")
    sys.exit(1)

ip = sys.argv[1]
numbers = [int(x) for x in sys.argv[3:]]

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:

    data_format = "!3s" + "h" * len(numbers)
    print(f"Message format is: {data_format}")

    data = struct.pack(data_format, operation.encode(), *numbers)
    s.sendto(data, (ip, 1234))

    data = s.recv(1024)
    result = struct.unpack("!i", data)[0]

    print(f"Result: {result}")
