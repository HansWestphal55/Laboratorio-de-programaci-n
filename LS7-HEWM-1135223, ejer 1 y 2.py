#Hans Ernst Westphal 1135223
#19/9/23
y = int(input("ingresa un valor entero y positivo"))
x = int(input("ingresa un valor entero y positivo"))
opcion = ""
while opcion != "8":
    print("Operaciones aritmeticas")
    print("1. suma")
    print("2. resta")
    print("3. multiplicacion")
    print("4. division")
    print("5. modulo")
    print("6. exponenciacion")
    print("7. cocinete")
    print("8. salir")

    opcion = input("ingresar un numero de 1 a 8")

    if opcion == "8":
        print("Espero haber sido de ayuda")
    elif opcion == "1":
        resultado = x + y 
        print("numero 1",x, "numero 2", y, "resultado",resultado)
    elif opcion == "2":
        resultado = x - y 
        print("numero 1",x, "numero 2", y, "resultado",resultado)
    elif opcion == "3":
        resultado = x * y
        print("numero 1",x, "numero 2", y, "resultado",resultado)
    elif opcion == "4":
        resultado = x/y 
        print("numero 1",x, "numero 2", y, "resultado",resultado)
    elif opcion =="5":
        resultado = x % y
        print("numero 1",x, "numero 2", y, "resultado",resultado)
    elif opcion == "6":
        resultado = x**y 
        print("numero 1",x, "numero 2", y, "resultado",resultado)
    elif opcion =="7":
        resultado = x // y
        print("numero 1",x, "numero 2", y, "resultado",resultado)

