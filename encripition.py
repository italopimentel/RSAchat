#coding utf-8
from numpy import mod

class RSA():

    def __init__(self):
        self.__p = 7
        self.__q = 13
        self.__n = self.__p * self.__q
        self.__phi_n = (self.__p - 1) * (self.__q - 1)
        self.__e = 53
        self.__d = 125

        #phi_n = 72
        #chave pública: e=23 n= 91

        #chave privada: d=7 n= 91

    def getPublicKey (self):
        return {'e': self.__e}

    def criptyMSG(self, MSG):
        num_cifrado = []
        for c in MSG:
            (ord(c)**self.__e) % self.__n
            num_cifrado.append(c)

        mensagem_cifrada = ""
        for num in mensagem_cifrada:
            mensagem_cifrada += chr(num)
        return mensagem_cifrada

    def decryptMSG(self, MSG):
        num_cifrado = []
        for c in MSG:
            (ord(c)**self.__d) % self.__n
            num_cifrado.append(c)
        mensagem_real = ""
        for num in mensagem_real:
            mensagem_real += chr(num)
        return mensagem_real