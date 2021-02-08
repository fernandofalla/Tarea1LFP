from collections import namedtuple

n = int(input())
campos = input().split()

total_marks = 0
for _ in range(n):
    estudiantes = namedtuple('estudiante', campos)
    MARKS, CLASS, NAME, ID = input().split()
    estudiante = estudiantes(MARKS, CLASS, NAME, ID)
    total_marks += int(estudiante.MARKS)
print('{:.2f}'.format(total_marks / n))