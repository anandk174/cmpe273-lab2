import grpc
import calculator_pb2
import calculator_pb2_grpc
import calculator
from concurrent import futures
import time

class AddCalculatorServicer(calculator_pb2_grpc.CalculatorServicer):
    def AddNumber(self, request, context):
        output = calculator_pb2.OutputNumber()
        output.res_num = calculator.add_numbers(request.num_one, request.num_two)
        return output

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
calculator_pb2_grpc.add_CalculatorServicer_to_server(AddCalculatorServicer(), server)

print('Server Active')
server.add_insecure_port('[::]:50051')
server.start()

try:
    while True:
        time.sleep(80000)
except KeyboardInterrupt:
        server.stop(0)