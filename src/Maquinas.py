from Cabecote import *
from Fita import *

class Maquina:
    def __init__(self,cadeia, cadeia_2=''):
        self.__cabecote = Cabecote() # controle finito
        self.__fita = Fita(cadeia)
        self.__fita_2 = Fita(cadeia_2)
        self.__fimDaConfiguracao = len(cadeia)+2
        self.__fimDaConfiguracao_2 =0
        self.__permitir = True

    def getFimDaConfiguracao(self):
        return self.__fimDaConfiguracao
    def getFita(self):
        return self.__fita
    def getFita_2(self):
        return self.__fita_2

    def aux_transicao(self, estado, posicao, posicao_2=2):
        # função do contrele finito que seta um estado, faz com o cabeçote ande para direita ou esquerda e imprime o resultado na tela.
        self.__cabecote.setEstado(estado)
        if self.__cabecote.getPosicao_1()== self.__fimDaConfiguracao:
            self.__fimDaConfiguracao = self.__cabecote.getPosicao_1()+1

        if posicao_2 in [1,-1,0]:
            self.__cabecote.setPosicao_1(posicao)
            self.__cabecote.setPosicao_2(posicao_2)
            if self.__cabecote.getPosicao_2() > self.__fimDaConfiguracao_2:
                self.__fimDaConfiguracao_2 = self.__cabecote.getPosicao_2()
            if self.__cabecote.getPosicao_2() < self.__fimDaConfiguracao_2 and self.__permitir == True:
                self.__fimDaConfiguracao_2 +=1
                self.__permitir = False
            self.imprimir_soma()
        elif posicao_2 ==2:
            self.__cabecote.setPosicao_1(posicao)
            self.imprimir()

    def aux_set_transicao(self, estado, simbolo, simbolo_2=''):
        # função do contrele finito que seta um estado, escreve um simbolo na posicão atual do cabeçote e imprime o resultado na tela.
        self.__cabecote.setEstado(estado)
        if self.__cabecote.getPosicao_1()== self.__fimDaConfiguracao:
            self.__fimDaConfiguracao = self.__cabecote.getPosicao_1()+1
        if simbolo_2 != '':
            # se a maquina tiver duas fitas e dois cabeçotes.
            self.__fita.setFita(self.__fita.getFita()[:self.__cabecote.getPosicao_1()] + str(simbolo) + self.__fita.getFita()[self.__cabecote.getPosicao_1() + 1:])
            self.__fita_2.setFita(self.__fita_2.getFita()[:self.__cabecote.getPosicao_2()] + str(simbolo_2) + self.__fita_2.getFita()[self.__cabecote.getPosicao_2() + 1:])
            if self.__cabecote.getPosicao_2() > self.__fimDaConfiguracao_2:
                self.__fimDaConfiguracao_2 = self.__cabecote.getPosicao_2()
            self.imprimir_soma()
        elif simbolo_2 == '':
            # se a maquina tiver 1 fitas e 1 cabeçote.
            self.__fita.setFita(self.__fita.getFita()[:self.__cabecote.getPosicao_1()] + str(simbolo) + self.__fita.getFita()[self.__cabecote.getPosicao_1() + 1:])
            self.imprimir()

    def imprimir_soma(self):
        print("|─("+(self.__cabecote.getEstado() + ", ")+(self.__fita.getFita()[:self.__cabecote.getPosicao_1()] + "|" + self.__fita.getFita()[self.__cabecote.getPosicao_1()] + "|" + self.__fita.getFita()[self.__cabecote.getPosicao_1() + 1:self.__fimDaConfiguracao])+", "+
              (self.__fita_2.getFita()[:self.__cabecote.getPosicao_2()] + "|" + self.__fita_2.getFita()[self.__cabecote.getPosicao_2()] + "|" + self.__fita_2.getFita()[self.__cabecote.getPosicao_2() + 1:self.__fimDaConfiguracao_2])+")")

    def imprimir(self):
        print("|─("+(self.__cabecote.getEstado() + ", ")+(self.__fita.getFita()[:self.__cabecote.getPosicao_1()] + "|" + self.__fita.getFita()[self.__cabecote.getPosicao_1()] + "|" + self.__fita.getFita()[self.__cabecote.getPosicao_1() + 1:self.__fimDaConfiguracao])+")")

    def imprimir_primeira_configuracao(self):
        print("("+(self.__cabecote.getEstado() + ", ")+(self.__fita.getFita()[:self.__cabecote.getPosicao_1()] + "|" + self.__fita.getFita()[self.__cabecote.getPosicao_1()] + "|" + self.__fita.getFita()[self.__cabecote.getPosicao_1() + 1:self.__fimDaConfiguracao])+")")

    def imprimir_primeira_configuracao_soma(self):
        print("("+(self.__cabecote.getEstado() + ", ")+(self.__fita.getFita()[:self.__cabecote.getPosicao_1()] + "|" + self.__fita.getFita()[self.__cabecote.getPosicao_1()] + "|" + self.__fita.getFita()[self.__cabecote.getPosicao_1() + 1:self.__fimDaConfiguracao])+", "+
              (self.__fita_2.getFita()[:self.__cabecote.getPosicao_2()] + "|" + self.__fita_2.getFita()[self.__cabecote.getPosicao_2()] + "|" + self.__fita_2.getFita()[self.__cabecote.getPosicao_2() + 1:self.__fimDaConfiguracao_2])+")")

    def R_vazio(self, posicao):
        # Regras de transição de uma máquina que faz a posição do cabeçote se deslocar para a direita até encontrar um " "
        while self.__cabecote.getEstado() != 'R_h':
            if self.__fita.getFita()[self.__cabecote.getPosicao_1()] == '>':  # 1
                self.aux_transicao(self.__cabecote.getEstado(), 1)
            elif self.__fita.getFita()[self.__cabecote.getPosicao_1()] == '1':
                self.aux_transicao("R_q0", 1)
            elif self.__fita.getFita()[self.__cabecote.getPosicao_1()] == '0':
                self.aux_transicao("R_q1", 1)
            elif self.__fita.getFita()[self.__cabecote.getPosicao_1()] == ' ':
                self.aux_transicao("R_h", 0)

    def R_Nvazio(self, posicao):
        # Regras de transição de uma máquina que faz a posição do cabeçote se deslocar para a direita até encontrar um " "
        while self.__cabecote.getEstado() != 'R_Nh':
            if self.__fita.getFita()[self.__cabecote.getPosicao_1()] == '>':  # 1
                self.aux_transicao(self.__cabecote.getEstado(), 1)
            elif self.__fita.getFita()[self.__cabecote.getPosicao_1()] == ' ':
                self.aux_transicao("R_Nq0", 1)
            elif self.__fita.getFita()[self.__cabecote.getPosicao_1()] != ' ':
                self.aux_transicao("R_Nh", 0)

    def L_vazio(self, posicao):
        # Regras de transição de uma máquina que faz a posição do cabeçote se deslocar para a direita até encontrar um " "
        while self.__cabecote.getEstado() != 'L_h':
            if self.__fita.getFita()[self.__cabecote.getPosicao_1()] == '>':  # 1
                self.aux_transicao(self.__cabecote.getEstado(), 1)
            elif self.__fita.getFita()[self.__cabecote.getPosicao_1()] == '1':
                self.aux_transicao("L_q0", -1)
            elif self.__fita.getFita()[self.__cabecote.getPosicao_1()] == '0':
                self.aux_transicao("L_q1", -1)
            elif self.__fita.getFita()[self.__cabecote.getPosicao_1()] == ' ':
                self.aux_transicao("L_h", 0)

    def L_Nvazio(self, posicao):
        # Regras de transição de uma máquina que faz a posição do cabeçote se deslocar para a direita até encontrar um " "
        while self.__cabecote.getEstado() != 'L_Nh':
            if self.__fita.getFita()[self.__cabecote.getPosicao_1()] == '>':  # 19
                self.aux_transicao(self.__cabecote.getEstado(), 1)
            elif self.__fita.getFita()[self.__cabecote.getPosicao_1()] == ' ':
                self.aux_transicao("L_Nq0", -1)
            elif self.__fita.getFita()[self.__cabecote.getPosicao_1()] != ' ':
                self.aux_transicao("L_Nh", 0)

    def shift(self, posicao):
        # Regras de transição de uma máquina que desloca toda a cadeia escrita na fita para a direita em.
        self.__cabecote.setEstado("Sq0")
        self.imprimir()
        while self.__cabecote.getEstado() != 'Sh':
            if self.__fita.getFita()[self.__cabecote.getPosicao_1()] == '>':  # 19
                self.aux_transicao(self.__cabecote.getEstado(), 1)
            elif self.__cabecote.getEstado() == "Sq0" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == ' ':  # 1
                self.aux_transicao("Sq1", -1)
            elif self.__cabecote.getEstado() == "Sq1" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == ' ':  # 2
                self.aux_transicao("Sq2", 1)
            elif self.__cabecote.getEstado() == "Sq2" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == '1':  # 3
                self.aux_transicao("Sq2", 1)
            elif self.__cabecote.getEstado() == "Sq2" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == '0':  # 4
                self.aux_transicao("Sq2", 1)
            elif self.__cabecote.getEstado() == "Sq2" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == ' ':  # 5
                self.aux_set_transicao('Sh', ' ')
            elif self.__cabecote.getEstado() == "Sq1" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == '1':  # 6
                self.aux_set_transicao("Sq3", " ")
            elif self.__cabecote.getEstado() == "Sq3" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == ' ':  # 7
                self.aux_transicao("Sq4", 1)
            elif self.__cabecote.getEstado() == "Sq4" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == ' ':  # 8
                self.aux_set_transicao("Sq5", "1")
            elif self.__cabecote.getEstado() == "Sq5" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == '1':  # 9
                self.aux_transicao("Sq6", -1)
            elif self.__cabecote.getEstado() == "Sq6" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == '0':  # 11
                self.aux_set_transicao("Sq1", "0")
            elif self.__cabecote.getEstado() == "Sq6" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == '1':  # 12
                self.aux_set_transicao("Sq1", "1")
            elif self.__cabecote.getEstado() == "Sq6" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == ' ':  # 13
                self.aux_transicao("Sq1", -1)
            elif self.__cabecote.getEstado() == "Sq1" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == '0':  # 14
                self.aux_set_transicao("Sq7", " ")
            elif self.__cabecote.getEstado() == "Sq7" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == ' ':  # 15
                self.aux_transicao("Sq8", 1)
            elif self.__cabecote.getEstado() == "Sq8" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == ' ':  # 16
                self.aux_set_transicao("Sq9", "0")
            elif self.__cabecote.getEstado() == "Sq9" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == '0':  # 17
                self.aux_transicao("Sq6", -1)

    def divisor(self):
        # função que roda a máquina de turing que faz divisão exata por 2.
        # função que contém as regras de transição da maquina e que chama o controle finito de acordo com o estado, posição e simbolo no cabeçote.
        self.imprimir_primeira_configuracao()
        while self.__cabecote.getEstado() != 'h':
            if self.__fita.getFita()[self.__cabecote.getPosicao_1()] == '>':  # 1
                # Se o cabeçote estiver no simbolo ">" o controle finito mantêm o estado atual e o cabeçote vai para a direita.
                self.aux_transicao((self.__cabecote.getEstado()), 1)
            elif self.__cabecote.getEstado() == "q0" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == ' ': #2
                self.aux_transicao("q1", 1)
            elif self.__cabecote.getEstado() == "q1" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == '0': #3
                self.aux_transicao("q1", 1)
            elif self.__cabecote.getEstado() == "q1" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == '1': #4
                self.aux_transicao("q1", 1)
            elif self.__cabecote.getEstado() == "q1" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == ' ': #5 # (-)
                self.aux_transicao("q2", -1)
            elif self.__cabecote.getEstado() == "q2" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == '1': #6 #SET
                self.aux_set_transicao("q2"," ")
            elif self.__cabecote.getEstado() == "q2" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == '0': #7 #SET
                self.aux_set_transicao("q2"," ")
            elif self.__cabecote.getEstado() == "q2" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == ' ': #8 #SET
                self.aux_set_transicao("h"," ")

    def antecessor(self):
        # função que roda a máquina de turing antecessor.
        # função que contém as regras de transição da maquina e que chama o controle finito de acordo com o estado, posição e simbolo no cabeçote.
        self.imprimir_primeira_configuracao()
        while self.__cabecote.getEstado() != 'h':
            if self.__fita.getFita()[self.__cabecote.getPosicao_1()] == '>':  # 1
                # Se o cabeçote estiver no simbolo ">" o controle finito mantêm o estado atual e o cabeçote vai para a direita.
                self.aux_transicao((self.__cabecote.getEstado()), 1)
            elif self.__cabecote.getEstado() == "q0" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == ' ':  # 2
                self.aux_transicao("q1", 1)

            elif self.__cabecote.getEstado() == "q1" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == '0':  # 3
                self.aux_transicao("q1", 1)
            elif self.__cabecote.getEstado() == "q1" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == '1':  # 4
                self.aux_transicao("q1", 1)
            elif self.__cabecote.getEstado() == "q1" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == ' ':  # 5
                self.aux_transicao("q2", -1)

            elif self.__cabecote.getEstado() == "q2" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == '0':  # 6
                self.aux_set_transicao("q3", "1")
            elif self.__cabecote.getEstado() == "q2" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == '1':  # 7
                self.aux_set_transicao("q3", "0")
            elif self.__cabecote.getEstado() == "q3" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == '1':  # 8
                self.aux_transicao("q2", -1)
            elif self.__cabecote.getEstado() == "q3" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == '0':  # 9
                self.aux_set_transicao("h","0", "")

    def sucessor(self):
        # função que roda a máquina de turing sucessor.
        # função que contém as regras de transição da maquina e que chama o controle finito de acordo com o estado e posição e simbolo no cabeçote.
        self.imprimir_primeira_configuracao()
        while self.__cabecote.getEstado() not in('h', "Sh"):
            if self.__fita.getFita()[self.__cabecote.getPosicao_1()] == '>': #1
                # Se o cabeçote estiver no simbolo ">" o controle finito mantêm o estado atual e o cabeçote vai para a direita.
                self.aux_transicao(self.__cabecote.getEstado(),1)
            elif self.__cabecote.getEstado() == "q0" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == ' ':  # 2
                self.aux_transicao("q1", 1)

            elif self.__cabecote.getEstado() == "q1" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == '1':  # 3
                self.aux_transicao("q1", 1)
            elif self.__cabecote.getEstado() == "q1" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == '0':  # 4
                self.aux_transicao("q1", 1)
            elif self.__cabecote.getEstado() == "q1" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == ' ':  # 5
                self.aux_transicao("q2", -1)

            elif self.__cabecote.getEstado() == "q2" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == '0':  # 6
                self.aux_set_transicao("q3","1")
            elif self.__cabecote.getEstado() == "q3" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == '1':  # 7
                self.aux_set_transicao("h","1", '')

            elif self.__cabecote.getEstado() == "q2" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == '1':  # 8
                self.aux_set_transicao("q3","0")
            elif self.__cabecote.getEstado() == "q3" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == '0':  # 9
                self.aux_transicao("q2", -1)

            elif self.__cabecote.getEstado() == "q2" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == ' ':  # 10
                self.aux_set_transicao("q4", "1")

            elif self.__cabecote.getEstado() == "q4" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == "1": # 11
                self.R_vazio(self.__cabecote.getPosicao_1())
                self.shift(self.__cabecote.getPosicao_1())

    def soma(self):
        # função que roda a máquina de turing soma.
        # função que contém as regras de transição da maquina e que chama o controle finito de acordo com o estado, posição e simbolo no cabeçote.
        self.imprimir_primeira_configuracao_soma()
        while self.__cabecote.getEstado() != 'h':
            if self.__cabecote.getEstado() == "q0" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == ' '  and self.__fita_2.getFita()[self.__cabecote.getPosicao_2()] == " ":
                self.aux_transicao("q0",+1,+1)
            elif self.__cabecote.getEstado() == "q0" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == "1"  and self.__fita_2.getFita()[self.__cabecote.getPosicao_2()] == " ":
                self.aux_set_transicao("q1","0","1")
            elif self.__cabecote.getEstado() == "q1" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == '0'  and self.__fita_2.getFita()[self.__cabecote.getPosicao_2()] == "1":
                self.aux_transicao("q0",+1,+1)
            elif self.__cabecote.getEstado() == "q0" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == "0"  and self.__fita_2.getFita()[self.__cabecote.getPosicao_2()] == " ":
                self.aux_set_transicao("q1","0","0")
            elif self.__cabecote.getEstado() == "q1" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == '0'  and self.__fita_2.getFita()[self.__cabecote.getPosicao_2()] == "0":
                self.aux_transicao("q0",+1,+1)
            elif self.__cabecote.getEstado() == "q0" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == ";"  and self.__fita_2.getFita()[self.__cabecote.getPosicao_2()] == " ":
                self.aux_set_transicao("q2","0"," ")

            elif self.__cabecote.getEstado() == "q2" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == '0'  and self.__fita_2.getFita()[self.__cabecote.getPosicao_2()] == " ":
                self.aux_transicao("q2",+1,0)
            elif self.__cabecote.getEstado() == "q2" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == '1'  and self.__fita_2.getFita()[self.__cabecote.getPosicao_2()] == " ":
                self.aux_transicao("q2",+1,0)

            elif self.__cabecote.getEstado() == "q2" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == ' '  and self.__fita_2.getFita()[self.__cabecote.getPosicao_2()] == " ":
                self.aux_transicao("q3",-1, -1)
            elif self.__cabecote.getEstado() == "q3" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == '0'  and self.__fita_2.getFita()[self.__cabecote.getPosicao_2()] == "0":
                self.aux_set_transicao("q4","0","0")
            elif self.__cabecote.getEstado() == "q4" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == '0'  and self.__fita_2.getFita()[self.__cabecote.getPosicao_2()] == "0":
                self.aux_transicao("q3",-1,-1)
            elif self.__cabecote.getEstado() == "q3" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == '0'  and self.__fita_2.getFita()[self.__cabecote.getPosicao_2()] == "1":
                self.aux_set_transicao("q4","1","1")
            elif self.__cabecote.getEstado() == "q4" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == '1'  and self.__fita_2.getFita()[self.__cabecote.getPosicao_2()] == "1":
                self.aux_transicao("q3",-1,-1)
            elif self.__cabecote.getEstado() == "q3" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == '1'  and self.__fita_2.getFita()[self.__cabecote.getPosicao_2()] == "0":
                self.aux_set_transicao("q4","1","0")
            elif self.__cabecote.getEstado() == "q4" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == '1'  and self.__fita_2.getFita()[self.__cabecote.getPosicao_2()] == "0":
                self.aux_transicao("q3",-1,-1)
            elif self.__cabecote.getEstado() == "q3" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == '1'  and self.__fita_2.getFita()[self.__cabecote.getPosicao_2()] == "1": # vai 1
                self.aux_set_transicao("q5","0","1")

            elif self.__cabecote.getEstado() == "q5" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == '0'  and self.__fita_2.getFita()[self.__cabecote.getPosicao_2()] == "1":
                self.aux_transicao("q6",-1,-1)
            elif self.__cabecote.getEstado() == "q6" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == '0'  and self.__fita_2.getFita()[self.__cabecote.getPosicao_2()] == "1":
                self.aux_set_transicao("q5","0","1")
            elif self.__cabecote.getEstado() == "q6" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == '1'  and self.__fita_2.getFita()[self.__cabecote.getPosicao_2()] == "0":
                self.aux_set_transicao("q5","0","0")
            elif self.__cabecote.getEstado() == "q6" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == '1'  and self.__fita_2.getFita()[self.__cabecote.getPosicao_2()] == "1":
                self.aux_set_transicao("q5","1","1")
            elif self.__cabecote.getEstado() == "q5" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == '1'  and self.__fita_2.getFita()[self.__cabecote.getPosicao_2()] == "1":
                self.aux_transicao("q6",-1,-1)
            elif self.__cabecote.getEstado() == "q6" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == '0'  and self.__fita_2.getFita()[self.__cabecote.getPosicao_2()] == "0":
                self.aux_set_transicao("q7","1","0")

            elif self.__cabecote.getEstado() == "q5" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == '0'  and self.__fita_2.getFita()[self.__cabecote.getPosicao_2()] == "0":
                self.aux_transicao("q6",-1,-1)
            elif self.__cabecote.getEstado() == "q7" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == '1'  and self.__fita_2.getFita()[self.__cabecote.getPosicao_2()] == "0":
                self.aux_transicao("q3",-1,-1)

            elif self.__cabecote.getEstado() == "q3" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] in ("1","0")and self.__fita_2.getFita()[self.__cabecote.getPosicao_2()] == " ":
                self.aux_transicao("q3",-1,0)
            elif self.__cabecote.getEstado() == "q3" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == " " and self.__fita_2.getFita()[self.__cabecote.getPosicao_2()] == " ":
                self.aux_set_transicao("h", " ", " ")

            elif self.__cabecote.getEstado() == "q6" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] in ("1","0") and self.__fita_2.getFita()[self.__cabecote.getPosicao_2()] == " ":
                self.aux_set_transicao("q7","1", " ")
            elif self.__cabecote.getEstado() == "q7" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] in ("1","0") and self.__fita_2.getFita()[self.__cabecote.getPosicao_2()] == " ":
                self.aux_transicao("q7", -1, 0)
            elif self.__cabecote.getEstado() == "q7" and self.__fita.getFita()[self.__cabecote.getPosicao_1()] == ' ' and self.__fita_2.getFita()[self.__cabecote.getPosicao_2()] == " ":
                self.aux_transicao("h", 0, 0)

            # Se o cabeçote estiver no simbolo ">" o controle finito mantêm o estado atual e o cabeçote vai para a direita.
            elif self.__fita.getFita()[self.__cabecote.getPosicao_1()] == '>':
                self.aux_transicao((self.__cabecote.getEstado()),+1,0)
            elif self.__fita_2.getFita()[self.__cabecote.getPosicao_2()] == ">":
                self.aux_transicao((self.__cabecote.getEstado()),0,+1)
            elif self.__fita.getFita()[self.__cabecote.getPosicao_1()] == '>' and self.__fita_2.getFita()[self.__cabecote.getPosicao_2()] == ">":
                self.aux_transicao((self.__cabecote.getEstado()),+1,+1)