import pandas as pd
import glob

# Exploracion de los datos y diferentes tipos de archivos
# .csv y .xlsx

df_medellin = pd.read_csv('sucursal_medellin.csv')
print(df_medellin.head(3))

print('\n')

df_bogota = pd.read_excel('sucursal_bogota.xlsx')
print (df_bogota.head(3))
print (df_bogota.columns)
print (df_medellin.columns)

# Agrupar archivos por .csv y .xlsx
archivos_csv = glob.glob('*.csv')
archivos_xlsx = glob.glob('*.xlsx')

# Unificar dataframes en una lista
lista_informes = []

for archivo in archivos_csv:
    df = pd.read_csv(archivo)
    lista_informes.append(df)
    print (f'leido: {archivo}, - {len(df)} filas')

for archivo in archivos_xlsx:
    df = pd.read_excel(archivo)
    lista_informes.append(df)
    print (f'leido: {archivo}, - {len(df)} filas')

# Unificar dataframe
df_consolidado = pd.concat(lista_informes, ignore_index=True)
print (df_consolidado)

# Resolver renombrando las columnas
for i, df in enumerate (lista_informes):
    if 'fecha_venta' in df.columns:
        lista_informes[i] = df.rename(columns={
            'Fecha_Venta': 'fecha', 'Producto': 'producto',
            'Categoria': 'categoria', 'Cant': 'cantidad',
            'Valor_Unitario': 'precio_unitario',
            'Vendedor': 'vendedor', 'Pago': 'metodo_pago'
        })

df_consolidado = pd.concat(lista_informes, ignore_index=True)
print(df_consolidado)