class Estudante:
    escola = "DIO"
    def __init__(self, nome, matricula):
        self.nome=nome
        self.matricula=matricula
    def __str__(self) -> str:
        return f"Aluno: {self.nome}\tMatrícula: {self.matricula}\tEscola: {self.escola}"
        
aluno1 = Estudante("Alisson", 1)
aluno2 = Estudante("Wendel", 2)

print(aluno1, aluno2)