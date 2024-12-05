### Metodos de Cadenas

## Son funciones que permiten manipular, modificar y consultar cadenas de texto (strings) de manera sencilla. 
## Se usan para tareas como cambiar mayúsculas 
## y minúsculas, reemplazar texto, buscar palabras o separar contenido.

cadena1 = "Hola soy dalto"
cadena2 = "Bienvenido Maquinola"

### 01. Dir (Nos va a devolver todos los metodos). Dir no es un metodo , es una función

resultado = dir(cadena1)
#print(resultado)

### 02. Upper (Convierte todo el texto a mayúsucla)

resultado = cadena1.upper()
print(f"El texto en mayúscula es: {resultado}")

### 02. Lower (Convierte a minúsculas)

resultado = cadena1.lower()
print(f"El texto en minúscula es: {resultado}")


### 03. Capitalize (Convertimos la primera letra a mayúscula)

cadena3 = "argentina"
resultado = cadena3.capitalize()
print(f"La primer letra a mayúscula quedara asi: {resultado}")


### 04. Find (Buscamos el valor de una cadena en otra cadena). (Nos devolvera la posición en la que encuentra lo que le pedimos)

busqueda_find = cadena3.find("t")
print(f"El resultado de la busqueda es: {busqueda_find}")

## Aclaración : (Los espacios también cuentan , porque son un caracter más)
## Aclaración : (Si no encuentra lo que le pedimos , nos da -1 )

### 05. Index (Es igual al metodo find)

cadena4 = 'Hola , Argentina'
busqueda_index = cadena4.index("A")
print(f"La búsqueda con index es: {busqueda_index}")

## Aclaración: (Si no las encuentra , aca nos devuelve una exepción)