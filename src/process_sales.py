from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import os
import shutil
import glob

# 1️⃣ Iniciar sesión de Spark
spark = SparkSession.builder \
    .appName("Analisis de Ventas") \
    .getOrCreate()

# 2️⃣ Cargar el CSV original
df = spark.read.csv("data/ventas.csv", header=True, inferSchema=True)

# 3️⃣ Vista previa
print("✅ Vista previa de los datos:")
df.show(5)

# 4️⃣ Calcular total_venta
df = df.withColumn("total_venta", col("precio_unitario") * col("cantidad"))

# 5️⃣ Agregación por tienda
ventas_por_tienda = df.groupBy("tienda") \
    .sum("total_venta") \
    .withColumnRenamed("sum(total_venta)", "ventas_totales") \
    .orderBy("ventas_totales", ascending=False)

# 6️⃣ Mostrar resultados
print("📊 Ventas totales por tienda:")
ventas_por_tienda.show(10)

# 7️⃣ Guardar en carpeta temporal con solo una partición
temp_path = "data/temp_ventas_por_tienda"
ventas_por_tienda.coalesce(1).write.csv(temp_path, header=True, mode="overwrite")

# 8️⃣ Buscar el archivo CSV generado y renombrarlo
output_path = "data/ventas_por_tienda.csv"

# Eliminar archivo anterior si existe
if os.path.exists(output_path):
    os.remove(output_path)

# Buscar archivo generado por PySpark
part_file = glob.glob(os.path.join(temp_path, "part-*.csv"))[0]
shutil.move(part_file, output_path)

# Eliminar la carpeta temporal (incluye _SUCCESS y demás)
shutil.rmtree(temp_path)

print(f"✅ Archivo final guardado como: {output_path}")

# 9️⃣ Cerrar Spark
spark.stop()
