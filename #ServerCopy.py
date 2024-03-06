#ServerCopy
from socket import *
import threading
import random

def performOperation(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'random':
        return random.randint(num1, num2)
    else:
        return None

def handleClient(clientSocket, clientAddress):
    operation = clientSocket.recv(1024).decode('utf-8')

    if operation == 'add' or operation == 'subtract':
        receivedNumbers = False
        if not receivedNumbers:
            numbersData = clientSocket.recv(1024).decode('utf-8')
            num1, num2 = map(int, numbersData.split(','))
            receivedNumbers = True

        result = performOperation(num1, num2, operation)
        if result is not None:
            clientSocket.send(f"Result: {result}".encode('utf-8'))
        else:
            clientSocket.send("Invalid operation".encode('utf-8'))
    elif operation == 'random':
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        clientSocket.send(f"Random Numbers: {num1} and {num2}".encode('utf-8'))
        rangeData = clientSocket.recv(1024).decode('utf-8')
        x, y = map(int, rangeData.split(','))
        result = performOperation(x, y, operation)
        clientSocket.send(f"Random Number: {result}".encode('utf-8'))
    else:
        clientSocket.send("Invalid operation".encode('utf-8'))
        clientSocket.close()

def main(): 
    serverPort = 8888

    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', serverPort))
    serverSocket.listen(1)
    print("Server listening on port 8888...")

    while True:
        clientSocket, clientAddress = serverSocket.accept()
        threading.Thread(target=handleClient,args=(clientSocket, clientAddress)).start()
        print(f"Accepted connection from {clientAddress}")
if __name__ == "__main__":
    main()