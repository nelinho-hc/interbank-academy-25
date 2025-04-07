import pandas as pd

ruta_csv = r"data.csv"
df = pd.read_csv(ruta_csv, sep=",")

# Cálculo del Balance Final
## Se utiliza 'df.loc[]' para ubicar las filas por tipo igual a "Débito" y "Crédito"
## Se utiliza 'sum()' para calcular la suma del monto por tipo

total_debito = df["monto"].loc[df["tipo"] == "Débito"].sum()
total_credito = df["monto"].loc[df["tipo"] == "Crédito"].sum()

balance_final = total_credito - total_debito

# Cálculo de la Transacción de Mayor Monto
## Se utiliza 'df.loc[]' para ubicar la fila que contenga la transacción de monto mayor
## Se utiliza 'index' para obtener el índice de la fila encontrada previamente

tr_mayor = df.loc[df["monto"] == df["monto"].max()]
indice_tr = tr_mayor.index[0]

id_tr_mayor = tr_mayor["id"][indice_tr]
monto_tr_mayor = tr_mayor["monto"][indice_tr]

# Conteo de Transacciones
## Se utiliza 'df.loc[]' para ubicar las filas por tipo igual a "Débito" y "Crédito"
## Se utiliza 'count()' para calcular el recuento por cada tipo

recuento_credito = df["tipo"].loc[df["tipo"] == "Crédito"].count()
recuento_debito = df["tipo"].loc[df["tipo"] == "Débito"].count()

print(f"""Reporte de transacciones
---------------------------------------------
Balance Final: {balance_final:.2f}
Transacción de Monto Mayor: ID {id_tr_mayor} - {monto_tr_mayor:.2f}
Conteo de Transacciones: Crédito: {recuento_credito} Débito: {recuento_debito}""")