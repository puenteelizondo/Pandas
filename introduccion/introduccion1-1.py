#importamos la libreria con el alias de pd
import pandas as pd
#creamos un diccionario con datos llamado mydataset con dos claves cars y passings
mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}
#convertimos el diccionario en dataframe y lo asignamos a la variable myvar
myvar = pd.DataFrame(mydataset)
#imprimos el dataframe
print(myvar)
#anexo la imagen con su respectivo acomodo del diccionario en el dataframe

