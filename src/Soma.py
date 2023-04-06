# biblioteca utilizada para transformar a entrada em uma expressão matematica.
import sympy

class Soma:

    def __init__(self, divisoesNoEixoX=100, divisoesNoEixoy=100):
        self.divisoesNoEixoX = divisoesNoEixoX
        self.divisoesNoEixoy = divisoesNoEixoy

    def getLimite(self,msg):
        try:
            limiteInfX = int(input(msg))
            return limiteInfX
        except:
            print("valor invalido digite um valor numerico: ")
            return self.getLimite(msg)

    def getExpressao(self):
        try:
            print("utilize a sintaxe correta: Adição(+), Subtração(-), Multiplicação(*), Divisão ( /), Potenciação (**) ou ( ^ ) e Raiz quadrada(sqrt)")
            expressaoEntrada = input("Digite uma funcao Ex: 2*x + 3*y**2: ")
            # transforma a string em uma expressao
            expressao = sympy.sympify(expressaoEntrada)
            return expressao 
        except:
            print("formato invalido utilize a sintaxe correta Adição(+) Subtração(-) Multiplicação(*) Divisão ( /) Potenciação (**) ou ( ^ ) Raiz quadrada(sqrt) ")
            return self.getExpressao()

    def intgralDupla(self, limiteInferiorX, limiteSupX, limiteInferiorY, limiteSupY, expressao):
        fatorDemultiplicacao = 1 #para integrais com intervalos simetricos podemos simplificar as contas integrando de 0 ate o intervalo superior e multiplicando seu resultado por 2
        if(limiteInferiorX == -limiteSupX):
            limiteInferiorX = 0
            fatorDemultiplicacao *= 2
        if(limiteInferiorY == -limiteSupY):
            limiteInferiorY = 0
            fatorDemultiplicacao *= 2

        divisoesNoEixoX = self.divisoesNoEixoX
        divisoesNoEixoy = self.divisoesNoEixoy
        x, y = sympy.symbols('x y')  # criando simbolos para as variaveis
        # cria a funcao com x y e a expressao
        func = sympy.lambdify((x, y), expressao)
        dx = (limiteSupX - limiteInferiorX) / divisoesNoEixoX
        dy = (limiteSupY - limiteInferiorY) / divisoesNoEixoy
        xi = limiteInferiorX # começa com o valor da base
        yj = limiteInferiorY # começa com o valor da base
        resultado = 0
        for i in range(divisoesNoEixoX):
            for j in range(divisoesNoEixoy):
                resultado += func(xi, yj)*dx*dy
                yj += dy #caminha para cima
            xi += dx #caminha para direira
            yj = limiteInferiorY #volta para base
            
        return resultado * fatorDemultiplicacao
