#fecha:29-6-26
#autor:piero garcia
#tema: cobro gimnasio 

def calcular_mensualidad(tarifa_base, es_estudiante=False):
    descuento = 0
    if es_estudiante== True:
        descuento = tarifa_base * 0.20
        
    total_a_pagar = tarifa_base - descuento 
    return descuento, total_a_pagar

# 3llamadas 
#estudiante:
desc , total = calcular_mensualidad(100, True)
print(f"Descuento: {desc}, Total: {total}")
#estudiante:
desc , total = calcular_mensualidad(80, True)
print(f"Descuento: {desc}, Total: {total}")
#Caso cliente normal:
desc , total = calcular_mensualidad(600)
print(f"Descuento: {desc}, total: {total}")