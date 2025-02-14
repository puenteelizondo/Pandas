#llamamos a la libreria
import pandas as pd
#leemos el documento
df = pd.read_csv('ejemplo.csv')
#mostramos todas las filas
pd.set_option('display.max_rows', None)
#usamos la funcion para duplicados
print(df.duplicated())
