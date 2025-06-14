# Importamos las librerías necesarias
from faker import Faker          # Para generar datos falsos realistas
import pandas as pd             # Para manipular los datos como DataFrame
import random                   # Para elegir productos, precios y cantidades aleatoriamente

# Creamos una instancia de Faker para generar datos falsos
fake = Faker()

# Establecemos semillas para Faker y random para que los datos generados
# sean siempre iguales al ejecutar el script (útil para depuración y pruebas)
Faker.seed(42)
random.seed(42)

# Función que genera datos falsos de ventas
def generar_datos(n=1000):  # n es el número de registros que se quieren generar
    data = []  # Lista vacía donde iremos añadiendo cada venta simulada

    # Bucle que genera 'n' ventas
    for _ in range(n):
        venta = {
            "fecha": fake.date_between(start_date="-1y", end_date="today"),  # Fecha entre hace un año y hoy
            "tienda": fake.company(),                                        # Nombre de empresa falsa
            "producto": random.choice(["Portátil", "Móvil", "Tablet", "Accesorio"]),  # Producto aleatorio
            "precio_unitario": round(random.uniform(50, 2000), 2),           # Precio entre 50 y 2000 euros
            "cantidad": random.randint(1, 5)                                 # Cantidad entre 1 y 5 unidades
        }
        data.append(venta)  # Añadimos la venta a la lista

    # Convertimos la lista de ventas a un DataFrame de pandas
    df = pd.DataFrame(data)

    # Guardamos el DataFrame en un archivo CSV en la carpeta "data/"
    df.to_csv("data/ventas.csv", index=False)

    # Mostramos mensaje de confirmación
    print("✅ Datos guardados en data/ventas.csv")

# Esta parte se ejecuta solo si el archivo se ejecuta directamente
# Aquí indicamos que queremos generar 10.000 filas
if __name__ == "__main__":
    generar_datos(10000)

