## 01. Es mayor de edad?

edad = int(input(" Ingresa una edad por favor: "))

if edad >= 18:
  print("Sos mayor de edad")
else:
   print("Sos menor de edad")


## 02. Comprarar dos números


n1 = int(input(" Ingresa un primer número por favor "))
n2 = int(input(" Ingresa un segundo número por favor "))

if n1 > n2:
    print(f'El número: {n1} es mayor a {n2}')

elif n1 < n2:
     print(f'El número: {n2} es menor a {n1}')

elif n1 == n2:
     print(f'Los dos números son iguales: {n1} {n2}')



## 03. Calificación del fernet

ingresa_nivel = int(input(" Ingresa el nivel del fernet: "))

if ingresa_nivel >= 80:
    print(" Es un fernet puro ")

elif ingresa_nivel == 50 and ingresa_nivel == 79:
    print(" Es una buena mezcla ")

elif ingresa_nivel <= 50:
    print(" Tenes más coca que fernet pa ")

## 04. Adivinar el clima

clima = float(input("Por favor ingresa el clima"))

if clima > 30:
    print( ' Que calor por dios. ')

elif 20 <= clima <= 30:
    print( ' Lindo día para unos mates.')

elif 10 <= clima < 20: 
    print( ' Hace frio , ponete una campera. ')

elif clima < 10:
    print(' No ingresaste un número valido.')


### Aclaración en este ejercicion
## La condición 10 <= clima < 20 es un operador de comparación encadenado. 
## Una forma elegante de verificar si un valor está dentro de un rango en Python.

## 05. Descuento en una tienda

tienda = int(input("Por favor ingresa el precio de tu compra"))

if tienda < 1000:
    print( " No tendras descuento ")

elif 1000 <= tienda <= 4999:
    print( " Tendras un descuento del 10 porciento")

elif 5000 <= tienda <= 9999:
    print( " Tendras un descuento del 15 porciento")

elif tienda >= 10000:
    print( " Tendras un descuento del 20 porciento ")

else:
    print( " No tendras ningún descuento")





