import pandas as pd

# Leemos el archivo especificando el separador correcto
df = pd.read_csv('formato_errores.csv', sep=";")

# Convertimos la columna 'Fecha' a tipo datetime
df['Fecha'] = pd.to_datetime(df['Fecha'], errors='coerce')

# Imprimimos el DataFrame

#tambien podemos eliminar la fila con el formato incorrecto
#df.dropna(subset=['Fecha'], inplace = True)

print(df.to_string())