# primero se necesita instalar las librerias de pandas
# En este ejemplo, se busca cargar un archivo CSV en un DataFrame de pandas (estructura de datos similar a una tabla).
# Para ello, el archivo debe encontrarse en el mismo directorio.



#importamos la libreria y le damos el alias de pd
import pandas as pd
#Se lee el archivo CSV y lo almacenamos en un DataFrame que al igual se almacena en la variable df en este caso el Dataframe
df = pd.read_csv('introduccion.csv')
#DATO IMPORTANTE: Panda asume que la primera fila en el documento contine los nombres de la columna.
#Ahora imprimimos el DataFrame en formato completo
print(df.to_string())
#para correr el programa usamos solo el ambiente de python(python introduccion.py)
#anexo la imagen de como se deberian mostrar los datos en la tabla