import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 15560

server.bind((host, port))
print('Binded')

server.listen(5000)
client, client_adress = server.accept()
received_string = client.recv(1024).decode('utf-8')
print(received_string)

client.close()
server.close()


