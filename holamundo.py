print("Hola mundo")
print("Bienvenido a Python")
print("_______")
print("UPB")

#tipos de datos en variables
Nombre= "lilia" #Cadena
Edad=21 #Numérico entero
Correo="liliapoot27@gmail.com" #Cadena
Promedio=8.5    #Numero de punto flotante (Float)
Beca= False     #booleano


#Imprimir los datos

print("Nombre: ", Nombre)
print("Tipo de la variable nombre: ", type(Nombre))

print("Edad: ", Edad)
print("Tipo de la variable Edad: ", type(Edad))

print("Edad: ", Correo)
print("Tipo de la variable Correo: ", type(Correo))

print("Edad: ", Promedio)
print("Tipo de la variable Promedio: ", type(Promedio))

print("Edad: ", Beca)
print("Tipo de la variable Beca: ", type(Beca))


#Operadores +, -, , /, %(Residuo), // (División entera), * (Exponente)

potencia2 = 2**10
residuo = 105 % 6


print(potencia2)
print(residuo)

# Condiciones if-else (operadores ==, >, >=, <, <=, !=)

edad = 15
if edad >= 18:
    print("Puede votar")
    print("Espero verte este 6 de junio")
else:
    print("No puede votar")
    print("Tan pronto tengas la edad, solicito tu INE")


# Listas en python
# Es un arreglo de elementos del cual la lista puede ser actulizando

alumno = ["Valentin", "Rosendo", "Valentin2", "Lili", "Leydi", "Alan", "Jonathan"]
print(type(alumno))

#Imprimir elementos individuales, con el índice inicindo desde 0
print(alumno[0])
print(alumno[1])
print(alumno[2])
print(alumno[3])
print(" ")
print("____________")
print(" ")
#Imprimir los elementos en un ciclo, recorrer la lista

i=0

for elemento in alumno:
    print(elemento)
    i=i+1


for i in range (100, 110, 2):
    print(i)

#while
print("while")
print("Elementos de la lista 2")
lista2=["pantalla","teclado","bocinas", "mouse", "usb", "cd", "quemador", "impresora", "microfono", "webcam"]
print(lista2)

#Recorrer la lista 2 con while
i=0
while i < len(lista2):
    print(i, ":",lista2[i])
    i=i+1

#acceder a los elementos de las lista2 por medio de los indices
    print("La lista2 tiene ", len(lista2), " elementos")
    print("Todos los elementos 0-9", lista2[0:10])
    print("elementos del 2-6", lista2[2:7])
    print("Elementos desde el 5 hasta el ultimo", lista2[5:])
    print("Imprimir los primeros 3 elementoss", lista2[:3])


# Realizar los siguientes ejercicios
# 1. Extraer 'mouse', 'usb', 'cd', 'quemador', 'impresora' con indices
# 2. extraer   'mouse', 'usb', 'cd', 'quemador', 'impresora', 'microfono', 'webcam'
# 3. extraer 'pantalla', 'teclado', 'bocinas', 'mouse', 'usb', 'cd', 'quemador', 'impresora'
# 4. extraer 'pantalla', 'bocinas',  'usb', 'quemador', 'microfono'
# 5. Programar para extraer de lista2, la sublista equipo = ['mouse', 'cd', 'microfono', 'cargador'] , que aparezca sú número de índice de cada uno
# Resultado esperado:
# Indice 3 : mouse
# Indice 5 : cd
# Indice 8 : microfono
# Cargador NO encontrado en lista2
lista2 = ["pantalla", "teclado", "bocinas", "mouse", "usb", "cd", "quemador", "impresora", "microfono", "webcam"]
equipo = ['mouse', 'cd', 'microfono', 'cargador']
    
#1 
print("ejercicio 1: ", lista2[3:8])
 
#2
print("ejercicio 2: ", lista2[3:10])

#3
print("ejercicio 3: ", lista2[0:8])

#4 len es una cadena para para saber el numero posiciones 
print("ejercicio 4:",[lista2[i] for i in range(len(lista2)) if i % 2 == 0])


#___________________________________________________________________________________________________



cadenaLarga = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent gravida euismod lorem non convallis. Pellentesque convallis iaculis sem, nec aliquet nulla. Integer quis rutrum sem. Donec orci dolor, vestibulum ut dictum vel, ultrices vel tellus. Vivamus blandit lobortis elit, id interdum tortor sodales tempus. Maecenas ut ante nec leo ultricies sollicitudin. Vivamus tempus leo quis odio dignissim tristique. Nam lorem ex, euismod in vestibulum id, laoreet ut arcu. Suspendisse scelerisque, mi a auctor dapibus, ipsum sem tincidunt est, porta elementum enim sem et massa.

Donec arcu urna, mattis ut mollis suscipit, pulvinar elementum sem. Praesent lacus nulla, ultricies vel orci ac, luctus dapibus metus. Pellentesque hendrerit mollis est. Maecenas leo tortor, viverra at magna id, consequat bibendum massa. Donec sit amet risus in sem vestibulum mollis. In sodales leo tellus, venenatis tincidunt nisl feugiat eu. Aliquam in pellentesque turpis. Nunc gravida diam a lectus sollicitudin ornare. Proin non eros quis odio pretium convallis. In pretium laoreet felis et tristique.

Maecenas rhoncus placerat dolor, in finibus nibh dictum sit amet. Sed malesuada condimentum ipsum, ut lacinia massa fermentum eu. Sed vel condimentum nulla, vitae gravida magna. Aliquam erat volutpat. Nam mollis tempor tempor. Vestibulum accumsan, arcu ac rhoncus commodo, augue augue interdum est, ac tincidunt ipsum urna vitae dui. Sed mollis in neque id gravida. Suspendisse in tempus eros. Nunc dignissim odio pretium ligula porta, a ultrices dui commodo. Phasellus sagittis hendrerit mauris, in faucibus lorem rutrum ac. Pellentesque posuere vulputate sem, fermentum feugiat dolor lobortis eu. Vivamus ac blandit elit, non rhoncus enim. Sed eu dapibus lacus. Praesent bibendum quam aliquam metus vestibulum commodo. Cras in dui dignissim, dapibus turpis vel, sollicitudin massa. Aenean nec risus massa.

Ut ullamcorper id libero et vestibulum. Etiam euismod massa sit amet mauris interdum consequat. Sed pharetra purus eget sodales posuere. Nulla facilisi. Donec egestas nisi ac erat tincidunt dapibus. Nulla facilisi. Nunc et metus ut metus fringilla dictum commodo sit amet risus. Cras semper odio tellus, eget molestie ipsum volutpat non. Morbi urna purus, semper non fermentum et, blandit eget diam. Duis est lectus, posuere ut metus id, egestas congue sapien. Curabitur libero est, auctor eu placerat rutrum, luctus vitae tortor. Maecenas at egestas velit. Phasellus id odio ac tellus facilisis elementum id id metus. Cras dignissim sed erat id efficitur. Nunc mauris libero, suscipit vitae ultricies sit amet, fringilla vitae ex. In nec aliquam magna.

Donec ornare nibh sit amet urna rutrum mollis. Praesent non ligula ut mi sollicitudin volutpat. Aliquam eu tellus velit. Cras ipsum velit, convallis vitae est sed, euismod sodales enim. Sed eget interdum risus, vel iaculis nisl. Fusce at porttitor risus, vitae pretium metus. Nunc sit amet felis sem. Phasellus ut pretium quam. Vivamus sed consequat turpis. Maecenas ullamcorper erat nunc, ac molestie leo tempus in. Interdum et malesuada fames ac ante ipsum primis in faucibus. Aenean et eleifend nunc. Mauris magna tellus, maximus eget suscipit a, tincidunt eget justo.
"""

print(cadenaLarga)

caracteres =['a', 'e','i', 'o','u', ' ', ',' ,';']  


#Dada una cadena larga (lorem ipsum de 5 párrafos)
#resentar un resumen de las estadísticas de los párrafos

#Total de caracteres:
#Total de letras (incluyendo vocales) :
#Total de vocales :
#Total de vocales a :
#Total de vocales e :
#Total de vocales i :
#Total de vocales o :
#Total de vocales u :
#Total de espacios :
##Total de comas :
#Total de palabras :

# Inicializar variables de estadísticas
total_caracteres = 0
total_letras = 0
total_vocales = 0
total_vocales_a = 0
total_vocales_e = 0
total_vocales_i = 0
total_vocales_o = 0
total_vocales_u = 0
total_espacios = 0
total_comas = 0
total_palabras = 0
total_punto_coma = 0

# Iterar sobre cada carácter en la cadena larga
for caracter in cadenaLarga:
    total_caracteres += 1 # para incrementar el valor de una variable sumándole otro valoren este caso es 1
    if caracter.isalpha():  # Verificar si el carácter es una letra
        total_letras += 1
        if caracter.lower() in ['a', 'e', 'i', 'o', 'u']:  # Verificar si es una vocal
            total_vocales += 1
            if caracter.lower() == 'a':
                total_vocales_a += 1
            elif caracter.lower() == 'e':#es una breviatura de else
                total_vocales_e += 1
            elif caracter.lower() == 'i':
                total_vocales_i += 1
            elif caracter.lower() == 'o':
                total_vocales_o += 1
            elif caracter.lower() == 'u':
                total_vocales_u += 1
    elif caracter == ' ':# para incrementar el valor de una variable sumándole otro valor
        total_espacios += 1
    elif caracter == ',':
        total_comas += 1
    elif caracter == ';':
        total_punto_coma +=1

# Calcular el total de palabras
total_palabras = len(cadenaLarga.split())#divide la cadena en palabras (separadas por espacios) y luego cuenta la longitud de la lista resultante

# Imprimir estadísticas
print("Estadisticas:")
print("Total de caracteres:", total_caracteres)
print("Total de letras (incluyendo vocales):", total_letras)
print("Total de vocales:", total_vocales)
print("Total de vocales a:", total_vocales_a)
print("Total de vocales e:", total_vocales_e)
print("Total de vocales i:", total_vocales_i)
print("Total de vocales o:", total_vocales_o)
print("Total de vocales u:", total_vocales_u)
print("Total de espacios:", total_espacios)
print("Total de comas:", total_comas)
print("Total de palabras:", total_palabras)
print("Total de punto coma:", total_punto_coma)


#version 2 
