#Hans Ernst Westphal Menéndez
#28/9/2023
#Uso de ciclos de For y While

x = ""
while x != 7: 
    print("1. rango de 1 a 25 incrementa en 1, FOR")
    print("2. rango de 1 a 25 incrementa en 1, WHILE")
    print("3. rango de 5 a 50 incrementado en 5, FOR")
    print("4. rango de 5 a 50 incrementado en 5, WHILE")
    print("5. rango de 20 a 0 decrementando en 2, FOR ")
    print("6. rango de 20 a 0 decrementando en 2, WHILE")
    print("7. salir")

    x = int(input("Ingrese una opción"))
    if x == 1:
        for i in range(1, 26):
            print(i,end=",")
    elif x == 2: 
        i = 1
        while i <= 25:
            print(i, end=",")
            i+=1
    elif x == 3:
        for i in range(5, 51, 5):
            print(i, end=",")
    elif x == 4: 
        i = 5 
        while i <= 50:
            print(i, end=",")
            i += 5
    elif x == 5:
        for i in range(21, 0, -2):
            print(i, end=",")
    elif x == 6: 
        i = 20
        while i >= 0: 
            print(i, end=",")
            i-=2
    else: 
        print("Espero haber sido de ayuda")