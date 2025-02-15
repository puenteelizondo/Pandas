#importamos las librerias con el alias de pd
import pandas as pd
#leemos el archivo y lo convertimos a dataframe
df = pd.read_csv('data.csv')
#Calcula la correlación (df.corr()) entre las columnas numéricas del DataFrame.
print(df.corr())
#hace que la tabla 

"""
1.00 → Correlación perfecta (una columna con ella misma).
0.98 → Fuerte correlación positiva (cuando sube una, la otra también).
0.00 o cerca de 0 → No hay relación entre las variables.
-1.00 → Correlación negativa (si una sube, la otra baja)

¿Para qué sirve df.corr()?
Encontrar relaciones entre variables en análisis de datos.
Ver qué variables están conectadas (Ejemplo: ingresos y gastos).
Detectar colinealidad en modelos de Machine Learning.


"""