import streamlit as st
from src.core.state_manager import StateManager
from src.core.config import config
from src.components.sidebar import render_sidebar
from src.views.resume import render_resume
from src.views.dashboard import render_dashboard

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title=f"CV | {config.APP_NAME}",
    page_icon="👨‍💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    # Initialize State
    state_manager = StateManager()
    
    # Render Sidebar (Navigation)
    render_sidebar()
    
    # Router
    if state_manager.state.selected_page == "resume":
        render_resume()
    elif state_manager.state.selected_page == "dashboard":
        render_dashboard()

if __name__ == "__main__":
    main()