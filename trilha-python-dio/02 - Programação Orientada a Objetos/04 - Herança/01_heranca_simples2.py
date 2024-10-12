class veiculo:
    
    def __init__(self, cor, placa, numero_rodas):
        self.cor=cor,
        self.placa=placa,
        self.numero_rodas=numero_rodas

    def ligar_veiculo(self):
        print("Ligando veículo")

class moto(veiculo):
    def __init__(self, cor, placa, numero_rodas, rota):
        super().__init__(cor, placa, numero_rodas)
        self.rota=rota
    
    def esta_em_rota(self):
        print(f"{'Sim' if self.rota else 'Não'} estou em rota")    

class carro(veiculo):
    pass

class caminhao(veiculo):
    pass

moto1 = moto('Branco', 'gte-0001', 2, False)
moto1.ligar_veiculo()
moto1.esta_em_rota()

carro1 = carro('Preto', 'gte1001', 4)