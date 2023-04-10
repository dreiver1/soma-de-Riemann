
import sympy

class Soma:

    def __init__(self, divisoesNoEixoX=100, divisoesNoEixoy=100):
        self.divisoesNoEixoX = divisoesNoEixoX
        self.divisoesNoEixoy = divisoesNoEixoy

    def getLimite(self, msg):
        try:
            limiteInfX = int(input(msg))
            return limiteInfX
        except:
            print("valor invalido digite um valor numerico: ")
            return self.getLimite(msg)

    def getExpressao(self):
        try:
            print("utilize a sintaxe correta: Adição(+), Subtração(-), Multiplicação(*), Divisão ( /), Potenciação (**) ou ( ^ ) e Raiz quadrada(sqrt)")
            expressaoEntrada = input("Digite uma funcao Ex: 2*x+3*y**2 ou x**2*sen(2y): ")
            
            expressao = sympy.sympify(expressaoEntrada)
            return expressao 
        except:
            print("formato invalido utilize a sintaxe correta Adição(+) Subtração(-) Multiplicação(*) Divisão ( /) Potenciação (**) ou ( ^ ) Raiz quadrada(sqrt) ")
            return self.getExpressao()

    def intgralDupla(self, limiteInferiorX, limiteSupX, limiteInferiorY, limiteSupY, expressao):
        fatorDemultiplicacao = 1 
        if(limiteInferiorX == -limiteSupX):
            limiteInferiorX = 0
            fatorDemultiplicacao *= 2
        if(limiteInferiorY == -limiteSupY):
            limiteInferiorY = 0
            fatorDemultiplicacao *= 2

        divisoesNoEixoX = self.divisoesNoEixoX
        divisoesNoEixoy = self.divisoesNoEixoy
        x, y = sympy.symbols('x y')  

        func = sympy.lambdify((x, y), expressao)
        dx = (limiteSupX - limiteInferiorX) / divisoesNoEixoX
        dy = (limiteSupY - limiteInferiorY) / divisoesNoEixoy
        xi = limiteInferiorX 
        yj = limiteInferiorY 
        resultado = 0
        for i in range(divisoesNoEixoX):
            for j in range(divisoesNoEixoy):
                resultado += func(xi, yj)*dx*dy
                yj += dy 
            xi += dx 
            yj = limiteInferiorY 
            
        return resultado * fatorDemultiplicacao
