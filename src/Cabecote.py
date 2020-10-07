from Fita import *
class Cabecote:
    def __init__(self,):
        self.__estado = "q0" # estados
        self.__posicao = 1  # cabeçote 1
        self.__posicao_2 = 1  # cabeçote 2

    def getEstado(self):
        return self.__estado

    def setEstado(self,novoEstado):
        self.__estado = novoEstado

    def getPosicao_1(self):
        return self.__posicao

    def setPosicao_1(self,valor):
        self.__posicao += valor

    def getPosicao_2(self):
        return self.__posicao_2

    def setPosicao_2(self,valor):
        self.__posicao_2 += valor