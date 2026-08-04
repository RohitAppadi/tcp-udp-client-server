import socket

HOST = "127.0.0.1"
PORT = 5001

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

msg = input("Enter message: ")

client.sendto(msg.encode(), (HOST, PORT))

reply, _ = client.recvfrom(1024)

print("Server:", reply.decode())

client.close()