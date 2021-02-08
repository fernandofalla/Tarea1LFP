from itertools import permutations

def itertool_permutation(string, numero):
    
    lista = []

    for i in string:
        lista.append(i)

    print(list(permutations(lista,2)))

cadena = input("Ingrese palabra y tamaño: ")
lista_aux = cadena.split(" ")
itertool_permutation(lista_aux[0],lista_aux[1])