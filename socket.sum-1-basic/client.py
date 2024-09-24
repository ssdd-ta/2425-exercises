#!/usr/bin/python3
import socket
import struct
import sys

if len(sys.argv) != 4:
    print(f"Usage: {sys.argv[0]} <server_host> <number_1> <number_2>")
    sys.exit(1)

ip = sys.argv[1]
num1 = int(sys.argv[2])
num2 = int(sys.argv[3])

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    data = struct.pack("!ii", num1, num2)
    s.sendto(data, (ip, 1234))

    data = s.recv(1024)
    result = struct.unpack("!i", data)[0]

    print(f"Result: {result}")
