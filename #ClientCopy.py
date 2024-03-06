#ClientCopy
from socket import *

serverName = 'localhost'
serverPort = 8888

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
operation = input("Choose an operation ('add', 'subtract', or 'random'): ")
clientSocket.send(operation.encode('utf-8'))
if operation == 'add' or operation == 'subtract':
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    data = f"{num1},{num2}"
    clientSocket.send(data.encode('utf-8'))
elif operation == 'random':
    pass
else:
    print("Invalid operation. Exiting.")
    clientSocket.close()
    
result = clientSocket.recv(1024)
print('From server: ', result.decode())
clientSocket.close()