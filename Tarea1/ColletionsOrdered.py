from collections import OrderedDict

ordi = OrderedDict()
for _ in range(int(input())):
    articulo, espacio, precio = input().rpartition(' ')
    ordi[articulo] = ordi.get(articulo, 0) + int(precio)
for articulo, precio in ordi.items():
    print(articulo, precio)