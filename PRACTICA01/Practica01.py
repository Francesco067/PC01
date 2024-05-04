#problema 01
nombre = input("Dime tu nombre: ")
print(f"¡HOLA {nombre}!")
#problema 02
monto=float(input("Cuanto fue su consumo?: "))
propina = float(input("Desea agregar servicio? Generalmente es el 15%: "))
print(f"El total a pagar es {monto+(monto*propina/100)}")
#problema 03
muñecas = int (input("cuantas muñecas saldran en este pedido?: "))
payasos= int (input("Cuantos payasos saldran en este pedido?: "))
print(f"El peso total de su pedido es :{muñecas*75+payasos*112} ")
#problema 04
N=int(input("Dame un Numero entero positivo: "))
print(f"La suma total de los N numeros enteros es : {N*(N+1)/2}")
#problema 05
shows=float(input("Cuantos shows musicales vio este año?: "))
mayormenor=shows>3
print(f"El usuario vio mas de tres shows? : {mayormenor}")
#problema 06
edad=int(input("Cual es tu edad : "))
if(edad<4):
    print("el niño  puede entrar gratis")
elif(edad>=4 and edad <=18):
    print("Debe de pagar 5 dolares")
elif(edad>18):
    print("Debe de pagar 10 dolares")
#problema 07
numero1=int(input("Dame un numero : "))
numero2=int(input("Dame otro numero : "))
menu=int(input(" Que desea realizar?: \n"
               " Marque 1 si desea una suma de los numeros\n"
               " Marque 2 si desea una resta de los numeros\n"
               " Marque 3 si desea una multiplicacion de los numeros?\n"
               ))
if(menu==1):
    print(f"La suma de los numeros {numero1} y {numero2} es : {numero1+numero2}")
elif(menu==2):
    print(f"La resta de los numeros {numero1} y {numero2} es : {numero1-numero2}")
elif(menu==3):
    print(f"La multiplicacion de los numeros {numero1} y {numero2} es : {numero1*numero2}")
else:
    print("Debe de marcar 1 , 2 o 3")

#problema 08
time = input("Ingrese la hora en formato 'HH:MM' (24 horas): ")

hora_minutos = time.split(":")

hora = int(hora_minutos[0])
minutos = int(hora_minutos[1])

if 7 <= hora <= 8:
    print("Es hora de desayunar.")
elif 12 <= hora <= 13:
    print("Es hora de almorzar.")
elif 18 <= hora <= 19:
    print("Es hora de cenar.")

#problema 09

lista = ['Di', 'buen', 'día', 'a', 'papa']


lista= lista[::-1]

print(f"La lista invertida es la siguiente : {lista}")

#problema 10


lista_problema10 = ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']


lista_problema10.pop(5)  
lista_problema10.pop(4)  
lista_problema10.pop(0)  

print(f"Resultado esperado: {lista_problema10}")

#problema 11
lista_original = [1, 1, 2, 3, 4, 4, 5, 1]
lista_procesada = []

for e in lista_original:
    if e not in lista_procesada:
        lista_procesada.append(e)

print(f"Lista original: {lista_original}")
print(f"Lista procesada:  {lista_procesada}")

#problema 12

nombre_archivo = input("Ingrese el nombre del archivo: ")

extension_nombre = nombre_archivo.split(".")

extension=extension_nombre[1]

tipos_mime = {
    'gif': 'image/gif',
    'jpg': 'image/jpeg',
    'jpeg': 'image/jpeg',
    'png': 'image/png',
    'pdf': 'application/pdf',
    'txt': 'text/plain',
    'zip': 'application/zip'
}

tipo_mime = tipos_mime.get(extension, 'application/octet-stream')

print(f"Tipo MIME del archivo {nombre_archivo}: {tipo_mime}")