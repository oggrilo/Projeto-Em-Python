def idade():
    print("Informe o dia do seu aniversário: ")
    dia = int(input())

    print("Informe o mês do seu aniversário(em formato númerico): ")
    mes = int(input())

    print("Informe o ano do seu aniversário: ")
    ano = int(input())


    total_de_dias = ano * 365 + mes * 30 + dia
    print('O valor do total de dias: ' + repr(total_de_dias))