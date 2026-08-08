"""
===============================================================================
MÓDULO DE REGRESIÓN - PASO 1: CARGA Y EXPLORACIÓN DE DATOS (EDA)
Capacitación de IA - Servicio Nacional de Migración de Panamá (Día 5)
===============================================================================
"""

import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

print("\n" + "="*75)
print(" MÓDULO REGRESIÓN - PASO 1: EXPLORACIÓN DE DATOS DE HISTORIA (.CSV)")
print("="*75 + "\n")

script_dir = os.path.dirname(os.path.abspath(__file__))
ruta_historia = os.path.join(script_dir, "..", "datos", "dataset_historia_migracion.csv")

df_historia = pd.read_csv(ruta_historia)

print(f"Cargando dataset desde: {os.path.normpath(ruta_historia)} ...")
print(f"\n1. PRIMEROS 10 REGISTROS OPERATIVOS:")
print(df_historia.head(10).to_string(index=False))

print(f"\n2. DIMENSIONES DEL DATASET DE HISTORIA:")
print(f" Total de registros: {len(df_historia)} filas")
print(f" Total de variables: {df_historia.shape[1]} columnas")

print("\n3. ¿CÓMO SE VE CADA VARIABLE? (gráfico)")
print(" Se abrirá una ventana con 4 gráficos: uno por cada variable de la historia.")

COLOR_PRINCIPAL = '#2a78d6'
COLOR_PROMEDIO = '#eb6834'

variables_info = [
    ('inspectores_turno', 'Inspectores de turno', 'Cantidad de inspectores'),
    ('presupuesto_usd', 'Presupuesto operativo', 'Dólares (USD)'),
    ('tiempo_espera_min', 'Tiempo de espera', 'Minutos'),
    ('tramites_procesados', 'Trámites procesados', 'Cantidad de trámites'),
]

fig, ejes = plt.subplots(2, 2, figsize=(11, 7.5))
fig.suptitle('¿Cómo se ve cada variable en los 400 días de historia?', fontsize=14, fontweight='bold')

for ax, (columna, titulo, etiqueta_x) in zip(ejes.flat, variables_info):
    datos = df_historia[columna]
    promedio = datos.mean()
    ax.hist(datos, bins=15, color=COLOR_PRINCIPAL, edgecolor='white')
    ax.axvline(promedio, color=COLOR_PROMEDIO, linestyle='--', linewidth=2)
    ax.text(promedio, ax.get_ylim()[1] * 0.92, f'  Promedio: {promedio:,.0f}',
            color=COLOR_PROMEDIO, fontsize=9, fontweight='bold')
    ax.set_title(titulo, fontsize=11, fontweight='bold')
    ax.set_xlabel(etiqueta_x, fontsize=9)
    ax.set_ylabel('Cantidad de días', fontsize=9)

fig.tight_layout(rect=[0, 0, 1, 0.95])
print("\n(Cierra la ventana gráfica para continuar)")
plt.show()

print("\n4. ¿QUÉ TAN RELACIONADAS ESTÁN LAS VARIABLES?")

plt.figure(figsize=(10, 7))

# Renombrar columnas para que las etiquetas en el gráfico sean legibles y claras
df_corr = df_historia.rename(columns={
    'inspectores_turno': 'Inspectores',
    'presupuesto_usd': 'Presupuesto (USD)',
    'tiempo_espera_min': 'Tiempo Espera (min)',
    'tramites_procesados': 'Trámites (Target)'
}).corr()

# Dibujar Heatmap con mejor tipografía y contraste
ax = sns.heatmap(df_corr, annot=True, cmap='YlGnBu', fmt=".2f", linewidths=1.5,
                 annot_kws={"size": 12, "weight": "bold"}, cbar_kws={'label': 'Nivel de Correlación'})

plt.title('Paso 1: ¿Qué tanto influye cada variable en los trámites?', fontsize=14, fontweight='bold', pad=20)
plt.xticks(fontsize=11, rotation=15)
plt.yticks(fontsize=11, rotation=0)

# Caja de explicación explicativa integrada abajo para mejor UX
plt.figtext(0.5, 0.02,
            "[GUÍA DE LECTURA RÁPIDA DE CORRELACIÓN]:\n"
            "• Cercano a +1.0 (Azul oscuro): Si esta variable sube, los trámites TAMBIÉN SUBEN (ej: más inspectores = más trámites).\n"
            "• Cercano a -1.0 (Rojo/Claro): Si esta variable sube, los trámites BAJAN (ej: más tiempo de espera = menos trámites).\n"
            "• Cercano a 0.0: No existe relación o influencia directa.",
            ha='center', fontsize=10, bbox=dict(boxstyle='round,pad=0.6', facecolor='#f8f9fa', edgecolor='#cccccc'), color='#222222')

plt.tight_layout(rect=[0, 0.15, 1, 0.95])

print("\n(Cierra la ventana gráfica para finalizar el Paso 1)")
plt.show()

print("\n¡PASO 1 COMPLETADO! Listo para ejecutar 'paso2_entrenamiento_regresion.py'.\n")
