def lists(n):
    lista = []
    for i in range(n):
        cadena_entrada = input()
        opcion = cadena_entrada.split(" ")
        if opcion[0] == "insert":
            lista.insert(int(opcion[1]),int(opcion[2]))
            cadena_entrada = ""
            opcion = ""
            indice = 0
            valor = 0
        elif opcion[0] == "print":
            print()
            print(lista)
            print()
            cadena_entrada = ""
            opcion = ""
        elif opcion[0] == "remove":
            lista.remove(int(opcion[1]))
            cadena_entrada = ""
            opcion = ""
        elif opcion[0] == "append":
            lista.append(int(opcion[1]))
            cadena_entrada = ""
            opcion = ""
        elif opcion[0] == "sort":
            lista.sort()
            cadena_entrada = ""
            opcion = ""
        elif opcion[0] == "pop":
            lista.pop()
            cadena_entrada = ""
            opcion = ""
        elif opcion[0] == "reverse":
            lista.reverse()
            cadena_entrada = ""
            opcion = ""

n = int(input("Ingrese cantidad de comandos: "))
lists(n)