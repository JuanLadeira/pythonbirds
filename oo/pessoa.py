class Pessoa:
    def __init__(self, *filhos, nome=None, idade=None):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return 'olá, meu bom.'

    pass


if __name__ == '__main__':
    Ruan = Pessoa('Maiara', 'Felipe', 'Fernando', nome='Ruan')
    print(Ruan.cumprimentar())
    print(Ruan.nome)
    print(Ruan.idade)
    print(Ruan.filhos)
    Ruan.sobrenome = 'Carlos'
    print(Ruan.__dict__)
    del Ruan.sobrenome
    print(Ruan.__dict__)
