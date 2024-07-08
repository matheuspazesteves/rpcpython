import os
import xmlrpc.client
from dotenv import load_dotenv

load_dotenv()

def main():
    server_ip = os.getenv("SERVER_IP")
    server_port = int(os.getenv("SERVER_PORT"))


    server_url = f"http://{server_ip}:{server_port}/"
    client = xmlrpc.client.ServerProxy(server_url)

    while True:
        operation = input("Escolha a operação (+, -, *, /) ou 'sair' para encerrar: ")
        if operation.lower() == 'sair':
            break
        numbers = input("Digite os números separados por espaço: ")
        numbers = list(map(float, numbers.split()))

        try:
            if operation == '+':
                result = client.add(numbers)
            elif operation == '-':
                result = client.subtract(numbers)
            elif operation == '*':
                result = client.multiply(numbers)
            elif operation == '/':
                result = client.divide(numbers)
            else:
                print("Operação inválida. Tente novamente.")
                continue

            print(f"Resultado: {result}")
        except Exception as e:
            print(f"Erro: {e}")

if __name__ == "__main__":
    main()
