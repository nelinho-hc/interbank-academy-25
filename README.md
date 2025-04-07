# Procesador de Transacciones Bancarias

## 1. Introducción
Este proyecto es una aplicación CLI desarrollada en Python para procesar transacciones bancarias desde un archivo CSV y generar un reporte con:
- Balance Final
- Transacción de mayor monto
- Conteo de Transacciones: Créditos y Débitos
## 2. Instrucciones de Ejecución
### 2.1 Requisitos previos
- Python 3.8 o superior instalado
- Instalación de la librería `pandas`:
```bash
pip install pandas
```
### 2.2 Preparar archivo CSV
El archivo CSV debe tener el siguiente formato, con encabezados:
```bash
id,tipo,monto
1,Crédito,100.00
2,Débito,50.00
3,Crédito,200.00
4,Débito,75.00
5,Crédito,150.00
```
### 2.3 Ejecutar la aplicación
Edite el script `reto_ibk.py` para ingresar la ruta del archivo CSV en la variable `ruta_csv`:
```bash
ruta_csv = r"ruta_del_archivo.csv"
```
Luego, ejecute el script desde la terminal:
```bash
python reto_ibk.py
```
### 2.4 Ejemplo de salida
```bash
Reporte de transacciones
---------------------------------------------
Balance Final: 325.00
Transacción de Monto Mayor: ID 3 - 200.00
Conteo de Transacciones: Crédito: 3 Débito: 2
```
# 3. Enfoque y Solución
- Se utilizó la librería pandas para la lectura y procesamiento de datos CSV.
- Se filtraron las transacciones por tipo para obtener sumatorias y conteos.
- Se identificó la transacción de mayor monto utilizando .max() y loc.
- Todo el procesamiento se hace en memoria, garantizando rapidez y simplicidad.

# 4. Estructura del proyecto
```bash
├── reto_ibk.py      # Script principal
├── data.csv        # Archivo CSV a analizar
└── README.md        # Documentación del proyecto
```
