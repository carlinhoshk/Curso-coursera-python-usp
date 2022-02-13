
def remove_repetidos(lista):
    lista= sorted(list(set(lista)))
    print(lista)
    return lista


lista = [3,4,1,1,4]
remove_repetidos(lista)
