1. What is **RPC** ?

   - Remote procedure call. It is a protocol that one program can use to request a service from a program that is located in another computer.
   - Remote procedure calls are the messages a server sends to a remote system to get the task done.
   - RPC is a request-response protocol. 
   - **Stub** is a piece of code used to convert parameters passed between client and server during RPC call. Main idea is to allow the local computer to call proedures on different computer (server).

2. Why **gRPC** ?

   - Language Independent Communication : two services say written in python and golang can communicate smoothly.

3. **Protocol Buffers** are a language-neutral mechanism for serializing structured data.

   gRPC uses protocol buffers for defining the type of data to be sent between the gRPC client and the gRPC server. 

4. There are 4 different types of **RPCs**

   1. **Unary RPCs** --> simple gRPC where it sends a single request to the server and gets back a single response.
   2. **Server streaming RPCs** --> client sends a message to the server and receives a stream of message sequence to read. It reads the message until nothing is left.
   3. **Client Streaming RPCs** --> Client sends a message stream to the server and receives a response
   4. **Bidirectional streaming RPCs** --> both client and server use a stream to send a message sequence.


Example:

- create **calculator.py**

  ```python
  import math
  
  def square_root(x):
    y = math.sqrt(x)
    return y
  ```

- create protocol buffers: create calculator.proto

  ```protobuf
  syntax = "proto3";
  
  message Number {
      float value = 1;
  }
  
  service Calculator {
      rpc SquareRoot(Number) returns (Number) {}
  }
  ```

- generate gRPC classes for python

  ```bash
  pip install grpcio
  pip install grpcio-tools
  
  python -m grpc_tools.protoc --proto_path=. ./calculator.proto --python_out=. --grpc_python_out=.
  ```

  These files will be generated:

  **calculator_pb2.py** — contains message classes

   **calculator_pb2_grpc.py** — contains server and client classes

-  Create gRPC server: server.py

  ```python
  import grpc
  from concurrent import futures
  import time
  
  # import the generated classes
  import calculator_pb2
  import calculator_pb2_grpc
  
  # import the original calculator.py
  import calculator
  
  # create a class to define the server functions, derived from
  # calculator_pb2_grpc.CalculatorServicer
  class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):
  
      # calculator.square_root is exposed here
      # the request and response are of the data type
      # calculator_pb2.Number
      def SquareRoot(self, request, context):
          response = calculator_pb2.Number()
          response.value = calculator.square_root(request.value)
          return response
  
  
  # create a gRPC server
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  
  # use the generated function `add_CalculatorServicer_to_server`
  # to add the defined class to the server
  calculator_pb2_grpc.add_CalculatorServicer_to_server(
          CalculatorServicer(), server)
  
  # listen on port 50051
  print('Starting server. Listening on port 50051.')
  server.add_insecure_port('[::]:50051')
  server.start()
  
  # since server.start() will not block,
  # a sleep-loop is added to keep alive
  try:
      while True:
          time.sleep(86400)
  except KeyboardInterrupt:
      server.stop(0)
  ```

- Start the server using the command:

  ```bash
  python server.py
  ```

- Create a gRPC client: client.py

  ```python
  import grpc
  
  # import the generated classes
  import calculator_pb2
  import calculator_pb2_grpc
  
  # open a gRPC channel
  channel = grpc.insecure_channel('localhost:50051')
  
  # create a stub (client)
  stub = calculator_pb2_grpc.CalculatorStub(channel)
  
  # create a valid request message
  number = calculator_pb2.Number(value=16)
  
  # make the call
  response = stub.SquareRoot(number)
  
  # et voilà
  print(response.value)
  ```

- 

