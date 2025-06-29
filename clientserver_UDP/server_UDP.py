import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Client is running...")

host = "localhost"
port = 5432

s.bind((host, port))
mensagem = "Hello, Client!"

while 1:
    dados, end = s.recvfrom(4096)

    if dados:
        print(f"Received from client: {dados.decode()}")
        print(f"Sending message to {end[0]}:{end[1]}")
        s.sendto(mensagem.encode(), end)
