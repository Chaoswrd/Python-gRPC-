import grpc
import calculator_pb2
import calculator_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = calculator_pb2_grpc.CalculatorStub(channel)
    response = stub.Add(calculator_pb2.AddRequest(a=1, b=2))
    print(response.result)
    response = stub.Subtract(calculator_pb2.SubtractRequest(a=5, b=3))
    print(response.result)

if __name__ == '__main__':
    run()
