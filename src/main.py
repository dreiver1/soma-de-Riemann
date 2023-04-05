# biblioteca utilizada para transformar a entrada em uma expressão matematica.
import sympy

def getExpressao():
    try:
        print("utilize a sintaxe correta: Adição(+), Subtração(-), Multiplicação(*), Divisão ( /), Potenciação (**) ou ( ^ ) e Raiz quadrada(sqrt)")
        expressaoEntrada = input("Digite uma funcao Ex: 2*x + 3*y**2: ")
        # transforma a string em uma expressao
        expressao = sympy.sympify(expressaoEntrada)
        return expressao 
    except:
        print("formato invalido utilize a sintaxe correta Adição(+) Subtração(-) Multiplicação(*) Divisão ( /) Potenciação (**) ou ( ^ ) Raiz quadrada(sqrt) ")
        return getExpressao()
def intgralDupla(limiteInferiorX, limiteSupX, limiteInferiorY, limiteSupY, expressao):
    fatorDemultiplicacao = 1 #para integrais com intervalos simetricos podemos simplificar as contas integrando de 0 ate o intervalo superior e multiplicando seu resultado por 2
    if(limiteInferiorX == -limiteSupX):
        limiteInferiorX = 0
        fatorDemultiplicacao *= 2
    if(limiteInferiorY == -limiteSupY):
        limiteInferiorY = 0
        fatorDemultiplicacao *= 2

    m = 100
    n = 100
    x, y = sympy.symbols('x y')  # criando simbolos para as variaveis
    # cria a funcao com x y e a expressao
    func = sympy.lambdify((x, y), expressao)
    dx = (limiteSupX - limiteInfX) / m
    dy = (limiteSupY - limiteInfY) / n
    xi = limiteInfX # começa com o valor da base
    yj = limiteInfY # começa com o valor da base
    resultado = 0
    for i in range(m):
        for j in range(n):
            resultado += func(xi, yj)*dx*dy
            yj += dy #caminha para cima
        xi += dx #caminha para direira
        yj = limiteInfY #volta para base
        
    return resultado * fatorDemultiplicacao
expressao = getExpressao() #Cria uma expressão a partir da entrada do terminal
limiteInfX = int(input('Digite um limite inferior para X: '))
limiteSupX = int(input('Digite um limite Superior para X: '))
limiteInfY = int(input('Digite um limite inferior para Y: '))
limiteSupY = int(input('Digite um limite Superior para Y: '))
print(intgralDupla(limiteInfX, limiteSupX, limiteInfY, limiteSupY, expressao))