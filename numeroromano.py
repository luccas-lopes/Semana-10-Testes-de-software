def converte(numeroEmRomano):
    tabela = {}
    tabela['I'] = 1
    tabela['V'] = 5
    tabela['X'] = 10
    tabela['L'] = 50
    tabela['C'] = 100
    tabela['D'] = 500
    tabela['M'] = 10000

    acumulador = 0
    ultimovizinhodireita = 0
  
    for i in reversed(range(len(numeroEmRomano))):
        # XXIV vira VIXX
        atual = 0
        numCorrente = numeroEmRomano[i] # I
        if (numCorrente in tabela):
            atual = tabela[numCorrente] # atual = 1

        if (atual < ultimovizinhodireita):
            acumulador -= atual
        else:
          acumulador += atual # acumulador = 0 + 5
          
        ultimovizinhodireita = atual # ultimovizinhodireita = 10

    return acumulador