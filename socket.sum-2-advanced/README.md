## Adding an arbitrary number of integers using a UDP socket connection
In this exercise we will create a simple client-server application that adds any number of integers. The client will send a list of numbers to the server, always serializing each number as a 2-bytes integer ("h" format in the `struct` module), then the server will return the sum of the numbers as a 4-bytes integer ("i" format). The client must print the result, and the server must run forever, listening for incoming messages.

Exec client and server programs in the following manner and order, in different terminal windows:
```bash
$ python3 server.py
```
```bash
$ python3 client.py <server_host> <number_1> <number_2> ... <number_n>
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
msg = pack(nums)   |   |                          |   |
                   +-->|                          |   |  msg = recv()
                       |         send(msg)        |   |
                       |------------------------->|<--+
                   +---|                          |
                   |   |                          |---+
        r = recv() |   |                          |   |  numbers = unpack(msg)
                   |   |                          |   |  r = sum(numbers)
                   |   |        send(r)           |<--+
                   +-->|<-------------------------|
                       |                          |---+
                   +---|                          |   |
result = unpack(r) |   |                          |   |  msg = recv()
     print(result) |   |                          |   |
                   +-->|                          |   |
                       |                          |   |
                       #                          |   |
                    finished                      ...   (loop forever)
```
