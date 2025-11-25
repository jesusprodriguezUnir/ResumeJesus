import streamlit as st
from src.core.state_manager import StateManager
from src.core.config import config

def render_sidebar():
    state_manager = StateManager()
    
    with st.sidebar:
        try:
            st.image("Imagen.jpeg", use_container_width=True)
        except:
            st.warning("Imagen.jpeg no encontrada")
            
        st.title(config.APP_NAME)
        
        # Navigation
        st.subheader("Navegación")
        page = st.radio("Ir a:", ["Curriculum Vitae", "Data Dashboard"], index=0 if state_manager.state.selected_page == "resume" else 1)
        
        if page == "Curriculum Vitae":
            state_manager.set_page("resume")
        else:
            state_manager.set_page("dashboard")
            
        st.markdown("---")
        
        # Contact Info (Simplified for sidebar)
        st.markdown("### Enlaces")
        st.markdown(f"""
        - [LinkedIn]({config.LINKEDIN_URL})
        - [GitHub]({config.GITHUB_URL})
        - [Blog]({config.BLOG_URL})
        """)
