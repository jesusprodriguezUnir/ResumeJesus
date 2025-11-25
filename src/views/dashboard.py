import streamlit as st
import plotly.express as px
from src.data.loader import load_sample_data

def render_dashboard():
    st.title("📊 Data Dashboard")
    st.markdown("### Análisis de Métricas (Demo)")
    
    data = load_sample_data()
    
    # KPIs
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Ventas", f"€{data['sales'].sum():,.2f}")
    col2.metric("Visitantes Totales", f"{data['visitors'].sum()}")
    col3.metric("Promedio Diario", f"€{data['sales'].mean():,.2f}")
    
    # Charts
    tab1, tab2 = st.tabs(["Tendencias", "Categorías"])
    
    with tab1:
        st.subheader("Evolución Temporal")
        fig_line = px.line(data, x="date", y="sales", title="Ventas Diarias", template="plotly_white")
        st.plotly_chart(fig_line, use_container_width=True)
        
    with tab2:
        st.subheader("Distribución por Categoría")
        fig_bar = px.bar(data, x="category", y="visitors", color="category", title="Visitantes por Categoría", template="plotly_white")
        st.plotly_chart(fig_bar, use_container_width=True)
