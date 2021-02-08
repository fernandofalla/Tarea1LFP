def Capitalize_Espacio(s):
    cadena = s.split(" ")
    cadena_completa = ""
    for i in cadena:
        cadena_completa += i.capitalize()
        cadena_completa += " "

    print(cadena_completa)

s = input("Ingrese la cadena: ")
Capitalize_Espacio(s)