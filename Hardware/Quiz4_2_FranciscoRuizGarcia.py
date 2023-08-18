# 1. Pedir segundos al usuario
# 2. definir variable auxiliar que guarde el valor original de los segundos ingresados por el usuario, ya que se harán operaciones a este
# 3. definir el valor de los días, para lo cual traeremos el valor entero del resultado de la división 
# de los segundos ingresados por el usuario y 86400, valor que corresponde a los segundos que hay en un día
# 4. a la variable de segundos usuarios, le hacemos una modificación para redefinirla como el residuo de el valor de segundos usuario y 86400
# 5. definimos la hora como el valor de la división entera de segundos ingresados por el usuario (con el nuevo valor asignado
# para estos) y 3600, que corresponde a los segundos que hay en una hora
# 6. volvemos a redefinir los segundos ingresados por el usuario como el residuo de la división del valor de segundos usuarios y 3600
# 7. definimos los minutos como el resultado de la división entera nuevo valor de segundos usuarios y 60, que 
# es la cantidad de segundos que hay en un minuto
# 8. por último, los segundos los definimos como el residuo de la división de segundos ingresados por el usuario y 60
# Imprimimos el resultado

segundos_usuario = int(input("Ingrese los segundos: "))
aux = segundos_usuario
dias = segundos_usuario // (86400)
segundos_usuario = segundos_usuario % (86400)
hora = segundos_usuario // (3600)
segundos_usuario = segundos_usuario % (3600)
minuto = segundos_usuario // 60
segundos = segundos_usuario % 60


print(f"los segundos {aux} corresponde a {dias}:{hora}:{minuto}:{segundos}")