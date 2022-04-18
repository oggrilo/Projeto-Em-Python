import exe01
import exe02
import this

this.opcao = 0 #Criar a variavel global
def mostrarMenu():
    print("Escolha uma das Opções Abaixo!\n " +
          "\n1. Exercicio 01" +
          "\n2. Exercicio 02" +
          "\n3. Sair")
    this.opcao = int(input()) #Comando para coletar oq o usuario irá digitar

def operacao():
    #Mostrar o Menu em tela
    while this.opcao != 3:
        mostrarMenu()
        #Realizar as operções
        if this.opcao == 1:
            print(exe01.trocar())
        if this.opcao == 2:
            print(exe02.coletar())

        elif this.opcao == 3:
            print("Obrigado!")
        else: print("Opção Escolhida Inválida, tente outro número!")
