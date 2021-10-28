# %%
import pandas as pd
import numpy as np
# %%
lista = [1, 2, 4, 6]
nplista = np.array(lista)
pdlista = pd.Series(lista)

#duplicar 10 veces la lista original
print(lista * 10)
#al arreglo se le multiplica por 2 (vector * escalar)
print(nplista * 2)
# te presenta la info como una columna, pero igual hace vector * escalar
print(pdlista * 2)

# %%
#cargar un archivo csv, df = dataframe
df = pd.read_csv("insurance.csv")
#imprimir todo el archivo csv en formato "excel"
#sin el print te sale más estético
df
# %%
# imprimir los primeros 5 elementos
df.head()
# imprimit los últimos 5 elementos
df.tail()
# imrpimir 10 elementos random
df.sample(10)
# %%
#solamente mostrar valores numéricos
df.describe()

# %%
# descripción de variables desde un punto de vista de programación
df.info()

# %%
# ACCESO A LOS DATOS
# Especificas el nombre de la columna y te lo muestra índice - valor
df["age"]
# hacer que se muestre como un dataframe
df[["age"]]
# %%
# al resultado del dataframe de age and bmi, mostrar el head
df[["age", "bmi"]].head()
# %%
# Mostrar solo hasta el 3er valor sin incluirlo 
df[:3]
# %%
df[-3:]
# %%
df[["age", "bmi"]].head(2)
# %%
df
# %%
df[10:11]
# %%
df[["bmi", "age"]].mean()
# %%
df["age"].quantile([0.25, 0.5, 0.75])

# %%
import seaborn as sbs
