def loops(n):
    lista_indices = []
    
    for i in range(n):
        lista_indices.append(i)
    
    lista_cuadrada = []

    for x in lista_indices:
        lista_cuadrada.append(x*x)
    
    for j in lista_cuadrada:
        print(j)

n = int(input("Ingrese cantidad: "))
loops(n)