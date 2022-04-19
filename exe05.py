import this

def coletar():
    print("Informe o total de Eleitores desse município: ")
    this.eleitores = int(input)

    print("Informe o total de Votos Brancos desse município: ")
    this.brancos = int(input)

    print("Informe o total de Votos Nulos desse município: ")
    this.nulos = int(input)

    print("Informe o total de Votos Válidos desse município: ")
    this.validos = int(input)
def calcular():
    this.validos =  this.eleitores - (this.brancos + this.nulos) /100
    this.totalBrancos = this.branco * this.eleitores/100
    this.totalNulos = this.nulos * this.eleitores / 100

def mostrar():
    coletar()
    calcular()
    print("A Porcentagem do total dos votos brancos é: " + this.totalBrancos +
    "\n A Porcentagem do total de votos nulos é: " + this.totalNulos +
    "\n A Porcentagem do total de votos valídos é: " + this.validos )




