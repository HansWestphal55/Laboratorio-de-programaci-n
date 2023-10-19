#Hans Westphal 1135223
#19/10/23
#Solicitar al usuario que ingrese una palabra 
palabra = input("Por favor, ingresa una palabra: ")
print("Las primeras tres letras de la palabra ingresada son:")
for i in range(3):
    if i < len(palabra):
        print(palabra[i])

Nuevacadena = palabra[:3]
print("La nueva subcadena es:", Nuevacadena)
Texto2 = input("Ahora, ingresa un nuevo texto: ")
Texto2 = Texto2.replace("O", "x")
print("El nuevo texto que se formó es:", Texto2)

#Investigación
#Python ofrece diferentes forma de crear cadenas, una de ellas es "len" que da la opción de tener la longitud de una lista.
#La segunda es "str.split()" que permite agregar cosas en cadena en los print de tipo str. 