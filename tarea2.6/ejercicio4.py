#fecha:29-6-26
#autor:piero garcia
#tema: Numeros
#Crea una función que reciba una cantidad indeterminada de números. Recórrelos con un bucle y calcula la suma únicamente de los números que sean pares.

def sumar_pares(*numeros):
    suma = 0 
    # puse el for para que recorra cada numero enviado
    for n in numeros:
        if n % 2 == 0:
            # para verificar si el numero es par usando el %
            suma = suma + n
    return suma
# 3 llamadas
res = sumar_pares( 1, 2, 3, 4, 5, 6, 7, 8)
print(res)
res = sumar_pares( 5, 2, 8, 7, 1, 4, 2, 8)
print(res)
res = sumar_pares( 9, 2, 6, 1, 22, 35, 65, 5)
print(res)