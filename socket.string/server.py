#!/usr/bin/python3
import socket

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind(('', 1234))
    msg, client = s.recvfrom(1024)
    print(f"{client} :: {msg.decode()}")
    s.sendto("Received!".encode(), client)
