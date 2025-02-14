#importamos la librerias
import pandas as pd
#leemor el archivo y lo convertimos a dataframe
df = pd.read_csv('erro.csv')
#le decimos que remplace el viejo por el nuevo dataframe que se crea
df.dropna(inplace = True)
#imprimimos el nuevo
print(df.to_string())
#eliminamos la fila 22 en este caso en el archivo esta erroneo