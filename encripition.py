#coding utf-8
from numpy import mod

class RSA():

    def __init__(self):
        self.__p = 3
        self.__q = 7
        self.__n = self.__p * self.__q
        self.__phi = (self.__p - 1) * (self.__q - 1)
        self.__e = 17
        self.__d = pow(self.__p,self.__q, self.__d)

    def getPublicKey (self):
        return self.__d

    def writeMSG(self, MSG):
        pass