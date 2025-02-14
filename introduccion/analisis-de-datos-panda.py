#importamos la libreria de pandas con un alias de pd
import pandas as pd
#lo convertimos a dataframe
df = pd.read_csv('ejemplo.csv')
#imprimimos pero ahora especificamos con la funcion head que solo traiga 5 indices
print(df.head(5))
#tambien podemos imprimir las ultimas 5 columnas siguiendo la misma logica
print(df.tail())

