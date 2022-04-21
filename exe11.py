import this

def coletar():
    print("Digite o seu salário fixo: ")
    this.salario = float(input())

    print("Agora digite o valor das suas vendas: ")
    this.vendas = float(input())

def calcular():
    coletar()
    if this.vendas <= 1500:
        this.adicional = (this.vendas * 3)/100
    else :
        this.adicional = (this.vendas * 5)/100
    print("O seu salário atual é :" + str(this.adicional + this.salario))