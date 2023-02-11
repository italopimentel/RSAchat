#coding utf-8

class RSA():

    def __init__(self):
        self.__p = 11
        self.__q = 17
        self.__n = self.__p * self.__q
        self.__phi_n = (self.__p - 1) * (self.__q - 1)
        self.__e = 23
        self.__d = 7

    def getPublicKey (self):
        return {'e': self.__e}

    def encryptMSG(self, MSG):
        num_cifrado = []
        for c in MSG:
            resto = (ord(c)**self.__e) % self.__n
            num_cifrado.append(resto)

        mensagem_cifrada = []
        for num in num_cifrado:
            mensagem_cifrada.append(chr(num))
        return "".join(mensagem_cifrada)

    def decryptMSG(self, MSG):
        num_cifrado = []
        for c in MSG:
            resto = (ord(c)**self.__d) % self.__n
            num_cifrado.append(resto)

        mensagem_real = []
        for num in num_cifrado:
            mensagem_real.append(chr(num))
        return "".join(mensagem_real)

