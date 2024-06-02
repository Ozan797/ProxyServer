# Import necessary modules
import socket

TARGET_HOST = "www.ozangokberk.com"
TARGET_PORT = 80


def start_proxy_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # IPv4 & TCP
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Proxy server running on {host}:{port}")
    
    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")
        
        request = client_socket.recv(1024).decode()
        print("Received request:")
        print(request)
        
        target_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        target_socket.connect((TARGET_HOST, TARGET_PORT))
        target_socket.sendall(request.encode())
        
        response = target_socket.recv(4096)
        print("Received response:")
        print(response.decode())
        
        
        
        client_socket.close()
        target_socket.close()
        
start_proxy_server('localhost', 4500)