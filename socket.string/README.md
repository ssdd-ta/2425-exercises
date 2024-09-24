## Sending and receiving strings over a UDP socket connection
In this exercise we will create a simple client-server application that sends and receives strings over a UDP socket connection. The client will send a string (given as input) to the server, and the server will print the string to the console, sending a "received" string back to the client as an acknowledgment. The server must run forever, listening for incoming messages.

Exec client and server programs in the following manner and order, in different terminal windows:
```bash
$ python3 server.py
```
```bash
$ python3 client.py <server_ip> <server_port>
```

### Sequence diagram

```
          +-----------------+        +-----------------+
          |                 |        |                 |
          |      Client     |        |      Server     |
          |                 |        |                 |
          +-----------------+        +-----------------+
                   |                          |
               +---|                          |---+
msg = input()  |   |                          |   |
               +-->|                          |   |  msg = recv()
                   |         send(msg)        |   |
                   |------------------------->|<--+
               +---|                          |
               |   |                          |---+
 ack = recv()  |   |                          |   |  print(msg)
               |   |         send(ack)        |<--+
               +-->|<-------------------------|
                   |                          |---+
               +---|                          |   |
   print(ack)  |   |                          |   |  msg = recv()
               +-->|                          |   |
                   |                          |   |
                   #                          |   |
                finished                      ...   (loop forever)
```
