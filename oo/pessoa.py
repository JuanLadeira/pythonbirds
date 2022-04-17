class Pessoa:
    def __init__(self, nome=None, idade = None):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return 'olá, meu bom.'

    pass


if __name__ == '__main__':
    p = Pessoa()
    print(p.cumprimentar())
    print(p.nome)
    print(p.idade)
