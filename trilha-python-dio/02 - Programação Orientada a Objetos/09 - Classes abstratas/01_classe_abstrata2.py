from abc import ABC, abstractmethod

class Controle(ABC):

    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

class ControleTV(Controle):
    def ligar(self):
        print("ligando")
    
    def desligar(self):
        print("desligando")

controletv = ControleTV()
controletv.ligar()    
controletv.desligar()    