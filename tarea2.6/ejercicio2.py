#fecha:29-6-26
#autor:piero garcia
#tema: Ticket de compra

#Diseña una función para generar un ticket de compra. Recibe el precio base y, de forma opcional,
# un porcentaje de descuento (por defecto 0). Usa un condicional para aplicar el descuento solo si es mayor a cero.
def comprobante_ticket(precio_base, descuento=0):
    #hago la verificacion si hay descuento o no
    if descuento > 0:
        #hago para ver cuanto hay que restar
        procentaje_descuento = precio_base * (descuento / 100)
        total = precio_base - procentaje_descuento
    else:
        #si no hay descuento , el precio se queda normal 
        total = precio_base
    
    return total 
    
# 3 llamadas 
print(comprobante_ticket(100))
print(comprobante_ticket(100, 20))
print(comprobante_ticket(100, 75))