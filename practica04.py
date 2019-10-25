"""
	# practica04
	## En función del archivo .txt, hacer:
	- Encontrar todos los que han hecho mas de 3 goles
	- Encontrar los que son del país Nigeria
	- El valor mínimo y máximo de la caracteristica Height
	author: juanyanza11
"""
import codecs
import json
archivo = codecs.open("datos.txt")
lineas = archivo.readlines()
lineas_diccionario = [json.loads(l) for l in lineas]

funcion1 = lambda x: list(x.items())[1][1] > 3
funcion2 = lambda x: list(x.items())[0][1] == "Nigeria"

lista1 = list(map(lambda x: list(x.items())[2][1], lineas_diccionario)) # Lista en la posición de la estatura a comparar
maximo = max(lista1)
minimo = min(lista1)

lmax = list(filter(lambda x: list(x.items())[2][1] == maximo, lineas_diccionario)) # Lista Comparación del valor máximo de la estatura para imprimir el jugador
lmin = list(filter(lambda x: list(x.items())[2][1] == minimo, lineas_diccionario)) # Lista Comparación del valor mínimo de la estatura para imprimir el jugador
listmax = max(lista1) # Maximo 197 se comparan con lmax
listmin = min(lista1) # Minimo 168 se comparan con lmin

goles = list(filter(funcion1, lineas_diccionario)) # Jugadores >= 3 GOLES
pais_Nigeria = list(filter(funcion2, lineas_diccionario)) # Paises de NIGERIA

print("\nPersonas con goles mayores a 3:\n\n",goles, "\n")
print("Personas de Nigeria: \n\n",pais_Nigeria, "\n")
print("Estatura maxima:\n\n",lmax, "\n")
print("Estatura minima:\n\n",lmin, "\n")