#Client
from socket import *

    # Create a TCP socket
client_socket = socket(AF_INET, SOCK_STREAM)

    # Connect to the server
client_socket.connect(('localhost', 8888))

    # Choose an operation ('add', 'subtract', or 'random')
operation = input("Choose an operation ('add', 'subtract', or 'random'): ")

    # Send the operation choice to the server
client_socket.send(operation.encode('utf-8'))

if operation == 'add' or operation == 'subtract':
        # Get user input for two numbers
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

        # Send the numbers to the server
    data = f"{num1},{num2}"
    client_socket.send(data.encode('utf-8'))

elif operation == 'random':
        # If 'random' operation, no need for additional input
        pass

else:
    print("Invalid operation. Exiting.")
    client_socket.close()

    # Receive and print the result or error message from the server
result = client_socket.recv(1024)
print('From server: ', result.decode())

    # Close the client socket
client_socket.close()


    