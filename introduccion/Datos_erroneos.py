#importamos la libreria de pandas con un alias de pd
import pandas as pd
#lo convertimos a dataframe
df = pd.read_csv('ejemplo.csv')
#de la columna de edad tomamos el indice 1 y lo modificamos
df.loc[1, 'Ciudad'] = "hola1212"
#imprimimos el nuevo dataframe
print(df.to_string())