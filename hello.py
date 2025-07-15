import pandas as pd

# Simular un CSV de entrada
data = {
    "id": [1, 2, 3, 4],
    "nombre": ["Ana", "Luis", "Carlos", "Lucía"],
    "ventas": [200, 150, 300, 500],
    "comisión": [0.05, 0.07, 0.06, 0.08]
}

df = pd.DataFrame(data)

# Calcular ingreso total por persona
df["ingreso_total"] = df["ventas"] * (1 + df["comisión"])

print(df)

# Guardar resultado como CSV
df.to_csv("output/ingresos_finales.csv", index=False)

print("ETL completado. Datos procesados y guardados en 'output/ingresos_finales.csv'")

