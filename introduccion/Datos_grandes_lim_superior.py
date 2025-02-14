#importamos la libreria de panda
import pandas as pd
#leemos el documento
df = pd.read_csv('ejemplo.csv')
#leemos los datos del dataframe y los que superen 120 los iguale a 120
for x in df.index:
  if df.loc[x, "Salario"] > 2000:
    df.loc[x, "Salario"] = 2000
#imprimimos
print(df.to_string())

#para eliminar los que pasan ese limite

#for x in df.index:
 # if df.loc[x, "Duration"] > 120:
  #  df.drop(x, inplace = True)