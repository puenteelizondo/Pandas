#importamos la libreria con el alias pd
import pandas as pd
#Creamos el diccionario
a = [1, 7, 2]
#convertimos el diccionario "a" series de panda y definimos los indices
myvar = pd.Series(a, index = ["x", "y", "z"])
#imprimimos la serie de panda
print(myvar)

#podemos accceder al dato por medio del indice
print(myvar["y"])  # Salida: 7
