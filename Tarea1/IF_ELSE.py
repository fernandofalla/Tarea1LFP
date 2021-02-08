def if_else(n):

    if not n % 2 == 0:
        print("")
        print("Weird")
        print("")
    elif n >= 2 and n <= 5:
        print("")
        print("Not Weird")
        print("")
    elif n >= 6 and n <= 20:
        print("")
        print("Weird")
        print("")
    elif n > 20:
        print("")
        print("Not Weird")
        print("")

numero = int(input("Ingrese numero: "))
if_else(numero)