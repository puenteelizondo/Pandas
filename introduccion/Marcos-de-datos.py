#importamos la libreria de panda con el alias pd
import pandas as pd
#creamos un diccionario con 2 claves con datos(cada clave representa una columna)
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
#los 2 arrays tienen que ser de las mismas dimensiones
#lo convertimos a dataframe
myvar = pd.DataFrame(data)
#imprimimos el dataframe
print(myvar)
#tambien podemos hacer un get de la fila que necesitamos por medio del indice
print(myvar.loc[0])
#podemos hacer un get de 2 filas juntas 
print(myvar.loc[[0, 1]])
# Al utilizar [], el resultado es un Pandas DataFrame .