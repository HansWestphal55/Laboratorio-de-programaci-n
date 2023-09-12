#Hans Westphal 1135223
#12/9/23
#proceso:
numero = input(" Ingrese un número de día: ")
numero = int(numero)
DIA=""
if numero<0 or numero>7:
    DIA="Ingresar unicamente un numero entre 1 y 7"
elif numero==1:
    print("lunes")
elif numero==2:
    print("martes")
elif numero==3:
    print("miercoles")
elif numero==4:
    print("jueves")
elif numero==5:
    print("viernes")
elif numero==6:
    print("sabado")
elif numero==7: 
    print("domingo")
else:
    print("No valido")
    


