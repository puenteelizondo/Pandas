#importamos las librerias  con el alias de pd
import pandas as pd
#leemos el archivo y lo transformamos a dataframe
df = pd.read_csv('erro.csv')
#sacamos la mediana a la columna de calories 
x = df["Calories"].median()
#asiganamos la mediana a los valores null de la columna
#calories
df["Calories"].fillna(x, inplace = True)
#imprimimos el nuevo dataframe
print(df.to_string())