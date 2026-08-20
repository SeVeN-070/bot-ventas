# Análisis de Ventas - Bot de Ventas

Este proyecto realiza la consolidación, limpieza y análisis automatizado de datos de ventas provenientes de múltiples sucursales (Medellín, Cali, Bogotá y Barranquilla).

## Requisitos e Instalación

Para ejecutar este proyecto necesitas Python 3 e instalar las siguientes librerías:

```bash
pip install pandas openpyxl matplotlib

## Cómo Ejecutar

1. Asegúrate de tener los archivos `.csv` y `.xlsx` de las sucursales en la raíz del proyecto.
2. Ejecuta el script principal con el comando:

```bash
python bot.py

## Resultados y Hallazgos

| Categoría | Total Ventas ($) |
| :--- | :--- |
| Electrónica | $3,347,125.00 |
| Ropa | $2,647,170.83 |

* **Vendedor con mayores ingresos:** Camila Ruiz (28.30%).
* **Productos más populares:** Jean clásico y Cargador USB-C (10 transacciones cada uno).

## Conclusión Final

Se recomienda mantener stock constante de los productos estrella (*Jean clásico* y *Cargador USB-C*) y potenciar las campañas comerciales en la categoría *Electrónica*, por ser la de mayor aporte al volumen general de ingresos.