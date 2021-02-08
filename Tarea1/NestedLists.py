def nested_lists(n):
    lista = []
    valores = []
    maximo = 0
    minimo = 0
    nombres = []
    valores_menores = []
    contador_notas = 0
    
    for _ in range(n):
        lista_extra = []
        name = input()
        score = float(input())        
        lista_extra.append(name)
        lista_extra.append(score)
        lista.append(lista_extra)
    
    for i in lista:
        if not i[1] in valores:
            valores.append(i[1])
            contador_notas += 1

    if contador_notas == 2:
        for x in lista:
            if x[1] == max(valores):
                if not x[0] in nombres:
                    nombres.append(x[0])
        nombres.sort()
        valores.sort()
        
        for j in nombres:
            print(j)
    else:

        maximo = max(valores)
        minimo = min(valores)
        
        for v in valores:
            if v > minimo and v < maximo:
                valores_menores.append(v)
        
        
        minimo_valor = min(valores_menores)
        
        for x in lista:
            if x[1] == minimo_valor:
                if not x[0] in nombres:
                    nombres.append(x[0])
        nombres.sort()
        valores.sort()
        
        for j in nombres:
            print(j)

n = int(input("Ingrese cantidad de estudiantes: "))
nested_lists(n)