import socket
from encripition import RSA

crypto = RSA()
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 15560

client.connect((host, port))
print('Conectando...')
string_to_send = crypto.criptyMSG(input('Digite a mensagem: '))
client.send(string_to_send.encode('utf-8'))

