class Passaro:
    def __inti__(self):
        pass
    
    def voar(self):
        pass

class Morcego(Passaro):

    def voar(self):
        print("Voando com sonar")

class Avestruz(Passaro):
    def voar(self):
        print("Voando baixo")

def voando(Passaro):
    Passaro.voar()

voando(Avestruz())