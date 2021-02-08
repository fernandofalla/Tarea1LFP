def finding_the_percentage(n):
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    lista = student_marks[query_name]

    suma = 0
    contador = 0
    for i in lista:
        suma += i
        contador += 1

    resultado = suma/contador

    print(f"{resultado:.2f}")

n = int(input("Ingrese cantidad de estudiantes: "))
finding_the_percentage(n)