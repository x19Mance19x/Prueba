def ordenar(palabra):
    lista = list(set(palabra))
    lista.sort()
    return lista

ordenado = ordenar("entretenido")

print(ordenado)