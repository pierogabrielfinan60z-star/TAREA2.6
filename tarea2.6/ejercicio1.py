#fecha:29-6-26
#autor:piero garcia
#tema: Lista de calificaciones
#Crea una función que reciba una lista de calificaciones. Usa un bucle para revisar cada nota:
# si la nota es menor a 5, súmale un punto de "asistencia".
# Si por error se incluye una nota superior a 10, la nota debe quedar en 10. 
# La lista original debe quedar modificada.
def lista_de_calificaciones(calificaciones):  #aqui le puse el nombre el cual va a llevar la funcion
    for i in range(len(calificaciones)):                       #aqui puse le bucle que pide la tarea para revisar cada nota     
        if calificaciones[i] > 10:
            calificaciones[i] = 10             #aqui limite hasta 10 la nota ya que hasta ahi pide la tarea
        elif calificaciones[i]< 5:
            calificaciones[i]= calificaciones[i] + 1    #qui modificamos la orignal 

#3 llamdas 
notas =[3, 7, 11, 2, 5]
lista_de_calificaciones(notas)
print(notas)
notas =[4, 6, 60, 1, 5]
lista_de_calificaciones(notas)
print(notas)
notas =[5, 1, 8, 2, 5,4]
lista_de_calificaciones(notas)
print(notas)