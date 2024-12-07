########################################
### Condicionales

### 01.
## Escribe un programa que reciba la temperatura actual en Buenos Aires e indique:
##  -"Hace frío" si está por debajo de 15°C.
##  -"Está agradable" si está entre 15°C y 25°C.
##  -"Hace calor" si supera los 25°C.

temperatura_bsas = int(input(" Por favor ingresa una temperatura: "))

if temperatura_bsas < 10:
    print("Hace frio")

elif temperatura_bsas == 15:
    print("Está Bien")
    if temperatura_bsas == 25:
        print(f"Está agradable hace {temperatura_bsas}")

elif temperatura_bsas >= 30 and temperatura_bsas <= 50:
     print(f"Hace calor, la temperatura es de: {temperatura_bsas} grados")


### 02. 
## Crea un programa que reciba una fecha (día y mes) e indique si corresponde a un feriado nacional en Argentina. Ejemplo:
## 25 de mayo: Día de la Revolución de Mayo.
## 9 de julio: Día de la Independencia.

dia = int(input("Ingresa un día por favor: "))
mes = int(input("Ingresa un número de mes por favor (1-12): "))

if dia == 25 and mes == 5:
    print("Es feriado, ¡Día de la Revolución de Mayo!")
elif dia == 9 and mes == 7:
    print("Es feriado, ¡Día de la Independencia!")
else:
    print("No es feriado. El día y mes no coinciden.")



### 03.
## Crea un programa que:
## Pida al usuario que ingrese el nombre de un equipo de fútbol argentino (por ejemplo: Boca, River, Racing, etc.).
## Imprima el estadio correspondiente.

estadios = {
    "River Plate": "Más Monumental",
    "Racing Club": "El Cilindro de Avellaneda",
    "Boca Juniors": "La Bombonera"
}

equipo = input("Por favor ingresa tu club y te diré el nombre de su estadio: ")

if equipo in estadios:
    print(f"El equipo es: {equipo} y su estadio es: {estadios[equipo]}.")
else:
    print("No hay ningún club registrado con ese nombre.")


### 04.
## Crea un programa que:
## Almacene las edades en una lista.
## - Luego, clasifique y muestre cuántas personas hay en cada grupo de edad:
## - Menores de 18 años.
## - Entre 18 y 60 años.
## - Mayores de 60 años.


edades = int(input(" Ingresa una edad por favor: "))

if edades <= 18:
    print("Sos adolescente")

elif edades == 18 and edades <= 60:
    print("Sos un Adulto")

elif edades >= 60:
    print("Sos un jubilado")

