#importamos las librerias
import pandas as pd
#leemos el archivo de errores
df = pd.read_csv('erro.csv')
#remplazamos todos los campos de las filas incompletas con 130
df.fillna(130, inplace = True)
#imprimimos 
print(df.to_string())  # Muestra todo el DataFrame sin cortes
