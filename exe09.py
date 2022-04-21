import this
def coletarMacas():
    print("Quantas maças deseja comprar ?: ")
    this.quantidadeMacas = int(input())

def guardarValor():
    coletarMacas()
    if this.quantidadeMacas >= 12:
        this.valorMacas = this.quantidadeMacas * 1.00
    elif this.quantidadeMacas < 12:
        this.valorMacas = this.quantidadeMacas * 1.30
    print("O valor da sua compra é :" + str(this.valorMacas))
