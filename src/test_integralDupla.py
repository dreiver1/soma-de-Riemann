import unittest
from main import getExpressao
from main import intgralDupla
import math


class TestandoIntegral(unittest.TestCase):
    def test_integralDupla(self):
        limiteInfX = 0
        limiteSupX = 2
        limiteInfY = 0
        limiteSupY = 2
        expressao = getExpressao("x+y")
        assert math.isclose(intgralDupla(limiteInfX, limiteSupX, limiteInfY, limiteSupY, expressao), 8, rel_tol=1e-6, abs_tol=1)

if __name__ == '__main__':
    unittest.main()