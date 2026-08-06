import pandas as pd
import glob

# --------------------------------------------
# PARTE 1: Buscar y leer los archivos
# --------------------------------------------
# Usamos el prefijo 'sucursal_*' para evitar leer el archivo final consolidado
archivos_csv = glob.glob("sucursal_*.csv")
archivos_xlsx = glob.glob("sucursal_*.xlsx")

lista_informes = []

for archivo in archivos_csv:
    df = pd.read_csv(archivo)
    lista_informes.append(df)
    print(f"Leído: {archivo} - {len(df)} filas")

for archivo in archivos_xlsx:
    df = pd.read_excel(archivo, engine='openpyxl')
    lista_informes.append(df)
    print(f"Leído: {archivo} - {len(df)} filas")


# --------------------------------------------
# PARTE 2: Consolidar (primer intento)
# --------------------------------------------
df_consolidado = pd.concat(lista_informes, ignore_index=True)
print("\nColumnas iniciales:", df_consolidado.columns.tolist())


# --------------------------------------------
# PARTE 3: Renombrar columnas (Sucursal Bogotá tiene nombres distintos)
# --------------------------------------------
for i, df in enumerate(lista_informes):
    if 'Fecha_Venta' in df.columns:  # Columna única de Bogotá
        lista_informes[i] = df.rename(columns={
            'Fecha_Venta': 'fecha',
            'Producto': 'producto',
            'Categoria': 'categoria',
            'Cant': 'cantidad',
            'Valor_Unitario': 'precio_unitario',
            'Vendedor': 'vendedor',
            'Pago': 'metodo_pago'
        })

df_consolidado = pd.concat(lista_informes, ignore_index=True)
print("Columnas corregidas (deben ser exactamente 7):", df_consolidado.columns.tolist())


# --------------------------------------------
# PARTE 4: Limpieza de datos
# --------------------------------------------

# 4a. Eliminar filas duplicadas
filas_antes = len(df_consolidado)
df_consolidado = df_consolidado.drop_duplicates()
print(f"Filas antes: {filas_antes} - después: {len(df_consolidado)}")

# 4b. Explorar valores nulos
print("\nValores nulos antes de rellenar:")
print(df_consolidado.isnull().sum())

# 4c. Rellenar datos faltantes
df_consolidado['metodo_pago'] = df_consolidado['metodo_pago'].fillna('No registrado')
df_consolidado['vendedor'] = df_consolidado['vendedor'].fillna('Sin asignar')

# Para el precio unitario faltante, imputamos el precio promedio del producto correspondiente
df_consolidado['precio_unitario'] = df_consolidado.groupby('producto')['precio_unitario'].transform(
    lambda x: x.fillna(x.mean())
)

print("\nValores nulos después de la limpieza:")
print(df_consolidado.isnull().sum())


# --------------------------------------------
# PARTE 5: Guardar el resultado
# --------------------------------------------
df_consolidado.to_excel("consolidado_limpio.xlsx", index=False)
print("\nArchivo guardado con éxito como 'consolidado_limpio.xlsx'")