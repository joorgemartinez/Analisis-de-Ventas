# 🛍️ Análisis de Ventas con PySpark y Streamlit

[![PySpark](https://img.shields.io/badge/PySpark-3.0+-f27d0c?style=for-the-badge&logo=apache-spark&logoColor=white&labelColor=101010)](https://spark.apache.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-ff4b4b?style=for-the-badge&logo=streamlit&logoColor=white&labelColor=101010)](https://streamlit.io/)

Este proyecto simula y analiza datos de ventas utilizando **PySpark** para el procesamiento distribuido y **Streamlit** para la visualización interactiva. Es ideal como ejemplo práctico de un mini pipeline de datos para portafolio.

---

## 📦 Estructura del proyecto

```
Analisis-de-Ventas/
├── data/
│   ├── ventas.csv                  # Datos simulados
│   ├── ventas_por_tienda.csv      # Resultado procesado por PySpark
│
├── src/
│   ├── generate_fake_data.py      # Generador de datos con Faker
│   ├── process_sales.py           # Análisis con PySpark
│
├── app.py                         # Dashboard interactivo con Streamlit
├── requirements.txt               # Dependencias del proyecto
└── README.md                      # Documentación
```

---

## 🚀 Funcionalidades del proyecto

### 🔧 1. Generación de datos
Se generan 10.000 registros de ventas ficticias con:
- Fecha de venta
- Tienda
- Producto (Portátil, Móvil, Tablet, Accesorio)
- Precio unitario y cantidad

📄 Código: `src/generate_fake_data.py`

---

### ⚙️ 2. Procesamiento con PySpark
Se procesa el CSV para:
- Calcular ventas totales por tienda
- Guardar el resultado en un solo archivo limpio `.csv`

📄 Código: `src/process_sales.py`

---

### 📊 3. Visualización con Streamlit
Se construye un dashboard interactivo con:
- Filtro por tienda
- Selector de top tiendas
- Gráfico de barras
- Tabla de resultados

📄 Código: `app.py`

---

## 🧪 Cómo ejecutar el proyecto

### 1. Clona el repositorio

```bash
git clone https://github.com/tu_usuario/Analisis-de-Ventas.git
cd Analisis-de-Ventas
```

### 2. Crea y activa el entorno virtual

```bash
python3 -m venv venv
source venv/bin/activate
```
### 3. Instala las dependencias

```bash
pip3 install -r requirements.txt
```

### 4. Genera los datos

```bash
python3 src/generate_fake_data.py
```

### 5. Procesa los datos con PySpark

```bash
python3 src/process_sales.py
```

### 6. Lanza el dashboard

```bash
streamlit run app.py
```
---

## 🖥️ Requisitos técnicos

- Python 3.9+
- Java 17
- PySpark
- Streamlit
- Faker
- Pandas
- Matplotlib
