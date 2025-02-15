
"""
#importamos las librerias de panda con el alias de pd
import pandas as pd
#importamos la libreria que nos permite graficar
import matplotlib.pyplot as plt
#convertimos el archivo a dataframe
df = pd.read_csv('data.csv')
#usamos la funcion para graficar
df.plot()
#mostramos la grafica
plt.show()

"""

#tambien podemos hacer un plano carteciano dandole parametros al plot
"""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')

plt.show()

"""
#si la dispersion de datos no tiene relacion entre las columnas
#el grafico sale de manera erronea


#tambien podemos hacer un histograma

import sys
import matplotlib
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df["Duration"].plot(kind = 'hist')

plt.show()

#imprimimos y guardamos como png
plt.savefig("grafica.png")  # Guarda la imagen en un archivo
sys.stdout.flush()


