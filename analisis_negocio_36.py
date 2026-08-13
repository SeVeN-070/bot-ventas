# ============================================
# ANÁLISIS DE NEGOCIO - Bot de Ventas
# (continúa después de tu código de lectura, 
# consolidación y limpieza ya hecho)
# ============================================
import matplotlib.pyplot as plt

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
# Paso 1: agrupen por vendedor y sumen precio_unitario
# Paso 2: impriman el resultado
# Paso 3: hagan un gráfico de torta (pie) con porcentajes
# Paso 4: guarden como "grafico_vendedor.png"



# --------------------------------------------
# PREGUNTA 3: ¿Cuál es el producto que más se vende?
# --------------------------------------------
# Paso 1: investiguen la función value_counts()
# Paso 2: apliquenla a la columna producto
# Paso 3: impriman el resultado



# --------------------------------------------
# PREGUNTA 4: ¿Cómo se distribuyen las ventas según 
# el método de pago?
# --------------------------------------------
# Paso 1: agrupen por metodo_pago y sumen precio_unitario
# Paso 2: impriman el resultado
# Paso 3: hagan el gráfico que consideren más apropiado
# Paso 4: guarden como "grafico_metodo_pago.png"


# --------------------------------------------
# RETO OPCIONAL - Para quien termine las 4 preguntas
# PREGUNTA 5: ¿Cuál es el día de la semana con más ventas?
# --------------------------------------------
# Paso 1: investiguen pd.to_datetime() para convertir la columna 
# fecha a formato de fecha real
# Paso 2: investiguen .dt.day_name() para extraer el día de la semana
# Paso 3: agrupen por ese nuevo dato y sumen las ventas