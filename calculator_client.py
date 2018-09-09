import calculator_pb2
import calculator_pb2_grpc
import grpc

comm_line = grpc.insecure_channel('localhost:50051')

stub = calculator_pb2_grpc.CalculatorStub(comm_line)

inputs = calculator_pb2.InputNumber(num_one = 10, num_two = 15)

output = stub.AddNumber(inputs)

print(output.res_num)