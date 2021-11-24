1. **Protocol Buffers** are a language-neutral mechanism for serializing structured data.

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
  
  python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calculator.proto
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

