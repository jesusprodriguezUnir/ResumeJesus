import streamlit as st
import pandas as pd
import numpy as np

@st.cache_data(ttl=3600)
def load_sample_data():
    """Generates sample data for the dashboard."""
    dates = pd.date_range(start="2023-01-01", periods=100)
    data = pd.DataFrame({
        "date": dates,
        "sales": np.random.randn(100).cumsum() + 100,
        "visitors": np.random.randint(50, 200, 100),
        "category": np.random.choice(["A", "B", "C"], 100)
    })
    return data
