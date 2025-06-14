from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr

# 1️⃣ Iniciar una sesión de Spark
spark = SparkSession.builder \
    .appName("Analisis de Ventas") \
    .getOrCreate()

# 2️⃣ Cargar el CSV con PySpark
df = spark.read.csv("data/ventas.csv", header=True, inferSchema=True)

# 3️⃣ Mostrar las primeras filas para asegurarte de que se ha cargado bien
print("✅ Vista previa del DataFrame:")
df.show(5)

# 4️⃣ Añadir columna 'total_venta' = precio_unitario * cantidad
df = df.withColumn("total_venta", col("precio_unitario") * col("cantidad"))

# 5️⃣ Agrupar por tienda y calcular ventas totales por tienda
ventas_por_tienda = df.groupBy("tienda") \
                      .sum("total_venta") \
                      .withColumnRenamed("sum(total_venta)", "ventas_totales") \
                      .orderBy("ventas_totales", ascending=False)

print("📊 Ventas totales por tienda:")
ventas_por_tienda.show(10)

# 6️⃣ Guardar resultados como CSV (opcional)
ventas_por_tienda.write.csv("data/ventas_por_tienda.csv", header=True, mode="overwrite")

# 7️⃣ Finalizar la sesión de Spark
spark.stop()
