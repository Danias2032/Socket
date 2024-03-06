#ClientJson
from socket import *
import json

serverName = 'localhost'
serverPort = 8888

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

try:
    operation = input("Choose an operation ('add', 'subtract', or 'random'): ")
    data = {"operation": operation}

    if operation in ['add', 'subtract']:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        data["num1"] = num1
        data["num2"] = num2

    clientSocket.send(json.dumps(data).encode('utf-8'))

    if operation == 'random':
        pass
    else:
        result_data = clientSocket.recv(1024).decode('utf-8')
        result = json.loads(result_data)
        
        if 'result' in result:
            print(f'Result from server: {result["result"]}')
        elif 'randomNumber' in result:
            print(f'Random Number from server: {result["randomNumber"]}')
        elif 'error' in result:
            print(f'Error from server: {result["error"]}')

except Exception as e:
    print(f"Error: {str(e)}")
finally:
    clientSocket.close()