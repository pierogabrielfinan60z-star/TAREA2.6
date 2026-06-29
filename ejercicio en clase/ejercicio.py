#fecha:29-6-26
#autor:piero garcia
#tema: ejercicios en clases



def potencia(base, exponente):
    return base ** exponente
base = 3
exponente = 4
res = potencia(base, exponente)
print(f"El resultado de {base} elevado a la {exponente} es {res}")

# Prueba de función dentro de otra
print(f"El resultado de 5 elevado al cubo es {potencia(5, 3)}")

# Prueba de funciones anidadas
res = potencia(potencia(2, 5), 2)
print(f"El resultado de potencia(potencia(2,5),2) es {res}")

# Parámetros nombrados
res = potencia(exponente=4, base=3)
print(f"Resultado con parámetros nombrados: {res}")

#Modificación de lista (paso por referencia) 

def modificaListaEnteros(lista):
    print("lista original ", lista)
    lista[0] = 22
    lista.append(10)
    print("nueva lista ", lista)

# Parámetros opcionales 
def saludar(nombre="Invitado", total=5):
    cont = 0
    while cont < total:
        print(f"Hola {nombre}. Bienvenido!!!")
        cont = cont + 1

#  Contador de cifras v1 y v2
def cuentaCifrasv1(num):
    # Basado en la llamada simple que aparece en tus fotos
    return len(str(abs(num)))

def cuentaCifrasv2(num):
    num = abs(num) # Aseguramos que sea positivo
    total = 0
    n = 1
    while n <= num:
        n = n * 10
        total = total + 1
    return total

# Prueba de lista
lista = [1, 2, 3, 4]
modificaListaEnteros(lista)
print("La lista después de la llamada a la función ", lista)

# Prueba de saludo
saludar()
print() # Salto de línea
saludar("Ana")

# Pruebas del contador de cifras
num = -34
print(f"El número de cifras de {num} es {cuentaCifrasv1(num)}")
num = 134
print(f"El número de cifras de {num} es {cuentaCifrasv2(num)}")
print(f"El número de cifras de 1000 es {cuentaCifrasv2(1000)}")
print(f"El número de cifras de 1234567890 es {cuentaCifrasv2(1234567890)}")