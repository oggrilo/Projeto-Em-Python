import exe01
import exe02
import this

import exe03
import exe04
import exe05
import exe06
import exe07
import exe08
import exe09
import exe10
import exe11
import exe12
import exe13

this.opcao = 0 #Criar a variavel global
def mostrarMenu():
    print("Escolha uma das Opções Abaixo!\n " +
          "\n1. Exercicio 01" +
          "\n2. Exercicio 02" +
          "\n3. Exercicio 03" +
          "\n4. Exercicio 04" +
          "\n5. Exercicio 05" +
          "\n6. Exercicio 06" +
          "\n7. Exercicio 07" +
          "\n8. Exercicio 08" +
          "\n9. Exercicio 09" +
          "\n10. Exercicio 10" +
          "\n11. Exercicio 11" +
          "\n12. Exercicio 12" +
          "\n13. Exercicio 13" +
          "\n14. Exercicio 14" +
          "\n15. Sair")
    this.opcao = int(input()) #Comando para coletar oq o usuario irá digitar




def operacao():
    #Mostrar o Menu em tela
    while this.opcao != 15:
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
            print(exe07.exe07())
        elif this.opcao == 8:
            print(exe08.exe08())
        elif this.opcao == 9:
            print(exe09.guardarValor())
        elif this.opcao == 10:
            print(exe10.bubbleSort())
        elif this.opcao == 11:
            print(exe11.calcular())
        elif this.opcao == 12:
            print(exe12.calcularConta())
        elif this.opcao == 13:
            print(exe13.mostrar())
        elif this.opcao == 14:
            print(exe14.mostrar())

        elif this.opcao == 15:## opção para fechar
            print("Obrigado!")
        else: print("Opção Escolhida Inválida, tente outro número!")
