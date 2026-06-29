#fecha:29-6-26
#autor:piero garcia
#tema: lista de numeros
#Diseña una función que reciba una lista de números. Debe recorrerla para c
def contar_numeros(lista):
    positivos = 0
    negativos = 0
    ceros = 0
    for n in lista:
        if n > 0:
            positivos = positivos + 1
        elif n < 0:
            negativos = negativos + 1
        else:
            ceros = ceros + 1
    return positivos, negativos, ceros

#3 llamadas
numeros= [10, -5, 0, 3, -1, 0]
p, n, c = contar_numeros(numeros)
print(f"Positivos: {p}, Negativos: {n}, Ceros: {c}")