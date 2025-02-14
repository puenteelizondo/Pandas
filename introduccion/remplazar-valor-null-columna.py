#importamos las librerias de panda con alias de pd
import pandas as pd
#leemos el archivo
df = pd.read_csv('erro.csv')
#obtenemos el dataframe y en la columna de calories que tenga valores null
#remplazamos con un 130
df["Calories"].fillna("hola", inplace = True)
#imprimimos
print(df.to_string())
#en la fila 28 esta el error