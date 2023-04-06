from Soma import Soma

soma = Soma()

expressao = soma.getExpressao()
limiteInfX = soma.getLimite('Digite um limite inferior para X: ')
limiteSupX = soma.getLimite('Digite um limite Superior para X: ')
limiteInfY = soma.getLimite('Digite um limite inferior para Y: ')
limiteSupY = soma.getLimite('Digite um limite Superior para Y: ')

soma.intgralDupla(limiteInfX, limiteSupX, limiteInfY, limiteSupY, expressao)