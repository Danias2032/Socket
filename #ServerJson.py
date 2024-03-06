#ServerJson
from socket import *
import threading
import json
import random

def performOperation(data):
    num1 = data.get('num1', 0)
    num2 = data.get('num2', 0)
    operation = data.get('operation', '')

    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'random':
        return random.randint(num1, num2)
    else:
        return None

def handleClient(clientSocket, clientAddress):
    try:
        operationData = clientSocket.recv(1024).decode('utf-8')
        data = json.loads(operationData)

        if data['operation'] in ['add', 'subtract']:
            result = performOperation(data)
            if result is not None:
                response = {"result": result}
            else:
                response = {"error": "Invalid operation"}
        elif data['operation'] == 'random':
            num1 = random.randint(1, 100)
            num2 = random.randint(1, 100)
            response = {"randomNumbers": [num1, num2]}
            clientSocket.send(json.dumps(response).encode('utf-8'))

            rangeData = clientSocket.recv(1024).decode('utf-8')
            rangeData = json.loads(rangeData)
            result = performOperation(rangeData)
            response = {"randomNumber": result}
        else:
            response = {"error": "Invalid operation"}

        clientSocket.send(json.dumps(response).encode('utf-8'))

    except Exception as e:
        print(f"Error handling client {clientAddress}: {str(e)}")
    finally:
        clientSocket.close()

def main(): 
    serverPort = 8888

    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', serverPort))
    serverSocket.listen(1)
    print("Server listening on port 8888...")

    while True:
        clientSocket, clientAddress = serverSocket.accept()
        threading.Thread(target=handleClient, args=(clientSocket, clientAddress)).start()
        print(f"Accepted connection from {clientAddress}")

if __name__ == "__main__":
    main() 