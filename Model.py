import socket
from mailbox import Message


class Server:

    #--- Constructor ---#
    def __init__(self):

        self.ServerIP = socket.gethostbyname(socket.gethostname())
        self.Port = 8080

    def Start(self):
        print("Server Initializing ...")
        ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ServerSocket.bind((self.ServerIP, self.Port))
        print("Server Started")
        ServerSocket.listen(5)
        print("Server Listening ...")

        while True:
            ClientSocket, ClientAddr = ServerSocket.accept()
            Message = ClientSocket.recv(1024).decode()
            print(Message)
            ClientSocket.send(f"Connected to {self.ServerIP}".encode())

class Client:

    # --- Constructor ---#
    def __init__(self, Name):
        self.ServerIP = socket.gethostbyname(socket.gethostname())
        self.Port = 8080
        self.Name = Name

    def Connect(self):
        ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ClientSocket.connect((self.ServerIP, self.Port))
        ClientSocket.send(f"{self.Name} joined.".encode())
        Message = ClientSocket.recv(1024).decode()
        print(Message)