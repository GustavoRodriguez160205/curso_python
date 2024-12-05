## 01. Calcular la longitud de la cadena

cadena = input(" Ingresa una frase por favor : ")
contar_cadena = len(cadena)
print(f"La longitud de la cadena es: {contar_cadena}")


## 02. Mayúsculas y minúsculas

cadena_en_mayusculas = input(" Ingresa una frase en minúscula: ")
cadena_mayus = cadena_en_mayusculas.upper()
print(f"La frase en mayúsculas quedara asi: {cadena_mayus}")

ingresar_cadena = input(" Ingresa una cadena en mayúsculas: ")
cadena_minus = ingresar_cadena.lower()
print(f"La frase en minúsculas quedara asi: {cadena_minus}")


## 03. Reemplazar una frase

oracion = input("Ingresa una oración:")
nueva_oracion = oracion.replace("a" , "y")
print("Oración Modificada:" , nueva_oracion)


## 04. Separar palabras

oracion = input("Ingresa una oración: ")
oracion_separada = oracion.split("-") 
print("Oración separada:", oracion_separada)


## 0. Eliminar espacios en blanco

sin_espacios = input("Ingresa una oración: ")
sin_espacios_sin_bordes = sin_espacios.strip()  
print("Oración sin espacios:", sin_espacios_sin_bordes)
