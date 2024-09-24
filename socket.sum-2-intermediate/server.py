#!/usr/bin/python3
import socket
import struct

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind(('', 1234))

    while 1:
        data, client = s.recvfrom(1024)

        data_format = "!{}h".format(len(data) // 2)
        print(f"Message format is: {data_format}")

        numbers = struct.unpack(data_format, data)
        result = sum(numbers)

        print(f"{client} :: result = {result}")
        s.sendto(struct.pack("!i", result), client)
