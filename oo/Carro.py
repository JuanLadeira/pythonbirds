"""
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> # testando direcao
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_esquerda()
    >>> direcao.valor
    'Leste'
    >>> #testando carro
    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    'Leste'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Sul'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Norte'
    """
NORTE = 'Norte'
OESTE = 'Oeste'
LESTE = 'Leste'
SUL = 'Sul'


class Carro:
    def __init__(self, direcao, motor):
        self.motor = motor
        self.direcao = direcao

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def calcular_direcao(self):
        return self.direcao.valor

    def girar_a_direita(self):
        self.direcao.girar_direita()

    def girar_a_esquerda(self):
        self.direcao.girar_esquerda()


class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)


class Direcao:
    rotacao_a_direita_dct = {
        NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE
    }
    rotacao_a_esquerda_dct = {
        NORTE: OESTE, OESTE: SUL, SUL: LESTE, LESTE: NORTE
    }

    def __init__(self):
        self.valor = NORTE

    def girar_direita(self):
        self.valor = self.rotacao_a_direita_dct[self.valor]

    def girar_esquerda(self):
        self.valor = self.rotacao_a_esquerda_dct[self.valor]
