#!/usr/bin/python3
import socket
import struct


def mul(numbers):
    result = 1
    for n in numbers:
        result *= n
    return result


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind(('', 1234))

    while 1:
        data, client = s.recvfrom(1024)

        operation = struct.unpack("!3s", data[:3])[0].decode()
        nums_format = f"!{((len(data) - 3) // 2)}h"
        print(f"Numbers format is: {nums_format}")

        numbers = struct.unpack(nums_format, data[3:])
        result = sum(numbers) if operation == "sum" else mul(numbers)

        print(f"{client} :: {operation} result = {result}")
        s.sendto(struct.pack("!i", result), client)
