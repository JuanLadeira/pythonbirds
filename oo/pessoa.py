class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=None):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return 'olá, meu bom.'

    pass


if __name__ == '__main__':
    ruan = Pessoa('Maiara', 'Felipe', 'Fernando', nome='Ruan')
    print(ruan.cumprimentar())
    print(ruan.nome)
    print(ruan.idade)
    print(ruan.filhos)
    ruan.sobrenome = 'Carlos'
    ruan.olhos = 1
    print(ruan.__dict__, f'Ruan tem {ruan.olhos} olho.')
    Pessoa.olhos = 3
    del ruan.olhos
    del ruan.sobrenome
    print(ruan.__dict__, f'Ruan tem {ruan.olhos} olhos.')
