import exe01
import exe02
import this

import exe03
import exe04
import exe05
import exe06

this.opcao = 0 #Criar a variavel global
def mostrarMenu():
    print("Escolha uma das Opções Abaixo!\n " +
          "\n1. Exercicio 01" +
          "\n2. Exercicio 02" +
          "\n3. Exercicio 03" +
          "\n4. Exercicio 04" +
          "\n5. Exercicio 05" +
          "\n6. Exercicio 06" +
          "\n5. Sair")
    this.opcao = int(input()) #Comando para coletar oq o usuario irá digitar




def operacao():
    #Mostrar o Menu em tela
    while this.opcao != 3:
        mostrarMenu()
        #Realizar as operções
        if this.opcao == 1:
            print(exe01.trocar())
        elif this.opcao == 2:
            print(exe02.coletar())
        elif this.opcao == 3:
            print(exe03.coletarBaseAltura())
        elif this.opcao == 4:
            print(exe04.idade())
        elif this.opcao == 5:
            print(exe05.mostrar())
        elif this.opcao == 6:
            print(exe06.mostrarNovoSalario())

        elif this.opcao == 7:
            print("Obrigado!")
        else: print("Opção Escolhida Inválida, tente outro número!")
