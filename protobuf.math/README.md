## Adding and multiplying an arbitrary number of integers using Protocol Buffers
In this exercise we will create a simple client-server application that adds or multiplies any number of integers. The client will send the request with the list of numbers, then the server will return the sum/multiplication of the numbers. The client must print the result, and the server must run forever, listening for incoming messages.

Exec client and server programs in the following manner and order, in different terminal windows:
```bash
$ python3 server.py
```
```bash
$ python3 client.py <server_host> <op> <n1> <n2> ... <ni>
```

### Requirements
Install the following Debian packages:
```bash
sudo apt install protobuf-compiler python3-protobuf
```
