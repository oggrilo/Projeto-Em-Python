import this

def coletarSalario():
    print("Informe seu salário mensal: ")
    this.salarioMensal = (float(input()))

    print("Informe o percentual de ajuste: ")
    this.percentualAjuste = int(input())

def calcularSalario():
    this.novoSalario = this.salarioMensal * (this.percentualAjuste/100)
def mostrarNovoSalario():
    coletarSalario()
    calcularSalario()
    print("O seu novo salário é: " + str(this.novoSalario))