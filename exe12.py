import this
def lerConta():
    print("Qual número da sua conta? :")
    this.numConta = int(input())

    print("Qual saldo da sua conta? :")
    this.saldoConta = float(input())

    print("Qual débito da sua conta? :")
    this.debitoConta = int(input())

    print("Qual crédito da sua conta? :")
    this.creditoConta = int(input())

def calcularConta():
    lerConta()
    saltoAtual = (this.saldoConta - this.debitoConta) + this.creditoConta

    if saltoAtual >= 0:
        print("Saldo Positivo " + str(saltoAtual))
    else:print("Saldo Negativo")