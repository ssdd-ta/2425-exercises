## Adding an arbitrary number of integers using a UDP socket connection
In this exercise we will create a simple client-server application that adds or multiplies any number of integers. The client will send a 3-bytes string ("sum" or "mul") and a list of numbers to the server, always serializing each number as a 2-bytes integer ("h" format in the `struct` module), then the server will return the sum/multiplication of the numbers as a 4-bytes integer ("i" format). The client must print the result, and the server must run forever, listening for incoming messages.

Exec client and server programs in the following manner and order, in different terminal windows:
```bash
$ python3 server.py
```
```bash
$ python3 client.py <server_host> <op> <n1> <n2> ... <ni>
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
msg = pack(op, nums)  |   |                          |   |
                      +-->|                          |   |  msg = recv()
                          |         send(msg)        |   |
                          |------------------------->|<--+
                      +---|                          |
                      |   |                          |---+
           r = recv() |   |                          |   |  op, numbers = unpack(msg)
                      |   |                          |   |  r = sum(numbers) or mul(numbers)
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
