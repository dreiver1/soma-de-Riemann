import unittest

import sympy
from Soma import Soma
import math


class TestandoIntegral(unittest.TestCase):
    def test_integralDupla(self):
        soma = Soma()
        assert math.isclose(
            soma.intgralDupla(0, 2, 0, 2, sympy.sympify("x+y")),
            8,
            rel_tol=1e-6,
            abs_tol=1
            )
    
    def test_integralDupla02(self):
        soma = Soma()
        assert math.isclose(
            soma.intgralDupla(0, 2, 0, 2, sympy.sympify("x+y")),
            8,
            rel_tol=1e-6,
            abs_tol=1
            )

if __name__ == '__main__':
    unittest.main()