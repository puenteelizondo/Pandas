#la limpieza de datos es corregir datos que tienen errores 
#por ejemplo celdas vacias, formato erroneo, duplicados

#El conjunto de datos contiene algunas celdas vacías ("Fecha" en la fila 22 y "Calorías" en las filas 18 y 28).

#El conjunto de datos contiene un formato incorrecto ("Fecha" en la fila 26).

#El conjunto de datos contiene datos erróneos ("Duración" en la fila 7).

#El conjunto de datos contiene duplicados (filas 11 y 12).

#importamos la libreria panda
import pandas as pd
#leemos el archivo error.csv
df = pd.read_csv('erro.csv')
#eliminamos filas con datos con valores faltantes
#dropna() devulve el nuevo dataframe pero no cambia al original
new_df = df.dropna()
#se imprime el nuevo dataframe
print(new_df.to_string())