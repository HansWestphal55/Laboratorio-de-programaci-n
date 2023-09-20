#Hans Ernst Westphal 1135223
#19/9/23
import math
a = int(input("ingresa la variable a"))
b = int(input("ingresa la variable b"))
c = int(input("ingresa la variable c"))
opcion = ""
while opcion != "6":
    print("1. a * b + c ")
    print("2. a * (b+c)")
    print("3. a/(b*c)")
    print("4. (3a+2b)/c^2")
    print("5. calculadora cuadratica")
    print("6. Salida")

    opcion = input("ingresar un numero de 1 a 6")

    if opcion == "6":
         print("Espero haber sido de ayuda")
    elif opcion == "1":
        resultado = a * b + c
        print("numero 1",a, "numero 2", b,"numero 3", c, "resultado",resultado)
    elif opcion == "2":
        resultado = a * (b+c)
        print("numero 1",a, "numero 2", b,"numero 3", c, "resultado",resultado)
    elif opcion == "3":
        if b == "0":
            print("No se puede calcular con un divisor igual a 0")
            continue
        resultado = a/(b*c)
        print("numero 1",a, "numero 2", b,"numero 3", c, "resultado",resultado)
    elif opcion == "4":
        resultado = (3* a + 2 * b)/(c**2)
        print("numero 1",a, "numero 2", b,"numero 3", c, "resultado",resultado)
    elif opcion == "5":
        raiz = b**2 -4*a*c
        if a== "0" or raiz < 0:
            print(" No se puede calcular con los valores ingresados")
        continue
        x1 = (-1*b +math.sqrt(raiz))/(2 * a)
        x2 = (-1*b -math.sqrt(raiz))/(2 * a)
        print("x1 es igual a", x1, "y x2 es igual a", x2)