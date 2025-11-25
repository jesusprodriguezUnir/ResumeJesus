import streamlit as st
import feedparser
from src.utils.pdf_gen import create_pdf
from src.utils.formatting import clean_html
from src.core.config import config

def render_resume():
    # --- DATA STRUCTURES ---
    # In a real app, this might come from a database or API via src.data
    profile_data = {
        "name": "Jesús Pedro Rodríguez Castro",
        "role": "Scrum Master & Team Lead",
        "email": config.EMAIL,
        "phone": config.PHONE,
        "location": config.LOCATION,
        "summary": """
        Scrum Master y Líder Técnico Senior con más de 15 años de experiencia en desarrollo de software enterprise. 
        Especialista en tecnologías .NET y Angular con certificación Scrum Master. He liderado equipos de hasta 12 desarrolladores, 
        implementado pipelines CI/CD que han reducido el tiempo de deployment en un 75%, y desarrollado sistemas críticos 
        que procesan más de €2M en transacciones mensuales. Comprometido con la excelencia técnica y el crecimiento profesional 
        de los equipos que lidero.
        """,
        "experience": [
            {
                "role": "Responsable de Scrum y Líder Técnico",
                "company": "UNIR (La Universidad en Internet)",
                "period": "Feb 2020 - Presente",
                "location": "Madrid, ES",
                "description": """
                Lidero la transformación ágil y técnica de un equipo de 12 desarrolladores, impactando a toda la organización.
                
                *   **Gestión de Equipos:** Implementé Scrum y prácticas de ingeniería moderna, resultando en una mejora del **35%** en la productividad.
                *   **Arquitectura DDD:** Diseñé la arquitectura del núcleo del ERP Académico, asegurando escalabilidad y mantenibilidad.
                *   **DevOps Excellence:** Orquesté la adopción de CI/CD (TeamCity, Azure DevOps), logrando **150+ deployments** exitosos mensuales.
                *   **Calidad de Software:** Elevé la cobertura de pruebas al **85%** y establecí revisiones de código obligatorias.
                """,
                "stack": "`Angular 18` `.NET Core 8.0` `Python` `Azure DevOps` `Docker` `TeamCity`"
            },
            {
                "role": "Analista .NET / Analista Funcional",
                "company": "SOTEC CONSULTING",
                "period": "Jun 2010 - Feb 2020",
                "location": "Madrid",
                "description": """
                Responsable del ciclo de vida completo de aplicaciones financieras críticas.
                
                *   **Sistemas Críticos:** Mantuve y evolucioné el sistema *Fiba Solar*, procesando **€2M+** mensuales.
                *   **Optimización:** Reduje el downtime en un **60%** y optimicé consultas Oracle mejorando el rendimiento un **300%**.
                *   **Modernización:** Lideré la migración de .NET 1.1 a 4.0, extendiendo la vida útil del software legacy.
                """,
                "stack": "`C#` `ASP.NET` `Oracle` `Web Services` `Legacy Systems`"
            }
        ],
        "skills": ["Angular", ".NET Core", "C#", "Python", "SQL Server", "Docker", "Scrum", "Azure DevOps", "TeamCity"]
    }

    # --- INYECCIÓN DE CSS PERSONALIZADO ---
    # Note: Global CSS is usually injected in app.py, but specific view CSS can be here
    
    # --- ACCIONES SIDEBAR (Vista Resume) ---
    with st.sidebar:
        st.markdown("### Acciones")
        # Botón de descarga de CV PDF
        pdf_bytes = create_pdf(profile_data)
        st.download_button(
            label="📄 Descargar CV (PDF)",
            data=bytes(pdf_bytes),
            file_name="CV_Jesus_Rodriguez.pdf",
            mime="application/pdf",
            key="pdf-download"
        )
        st.markdown("---")

    # --- CONTENIDO PRINCIPAL ---

    # --- HEADER ---
    st.title(profile_data['name'])
    st.markdown(f"<h2 style='margin-top: 0 !important; border: none; color: #64748b !important; font-size: 1.5rem !important;'>{profile_data['role']}</h2>", unsafe_allow_html=True)

    st.info(f"""
    **Resumen Ejecutivo:**
    {profile_data['summary'].strip()}
    """)

    # --- EXPERIENCIA PROFESIONAL ---
    st.header("Experiencia Profesional")

    for exp in profile_data['experience']:
        with st.container():
            col1, col2 = st.columns([3, 1])
            with col1:
                st.subheader(exp['role'])
                st.markdown(f"**{exp['company']}**")
            with col2:
                st.markdown(f"<div style='text-align: right; color: #64748b;'>{exp['period']}</div>", unsafe_allow_html=True)
                st.markdown(f"<div style='text-align: right; color: #64748b;'>{exp['location']}</div>", unsafe_allow_html=True)
            
            st.markdown(exp['description'])
            if "stack" in exp:
                st.markdown(f"**Stack:** {exp['stack']}")
        st.divider()


    # --- PROYECTOS DESTACADOS ---
    st.header("Proyectos Destacados")

    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.markdown("### 🏛️ ERP Académico UNIR")
            st.caption("Arquitectura & Desarrollo Fullstack")
            st.markdown("""
            Plataforma educativa integral basada en microservicios y DDD.
            - **Reto:** Escalar para soportar 50k usuarios concurrentes.
            - **Solución:** Arquitectura desacoplada con .NET Core y Angular.
            - **Resultado:** 40% de mejora en tiempos de carga.
            """)
            st.markdown("`Angular` `.NET Core` `SQL Server`")

        with st.container(border=True):
            st.markdown("### 🚀 CI/CD Pipeline Enterprise")
            st.caption("DevOps & Automatización")
            st.markdown("""
            Estandarización del proceso de entrega de software.
            - **Reto:** Deployments manuales propensos a errores y lentos.
            - **Solución:** Pipeline automatizado con TeamCity y Docker.
            - **Resultado:** Releases pasaron de 2 semanas a 2 días.
            """)
            st.markdown("`TeamCity` `Docker` `GitFlow`")

    with col2:
        with st.container(border=True):
            st.markdown("### 🏦 Sistema Bancario Core")
            st.caption("Fintech & Alta Disponibilidad")
            st.markdown("""
            Sistema de gestión de préstamos y transacciones.
            - **Reto:** Mantener 99.9% uptime en sistema legacy.
            - **Solución:** Refactorización progresiva y optimización DB.
            - **Resultado:** Estabilidad total durante picos de carga.
            """)
            st.markdown("`C#` `Oracle` `ASP.NET`")

        with st.container(border=True):
            st.markdown("### 📊 Executive Dashboard")
            st.caption("Data Visualization")
            st.markdown("""
            Tablero de control para toma de decisiones en tiempo real.
            - **Reto:** Unificar datos de fuentes heterogéneas.
            - **Solución:** API Gateway con Python/FastAPI y frontend Reactivo.
            - **Resultado:** Visibilidad instantánea de KPIs de negocio.
            """)
            st.markdown("`Python` `FastAPI` `Angular`")


    # --- COMPETENCIAS TÉCNICAS ---
    st.header("Arsenal Tecnológico")

    def skill_bar(label, percent, color):
        st.markdown(f"""
        <div style="margin-bottom: 0.8rem;">
            <div style="display:flex; justify-content:space-between; margin-bottom:0.2rem; font-weight:500; font-size:0.9rem;">
                <span>{label}</span>
                <span style="color:{color}">{percent}%</span>
            </div>
            <div style="width:100%; background-color:#f1f5f9; border-radius:4px; height:6px;">
                <div style="width:{percent}%; background-color:{color}; height:100%; border-radius:4px;"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Frontend & Mobile")
        skill_bar("Angular 18", 95, "#dd0031")
        skill_bar("TypeScript", 90, "#3178c6")
        skill_bar("HTML5/CSS3", 85, "#e34c26")
        st.markdown("`RxJS` `SASS` `Responsive Design`")

    with col2:
        st.subheader("Backend & API")
        skill_bar(".NET Core 8", 95, "#512bd4")
        skill_bar("C#", 95, "#239120")
        skill_bar("Python / FastAPI", 75, "#3776ab")
        st.markdown("`REST` `GraphQL` `Microservices`")

    with col3:
        st.subheader("DevOps & Cloud")
        skill_bar("Azure DevOps", 85, "#0078d7")
        skill_bar("Docker", 80, "#2496ed")
        skill_bar("SQL / Oracle", 85, "#f29111")
        st.markdown("`CI/CD` `Git` `TeamCity`")


    # --- BLOG SECTION ---
    st.header("Últimas Publicaciones")

    @st.cache_data(ttl=3600)
    def fetch_blog_posts(feed_url):
        try:
            feed = feedparser.parse(feed_url)
            if feed.bozo: return []
            posts = []
            for entry in feed.entries[:3]:
                summary = clean_html(entry.get("summary", ""))
                posts.append({
                    "title": entry.get("title", "Sin Título"),
                    "link": entry.get("link", "#"),
                    "summary": summary[:120] + "..." if len(summary) > 120 else summary
                })
            return posts
        except:
            return []

    blog_posts = fetch_blog_posts(config.BLOG_FEED_URL)

    if blog_posts:
        cols = st.columns(3)
        for i, post in enumerate(blog_posts):
            with cols[i]:
                with st.container(border=True):
                    st.markdown(f"#### [{post['title']}]({post['link']})")
                    st.caption(post['summary'])
    else:
        st.info(f"Visita mi blog en [{config.BLOG_URL}]({config.BLOG_URL}) para ver mis artículos técnicos.")


    # --- CONTACTO ---
    st.header("Hablemos")
    st.write("¿Tienes un proyecto en mente o quieres discutir sobre metodologías ágiles? Envíame un mensaje.")

    contact_col1, contact_col2 = st.columns([2, 1])

    with contact_col1:
        # Formulario funcional usando FormSubmit
        contact_form = f"""
        <form action="https://formsubmit.co/{profile_data['email']}" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Tu Nombre" required style="width: 100%; padding: 10px; margin-bottom: 10px; border: 1px solid #ccc; border-radius: 5px;">
            <input type="email" name="email" placeholder="Tu Email" required style="width: 100%; padding: 10px; margin-bottom: 10px; border: 1px solid #ccc; border-radius: 5px;">
            <textarea name="message" placeholder="Tu Mensaje" required style="width: 100%; padding: 10px; margin-bottom: 10px; border: 1px solid #ccc; border-radius: 5px; min-height: 100px;"></textarea>
            <button type="submit" style="background-color: #2563eb; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer; font-weight: 600;">Enviar Mensaje</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)

    with contact_col2:
        st.markdown(f"""
        <div style="background-color: #f8fafc; padding: 20px; border-radius: 10px; border: 1px solid #e2e8f0;">
            <h4 style="margin-top:0;">Información Directa</h4>
            <p>📍 <strong>Ubicación:</strong> {profile_data['location']}</p>
            <p>📧 <strong>Email:</strong> {profile_data['email']}</p>
            <p>📱 <strong>Teléfono:</strong> {profile_data['phone']}</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("<div style='text-align: center; color: #94a3b8; font-size: 0.8rem;'>© 2023 Jesús Pedro Rodríguez Castro. Built with Streamlit & Python.</div>", unsafe_allow_html=True)
