import this
this.base = 0
this.altura = 0


def coletarBaseAltura():
    print("Informe a base do retângulo: ")
    this.base = float(input())

    print("Agora informe a altura do retãngulo: ")
    this.altura = float(input())


    resultado=this.base * this.altura
    print("A área do retângulo é: " + str(float(resultado)))