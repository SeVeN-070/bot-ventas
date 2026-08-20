import pandas as pd
import glob
import matplotlib.pyplot as plt

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


# PARTE 3: Renombrar columnas
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
print(df_consolidado.columns)


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


#CONTINUACION

# --------------------------------------------
# PREGUNTA 1: ¿Cuánto vendió cada categoría en total?
# (EJEMPLO RESUELTO)
# --------------------------------------------

ventas_categoria = df_consolidado.groupby('categoria')['precio_unitario'].sum()
print(ventas_categoria)

ventas_categoria.plot(kind='bar', title='Ventas por Categoria')
plt.ticklabel_format(style='plain', axis='y')
plt.ylabel('Ventas totales ($)')
plt.xlabel('Categoría')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("grafico_categoria.png")
plt.show()

# --------------------------------------------
# PREGUNTA 2: ¿Qué porcentaje de las ventas representa 
# cada vendedor?
# --------------------------------------------
print("\n=== PREGUNTA 2: Porcentaje de Ventas por Vendedor ===")
# Paso 1: agrupen por vendedor y sumen precio_unitario
ventas_vendedor = df_consolidado.groupby('vendedor')['precio_unitario'].sum()

# Paso 2: impriman el resultado (en porcentaje)
porcentaje_vendedor = (ventas_vendedor / ventas_vendedor.sum()) * 100
print(porcentaje_vendedor.round(2))

# Paso 3: hagan un gráfico de torta (pie) con porcentajes
plt.figure(figsize=(6, 6))
ventas_vendedor.plot(kind='pie', autopct='%1.1f%%', startangle=140, title='Porcentaje de Ventas por Vendedor')
plt.ylabel('')
plt.tight_layout()

# Paso 4: guarden como "grafico_vendedor.png"
plt.savefig("grafico_vendedor.png")
plt.close()


# --------------------------------------------
# PREGUNTA 3: ¿Cuál es el producto que más se vende?
# --------------------------------------------
print("\n=== PREGUNTA 3: Producto más vendido ===")
# Paso 1: investiguen la función value_counts()
# Paso 2: apliquenla a la columna producto
mas_vendidos = df_consolidado['producto'].value_counts()

# Paso 3: impriman el resultado
print(mas_vendidos)


# --------------------------------------------
# PREGUNTA 4: ¿Cómo se distribuyen las ventas según 
# el método de pago?
# --------------------------------------------
print("\n=== PREGUNTA 4: Ventas por Método de Pago ===")
# Paso 1: agrupen por metodo_pago y sumen precio_unitario
ventas_metodo_pago = df_consolidado.groupby('metodo_pago')['precio_unitario'].sum()

# Paso 2: impriman el resultado
print(ventas_metodo_pago)

# Paso 3: hagan el gráfico que consideren más apropiado
plt.figure(figsize=(7, 5))
ventas_metodo_pago.plot(kind='barh', color='#2ca02c', title='Distribución de Ventas por Método de Pago')
plt.xlabel('Ventas ($)')
plt.ylabel('Método de Pago')
plt.ticklabel_format(style='plain', axis='x')
plt.tight_layout()

# Paso 4: guarden como "grafico_metodo_pago.png"
plt.savefig("grafico_metodo_pago.png")
plt.close()

print("\n¡Ejecución completada! Se han generado los 3 gráficos en tu carpeta.")


# ============================================
# NUEVO ANALISIS - agregar en la rama "mejoras"
# ============================================

# Pregunta 6: Precio promedio de venta por categoria
precio_promedio_categoria = df_consolidado.groupby('categoria')['precio_unitario'].mean()
print("Precio promedio por categoria:")
print(precio_promedio_categoria)

# Pregunta 7: Cantidad de transacciones por vendedor
transacciones_por_vendedor = df_consolidado.groupby('vendedor')['precio_unitario'].count()
print("Cantidad de transacciones por vendedor:")
print(transacciones_por_vendedor)

# Guardar este analisis extra en un nuevo archivo
resumen_extra = pd.DataFrame({
    'precio_promedio': precio_promedio_categoria
})
resumen_extra.to_excel("analisis_extra.xlsx")