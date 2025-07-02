class Estudante:
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
    
    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"


def mostrar_valores(*objetos):
    for obj in objetos:
        print(obj)

aluno_1 = Estudante("Raylan", 1)
aluno_2 = Estudante("Debora", 2)
mostrar_valores(aluno_1, aluno_2)

aluno_1.matricula = 3
mostrar_valores(aluno_1, aluno_2)

Estudante.escola = "Python"
aluno_3 = Estudante("Felipe", 4)
mostrar_valores(aluno_1, aluno_2, aluno_3)

