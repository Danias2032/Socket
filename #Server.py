#Server
from socket import *
import random

def perform_operation(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'random':
        return random.randint(num1, num2)
    else:
        return None

def handle_client(client_socket):
    # Receive the operation choice from the client
    operation = client_socket.recv(1024).decode('utf-8')

    if operation == 'add' or operation == 'subtract':
        # Check if the server has already received numbers
        received_numbers = False

        if not received_numbers:
            # Receive the user-input numbers from the client
            numbers_data = client_socket.recv(1024).decode('utf-8')
            num1, num2 = map(int, numbers_data.split(','))

            received_numbers = True

        # Perform the specified operation
        result = perform_operation(num1, num2, operation)

        if result is not None:
            # Send the result back to the client
            client_socket.send(f"Result: {result}".encode('utf-8'))
        else:
            # If the operation is not valid, send an error message
            client_socket.send("Invalid operation".encode('utf-8'))

    elif operation == 'random':
        # Generate two random numbers
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)

        # Send the random numbers to the client
        client_socket.send(f"Random Numbers: {num1} and {num2}".encode('utf-8'))

        # Receive additional information if needed
        range_data = client_socket.recv(1024).decode('utf-8')
        x, y = map(int, range_data.split(','))

        # Generate a random number in the specified range
        result = perform_operation(x, y, operation)

        # Send the random number back to the client
        client_socket.send(f"Random Number: {result}".encode('utf-8'))

    else:
        # If the operation is not valid, send an error message
        client_socket.send("Invalid operation".encode('utf-8'))

    # Close the client socket
    client_socket.close()

def main():
    # Create a TCP socket
    server_socket = socket(AF_INET, SOCK_STREAM)

    # Bind the socket to a specific address and port
    server_socket.bind(('localhost', 8888))

    # Listen for incoming connections
    server_socket.listen(5)
    print("Server listening on port 8888...")

    while True:
        # Accept a connection from a client
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")

        # Handle the client in a separate thread or process for concurrency
        handle_client(client_socket)

if __name__ == "__main__":
    main()

    