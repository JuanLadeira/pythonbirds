from unittest import TestCase

from oo.Carro import Motor


class CarroTestCase(TestCase):
    def test_velocidade_inicial(self):
        motor = Motor()
        self.assertEqual(0, motor.velocidade)
    def test_acelerar(self):
        motor = Motor()
        motor.acelerar()
        self.assertEqual(1, motor.velocidade)

    