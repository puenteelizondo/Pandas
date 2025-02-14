#importamos las librerias de panda
import pandas as pd
#leemos el documento y lo pasamos a dataframe
df = pd.read_csv('erro.csv')
#de la columna de calories sacamos la media con la funcion mean
x = df["Calories"].mean()
#obtenmos el nuevo daataframe 
df["Calories"].fillna(x, inplace = True)
#imprimimos el dataframe
#lo que hace es que pone la media en los valores null de la columna calories
print(df.to_string())