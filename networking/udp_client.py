import socket

target_host = "127.0.0.1"
target_port = 80

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.settimeout(5)

try:
    # send data
    string = "Test"
    client.sendto(string.encode('utf-8'),(target_host,target_port))
    # receive data
    data, addr = client.recvfrom(4096)
    print(data.decode('utf-8'))

except socket.timeout:
    print("Connection Timeout: No response received")
