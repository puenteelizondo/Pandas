#importamos el panda con alias de pd
import pandas as pd
#creamos el diccionario con clave/valor
calories = {"day1": 420, "day2": 380, "day3": 390}
#convertimos a series solo las claves que se especifican
myvar = pd.Series(calories, index = ["day1", "day2"])
#imprimimos
print(myvar)