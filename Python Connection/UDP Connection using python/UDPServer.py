import socket

HOST = "127.0.0.1"
PORT = 5001

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))

print("UDP Server is waiting...")

data, addr = server.recvfrom(1024)

print("Client:", data.decode())

reply = input("Enter reply: ")
server.sendto(reply.encode(), addr)

server.close()