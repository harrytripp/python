import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('127.0.0.1', 80))

while True:
    print("Server live...")
    data, addr = server.recvfrom(4096)
    print(f"Received: {data.decode('utf-8')}")
    server.sendto(data, addr)
