#!/usr/bin/python3
import socket
import struct

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind(('', 1234))

    while 1:
        data, client = s.recvfrom(1024)
        numbers = struct.unpack("!{}h".format(len(data) // 2), data)
        result = sum(numbers)

        print(f"{client} :: result = {result}")
        s.sendto(struct.pack("!i", result), client)
