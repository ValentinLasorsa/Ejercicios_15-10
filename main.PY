import os
#EJ 1
print("Ejercicio 1")
numeros=[]
suma=0
sumaPar=0
sumaImpar=0
for k in range(1,16):
    num=int(input(f"Ingrese el {k} número "))
    numeros.append(num)
    suma=suma+num
    if k %2==0:
        sumaPar=sumaPar+num
    else:
        sumaImpar=sumaImpar+num
print("La suma total es:"+str(suma)+" La suma de los números en posiciones pares es:"+str(sumaPar)+" La suma de los números en posiciones impares es:"+str(sumaImpar))
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')

#EJ 2
print("Ejercicio 2")
numeros=[]
for k in range(1,21):
    num=int(input(f"Ingrese el {k} número "))
    numeros.append(num)
producto=numeros[0]*numeros[19]
print("El valor de la cuarta posición es:",numeros[3],"El producto entre el primer y último componente de la lista es:",producto)
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')

#EJ 3
print("Ejercicio 3")
numeros=[]
suma=0
for k in range(1,21):
    num=int(input(f"Ingrese el {k} número "))
    numeros.append(num)
    suma=suma+num
promedio=suma/20
mayorProm=0
for num in numeros:
    if num > promedio:
        mayorProm+=1
print("El promedio fue de:",promedio, "y la cantidad de número mayores al promedio es de:",mayorProm)
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')

#EJ 1 (Luego de las explicaciones)
print("Ejercicio 1")
numeros=[]
for k in range(1,21):
    num=int(input(f"Ingrese el {k} número "))
    numeros.append(num)
mayor=0
for num in numeros:
    if num>mayor:
        mayor=num
print("El mayor número es",mayor)
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')

#EJ 2
print("Ejercicio 2")
numeros=[]
mayor=0
menor=999
for k in range(1,16):
    num=int(input(f"Ingrese el {k} número "))
    numeros.append(num)
for num in numeros:
    if num>mayor:
        mayor=num
    elif num<menor:
        menor=num
producto=menor*mayor
print("El menor valor fue:",menor,"y el mayor fue:",mayor,"por lo tanto, el producto entre el menor valor y el mayor valor es:",producto)
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')

#EJ 3
print("Ejercicio 3")
lista=[]
listaMenoresPromedio=[]
suma=0
prom=0
for k in range(1,21):
    num=int(input(f"Ingrese el {k} número "))
    lista.append(num)
    suma=suma+num
prom=suma/20
for h in lista:
    if h <prom:
        listaMenoresPromedio.append(h)
print("El promedio fue:",prom)
print("La lista de números menores al promedio quedó así:",listaMenoresPromedio)
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')

#EJ 4
print("Ejercicio 4")
numeros = []
for i in range(1,21):
    num=int(input(f"Ingrese el {i} número "))
    numeros.append(num)
numMin=999
contNumMin=0
for h in numeros:
    if h <numMin:
        numMin=h
for y in numeros:
    if y==numMin:
        contNumMin+=1
print("El valor mínimo es",numMin,"y apareció en la lista",contNumMin,"veces")
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')

#EJ 5
print("Ejercicio 5")
lista = []
for i in range(20):
    valor = float(input(f"Ingrese el valor {i + 1}: "))
    lista.append(valor)
posiciones_nulas = []
for i in range(len(lista)):
    if lista[i] == 0:
        posiciones_nulas.append(i)
if posiciones_nulas:
    print(f"Las posiciones de las componentes nulas son: {posiciones_nulas}")
else:
    print("No hay componentes nulas en la lista.")
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')