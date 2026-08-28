import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(page_title="Dashboard de Ventas", layout="wide")
st.title("Dashboard de Ventas")

df = pd.read_csv("ventas.csv")
df["fecha"] = pd.to_datetime(df["fecha"])
df = df.dropna(subset=["precio"]) # borra las filas donde precio esta vacio

st.sidebar.header("Filtros")
region_sel = st.sidebar.multiselect(
    "Region",
    options=df["region"].unique(),
    default=df["region"].unique()
)
producto_sel = st.sidebar.multiselect(
    "Producto",
    options=df["producto"].unique(),
    default=df["producto"].unique()    
)

df_filtrados = df[
    (df["region"].isin(region_sel)) &
    (df["producto"].isin(producto_sel))
]

# --- KPIs principales ---
col1, col2, col3 = st.columns(3)
col1.metric("Ingreso Total", f"${df_filtrados['ingreso_total'].sum():,.0f}")
col2.metric("Unidades Vendidas", f"${df_filtrados["vendidos"].sum():,}")
col3.metric("Ticket Promedio", f"${df_filtrados['ingreso_total'].mean():.2f}")

# --- Grafico 1 tendencia de ventas en el tiempo ---
ventas_dia = df_filtrados.groupby("fecha")["ingreso_total"].sum().reset_index()
fig_linea = px.line(
    ventas_dia,
    x="fecha",
    y="ingreso_total",
    title="Ingreso diario"
)
st.plotly_chart(fig_linea, width="stretch")

# --- Grafica 2 y 3 lado a lado ---
col_izq, col_der = st.columns(2)
with col_izq:
    ingreso_producto = df_filtrados.groupby("producto")["ingreso_total"].sum().reset_index()
    fig_barras = px.bar(
        ingreso_producto.sort_values("ingreso_total", ascending=False),
        x="producto",
        y="ingreso_total",
        title="ingreso por producto",
        color="producto"
    )
    st.plotly_chart(fig_barras, width="stretch")

with col_der:
    ingreso_region = df_filtrados.groupby("region")["ingreso_total"].sum().reset_index()
    fig_pie = px.pie(
        ingreso_region,
        names="region",
        values="ingreso_total",
        title="Participacion por region"
    )
    st.plotly_chart(fig_pie, width="stretch")

# --- Tabla de detalle ---
st.subheader("Detalle de ventas")
st.dataframe(df_filtrados.sort_values("fecha", ascending=False))
# se ejecuta asi : streamlit run app.py