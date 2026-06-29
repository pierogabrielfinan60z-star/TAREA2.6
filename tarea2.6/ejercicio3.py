#fecha:29-6-26
#autor:piero garcia
#tema: registro de un usuario
#Crea una función que simule el registro de un usuario con los parámetros nombre, rol y nivel_acceso. 
# Usa condicionales para verificar si el rol es "Admin" y el nivel es mayor a 5 para otorgar permisos especiales.
# Invócala cambiando el orden de los argumentos.
def registrar_usuario(nombre, rol, nivel_acceso):
    #condicional para verificar permisos 
    if rol == "admin" and nivel_acceso > 5:
        mensaje = (f"usuario {nombre} registrado con permisos especiales.")
    else:
        mensaje = (f"usuario {nombre} registrado con acceso normales.")
    print(mensaje)
    
# 3 llamadas 
registrar_usuario(nivel_acceso=8, nombre="Ana", rol="Admin")
registrar_usuario(nivel_acceso=8, nombre="Juan", rol="admin")
registrar_usuario(nivel_acceso=2, nombre="Paul", rol="Admin")
