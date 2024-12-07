### Practica de metodos de cadenas en python

## 01. Contar la frecuencia de una palabra en la cadena

contar = input( "Ingresa una frase por favor:" )
veces_repetidas = contar.count("a")
print(f"La palabra se repite {veces_repetidas}")


## 02. Reemplazar un texto dentro de una cadena

reemplazo = "Hola a todos como están"
texto_Cambiado = reemplazo.replace("como" , "Como")
print(f"La frase cambiada queda asi: {texto_Cambiado}.")

## 03. Comprobar si una cadena empieza o termina con una subcadena

empieza = "Javier Milei va a ser uno de los mejores presidentes de Argentina"
verificar = empieza.startswith("Javier")
print(f"Seguro ue empieza con esa?: {verificar}")

## 04. Convertir una cadena a mayúsculas 

may = input("Ingresa una cadena para poner en mayúscula: ").upper()
print(f"La cadena en mayúscula queda así: {may}")

min_ = input("Ingresa una cadena para poner en minúscula: ").lower()
print(f"La cadena en minúscula queda así: {min_}")
