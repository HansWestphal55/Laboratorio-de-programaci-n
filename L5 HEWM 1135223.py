#Hans Ernst Westphal 1135223
#12/9/23
#Al ingresar un valor determinar si es positivo, negativo o cero
#entrada
numero = int(input("Ingresar un número"))
#proceso
if numero == 0:
    resultado = 0 
    print("El resultado es igual a", resultado, "por lo tanto no es positivo ni negativo.")
elif numero > 0: 
    resultado = numero 
    print("El numero", resultado, "es positivo.")
elif numero < 0: 
    resultado = numero
    print("El número", resultado, "es negativo.")
    #salida
else:
    print("ingrese un número")