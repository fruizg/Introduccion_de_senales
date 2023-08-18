#Algoritmo

# 1. inicializar variables 
# 2. Pedir a usuario (médico) que ingrese los siguientes datos: edad del paciente, presión arteria, frecuencia
#  Respiratoria, nivel re úrea sérica y un booleano sobre si el paciente está desorientado
# 3. realizar un if para verificar cada condición del CURB-65: si el if se cumple, sumar al contador, de lo contrario,
# no hacerlo.
# 4. realizar otro if que evalue el contador final, que corresponde al puntaje e imprimir el mensaje correspondiente
# al puntaje obtenido por el paciente

from xmlrpc.client import boolean

from sqlalchemy import true


contador = 0
edad =  int (input("Ingrese la edad del paciente: "))
PAS = int(input("Ingrese la presión sistólica del paciente : "))
PAD = int(input("Ingrese la presión diástolica del paciente : "))
uremia = int(input("INgrese el nivel de úrea sérica del paciente en mmol/L: "))
rpm = int(input("Ingrese la frecuencia respiratoria del paciente en respiraciones por minuto: "))
confusion = boolean(input("Indique si el paciente presenta algún tipo de desotientación con la sentencia TRUE o FALSE: "))


if confusion == True:
    contador += 1 
if uremia > 7:
    contador += 1
if rpm >= 30:
    contador +=1
if PAS < 90 or PAD <= 65:
    contador +=1
if edad >= 65:
    contador +=1

if contador <= 1: 
    print(f'Riesgo de muerte bajo, manejo ambulatorio')
if contador  == 2: 
    print(f'Riesgo de muerte intermedio, manejo intrahospitalario')
if contador == 3: 
    print(f'Riesgo de muerte elevado, manejo intrahospitalario, considerar UCI')
if contador >= 4: 
    print(f'Riesgo de muerte elevado, considerar admisión en UCI')
