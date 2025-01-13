import socket
HOST = "127.0.0.1"     #loopback interface address(localhost)
PORT = 9999             #Non privilaged port numbers > 1023
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    message = input("Enter the text in lowercase: ")
    s.sendall(message.encode())
    data = s.recv(1024)
    print("Received from the server: ",data.decode())