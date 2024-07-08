import os
from functools import reduce
from xmlrpc.server import SimpleXMLRPCServer
from dotenv import load_dotenv

load_dotenv()

def add(numbers):
    if len(numbers) == 0:
        return "Sem números"
    if len(numbers) == 1:
        return "Somente um número"
    if len(numbers) > 20:
        return "Quantidade de números não pode ser maior que 20"
    return reduce(lambda x, y: x + y, numbers)

def subtract(numbers):
    if len(numbers) == 0:
        return "Sem números"
    if len(numbers) == 1:
        return "Somente um número"
    if len(numbers) > 20:
        return "Quantidade de números não pode ser maior que 20"
    return reduce(lambda x, y: x - y, numbers)

def multiply(numbers):
    if len(numbers) == 0:
        return "Sem números"
    if len(numbers) == 1:
        return "Somente um número"
    if len(numbers) > 20:
        return "Quantidade de números não pode ser maior que 20"
    return reduce(lambda x, y: x * y, numbers)

def divide(numbers):
    if len(numbers) == 0:
        return "Sem números"
    if len(numbers) == 1:
        return "Somente um número"
    if len(numbers) > 20:
        return "Quantidade de números não pode ser maior que 20"
    if 0 in numbers[1:]:
        return "Impossivel dividir por 0"
    return reduce(lambda x, y: x / y, numbers)

def main():

    server_ip = os.getenv("SERVER_LOCAL")
    server_port = int(os.getenv("SERVER_PORT"))

    server = SimpleXMLRPCServer((server_ip, server_port))
    server.register_function(add, "add")
    server.register_function(subtract, "subtract")
    server.register_function(multiply, "multiply")
    server.register_function(divide, "divide")

    print(f"Servidor XML-RPC rodando em {server_ip}:{server_port}")
    server.serve_forever()

if __name__ == "__main__":
    main()
