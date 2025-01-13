import socket
HOST = "127.0.0.1"     #loopback interface address(localhost)
PORT = 9999             #Non privilaged port numbers > 1023
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen()
    conn,addr = s.accept()
    # This line accepts the incoming connection. The accept() returns a 
    #socket object(conn) that is connected to the client amd also the 
    #address of the client(addr)
    with conn:
        print("Connected by",addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            upper_data=data.decode().upper()
            conn.sendall(upper_data.encode())
