import this

def coletar():
    print("Informe um número")
    this.num = float(input())

def mostrar():
    coletar()
    for i in range(this.num):
        print((i,this.num))
