#importamos la libreria pandas
import pandas as pd
#creamos una lista de valores
a = [1, 7, 2]
#convertimos la lista en una serie de pandas
myvar = pd.Series(a)
#imprimimos la serie
print(myvar)
#devuelve el valor de la serie dependiendo del indice que tenga
print(myvar[1])

#Se genera un dtype en la serie panda el cual es el tipo de dato de la lista
#anexo la imagen de dicha prueba con el mismo nombre del archivo