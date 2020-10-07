class Fita:
    def __init__(self, cadeia):
        self.__cadeia = "> " + cadeia + "  "

    def setFita(self, novaCadeia):
        self.__cadeia = novaCadeia

    def getFita(self):
        return self.__cadeia