import this

this.num = 0
this.contador = 0
this.resultado = 0
def valor():
    print('Informe um número')
    this.num = float(input())


def mostrar():
    valor()
    for i in range(11):
        print('{} * {} = {}'.format(this.num,i,this.num*i))
