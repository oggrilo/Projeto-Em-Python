import this

this.num = 0
this.contador = 0
this.resultado = 0

def coletar():
    print("Informe um número")
    this.num = float(input())

def mostrar():
    coletar()
    for i in range(this.num):
        print((i,this.num))
