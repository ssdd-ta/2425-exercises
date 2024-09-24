#!/usr/bin/python3
import socket
import struct
import sys

if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} <server_host> <number_1> <number_2> ... <number_n>")
    sys.exit(1)

ip = sys.argv[1]
numbers = [int(x) for x in sys.argv[2:]]

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    data_format = "!" + "h" * len(numbers)
    print(f"Message format is: {data_format}")

    data = struct.pack(data_format, *numbers)
    s.sendto(data, (ip, 1234))

    data = s.recv(1024)
    result = struct.unpack("!i", data)[0]

    print(f"Result: {result}")
