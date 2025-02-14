#importamos las librerias panda con alias de pd
import pandas as pd
#leemos y convertimos en dataframe el json
df = pd.read_json('data.json')
#imprimimos el dataframe
print(df.to_string())