def print_function(n):
    cadena = ""
    for i in range(n):
        cadena += str(i+1)
    return cadena

n = int(input("Ingrese numero: "))
print(print_function(n))