#Hans Ernst Westphal Menéndez 1135223
#26/09/23
#Calculos de facotiral y sucesión de Fibolacci
y = int(input("Ingrese un número para las operaciones"))
x = ""
while x != 3: 
    print ("1. factorial ")
    print("2. secuencia de fibolacci")
    print("3. salida")
    x = int(input("Ingrese una opción"))
    if x == 1: 
        print("Respuesta", y,"! es" )
        for y in range (1, y+1):
            print(y, "*")
    elif x== 2: 
        print("La respuesta de fibolacci en ", y, "es")
        for y in range(0, y+1):
         anterior = y
         nuevo = anterior + y
         print(nuevo, ",")
    else:
        print("Espero haber sido de ayuda") 

        

