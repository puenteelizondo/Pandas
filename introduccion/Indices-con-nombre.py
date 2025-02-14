#importamos la libreria panda y le ponemos el alias de pd
import pandas as pd
#creamos el diccionario con 2 claves con sus respectivos datos
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
#lo convertimos a dataframe pero ahora le damos nombres a los index que se generan
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
#imprimimos el dataframe
print(df) 
#para localizar un indice con nombre utlizamos loc y el indice
print(df.loc["day2"])