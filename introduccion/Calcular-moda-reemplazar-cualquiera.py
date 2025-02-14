#importamos las librerias de panda con alias de pd
import pandas as pd
#leemos el archivo y lo transformamos a dataframe
df = pd.read_csv('erro.csv')
#calculamos la moda en la columna calories y el 0 toma el primer valor que encuentre de moda
x = df["Calories"].mode()[0]
#colocamos la moda en los valores null de la columna
df["Calories"].fillna(x, inplace = True)
#imprimimos el nuevo dataframe
print(df.to_string())  
#18 y 28 remplazado por 300.0
