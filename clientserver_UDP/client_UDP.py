import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Client is running...")

host = "localhost"
port = 5433
mensagem = "Hello, Server!"

try:
    print(f"Sending message to {host}:{port}")
    s.sendto(mensagem.encode(), (host, port))

    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print(f"Received from server: {dados}")

finally:
    print("Closing connection")
    s.close()
    print("Connection closed")
