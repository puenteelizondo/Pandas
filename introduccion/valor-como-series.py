#importamos panda con alias de pd
import pandas as pd
#creamos dicccionario con clave/valor
calories = {"day1": 420, "day2": 380, "day3": 390}
#lo convertimos a series de panda
myvar = pd.Series(calories)
#imprimimos la serie de panda
print(myvar)