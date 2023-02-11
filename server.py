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
received_string_criptografada = client.recv(1024).decode("utf-8")
print("a mensagem criptografada recebida pelo servidor foi: {} ".format(received_string_criptografada))
received_string_decriptografada = rsa.decryptMSG(received_string_criptografada)
print("após a descriptografia ficou : {} ".format(received_string_decriptografada))
client.close()
server.close()


