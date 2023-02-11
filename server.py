import socket
from encripition import RSA

rsa = RSA()
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 15560

server.bind((host, port))
print('Binded')

server.listen(5000)
client, client_adress = server.accept()
received_string_criptografada = client.recv(1024).decode('utf-8')
print("a mensagem criptografada era: " + received_string_criptografada + "\n")
received_string_descriptografada = rsa.decryptMSG(received_string_criptografada)
print("após a descriptografia foi: " + received_string_descriptografada)

client.close()
server.close()


