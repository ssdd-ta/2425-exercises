#!/usr/bin/python3
import socket
import struct

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind(('', 1234))

    while 1:
        data, client = s.recvfrom(1024)
        n1, n2 = struct.unpack("!ii", data)
        result = n1 + n2

        print(f"{client} :: {n1} + {n2} = {result}")
        s.sendto(struct.pack("!i", result), client)
