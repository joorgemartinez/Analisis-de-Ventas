import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 🎨 Configuración de la página
st.set_page_config(page_title="Dashboard de Ventas", layout="wide")

# 🧾 Título
st.title("📊 Dashboard de Ventas por Tienda")

# 📂 Cargar datos
df = pd.read_csv("data/ventas_por_tienda.csv")

# Ordenar por ventas descendente
df = df.sort_values("ventas_totales", ascending=False)

# 💡 Mostrar métricas generales
st.metric("Total de tiendas", len(df))
st.metric("Ventas totales (€)", f"{df['ventas_totales'].sum():,.2f}")

# 🧰 Sidebar con filtros
st.sidebar.title("Filtros")

# Filtro por tienda específica
tiendas = df["tienda"].unique()
tienda_seleccionada = st.sidebar.multiselect("Selecciona tienda(s)", tiendas, default=tiendas[:5])

# Filtro por número de top tiendas
top_n = st.sidebar.slider("Número de tiendas a mostrar", min_value=1, max_value=len(df), value=10)

# Aplicar filtros
df_filtrado = df[df["tienda"].isin(tienda_seleccionada)].head(top_n)

# 📄 Tabla filtrada
st.subheader("📋 Tiendas seleccionadas")
st.dataframe(df_filtrado)

# 📊 Gráfico de barras
st.subheader("📈 Ventas por Tienda")
fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(df_filtrado["tienda"], df_filtrado["ventas_totales"], color="skyblue")
ax.set_ylabel("Ventas Totales (€)")
ax.set_xlabel("Tienda")
ax.set_title("Ventas por Tienda")
plt.xticks(rotation=90)
st.pyplot(fig)
