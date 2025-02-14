#importamos la libreria
import pandas as pd
#convertimos archivvo csv en dataframe
df = pd.read_csv('ejemplo.csv')
#imprimimos df
print(df)
#con esta configuracion lo que hace es que solo puedes traer solo 60 filas antes de que se trunque pero puede modificarse el valor

pd.options.display.max_rows = 20  # Ahora mostrará hasta 20 filas antes de truncar
print(pd.options.display.max_rows)
#en este caso no tenemos el string es porque no lo estamos imprimiendo completo