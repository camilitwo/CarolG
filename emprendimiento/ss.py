#Leer excel Producto de Emprendimiento .xlsx
import pandas as pd

df = pd.read_excel('Producto de Emprendimiento .xlsx', sheet_name='Hoja1')

print(df)