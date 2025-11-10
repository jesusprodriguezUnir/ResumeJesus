import streamlit as st
import feedparser  # Para leer el feed RSS del blog
import re          # Para limpiar el HTML del resumen del blog

# --- CONFIGURACIÓN DE LA PÁGINA ---
# Usamos el modo "wide" para aprovechar mejor el espacio
st.set_page_config(
    page_title="CV | Jesús Pedro Rodríguez Castro",
    page_icon="👨‍💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- INYECCIÓN DE CSS PERSONALIZADO ---
# Añadimos estilos para mejorar la apariencia
st.markdown("""
<style>
/* Importar fuente profesional */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

/* Estilos globales */
* {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}

/* Cabecera principal */
h1 {
    color: #1a365d !important;
    font-weight: 700 !important;
    font-size: 2.5rem !important;
    margin-bottom: 1rem !important;
    letter-spacing: -0.025em !important;
}

/* Subtítulos */
h2, h3 {
    color: #2d3748 !important;
    font-weight: 600 !important;
    margin-top: 2rem !important;
    margin-bottom: 1rem !important;
}

/* Texto del sidebar */
.sidebar .stMarkdown {
    color: #4a5568 !important;
}

/* Nombre en el sidebar */
.sidebar h1 {
    color: #1a365d !important;
    font-size: 1.5rem !important;
    font-weight: 700 !important;
    margin-bottom: 0.5rem !important;
}

/* Estilizar los contenedores de experiencia */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    transition: all 0.3s ease;
    padding: 2rem !important;
    margin: 1rem 0 !important;
}

div[data-testid="stVerticalBlockBorderWrapper"]:hover {
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
    transform: translateY(-2px);
}

/* Información destacada */
.stAlert {
    background-color: #ebf8ff !important;
    border: 1px solid #90cdf4 !important;
    border-radius: 8px !important;
}

/* Botones */
button[kind="primary"] {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
    border: none !important;
    border-radius: 8px !important;
    color: white !important;
    font-weight: 600 !important;
    padding: 0.75rem 2rem !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 4px 6px -1px rgba(102, 126, 234, 0.3) !important;
}

button[kind="primary"]:hover {
    background: linear-gradient(135deg, #5a67d8 0%, #6b46c1 100%) !important;
    box-shadow: 0 10px 15px -3px rgba(102, 126, 234, 0.4) !important;
    transform: translateY(-1px) !important;
}

/* Enlaces */
a {
    color: #667eea !important;
    text-decoration: none !important;
    transition: color 0.3s ease !important;
}

a:hover {
    color: #5a67d8 !important;
    text-decoration: underline !important;
}

/* Lista de elementos */
ul {
    padding-left: 1.5rem !important;
}

li {
    margin-bottom: 0.5rem !important;
    line-height: 1.6 !important;
}

/* Código inline */
code {
    background-color: #f7fafc !important;
    color: #e53e3e !important;
    padding: 0.125rem 0.25rem !important;
    border-radius: 4px !important;
    font-size: 0.875rem !important;
}

/* Divisores */
hr {
    border: none !important;
    height: 1px !important;
    background: linear-gradient(90deg, transparent 0%, #e2e8f0 50%, transparent 100%) !important;
    margin: 2rem 0 !important;
}

/* Columnas de habilidades */
[data-testid="column"] {
    background: #ffffff;
    border-radius: 8px;
    padding: 1.5rem !important;
    box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1) !important;
    border: 1px solid #f1f5f9 !important;
}

</style>
""", unsafe_allow_html=True)


# --- BARRA LATERAL (SIDEBAR) ---
with st.sidebar:
    st.image("Imagen.jpeg", use_container_width=True)
    st.title("Jesús Pedro Rodríguez Castro")
    st.markdown("Scrum Master & Team Lead")
    
    st.divider()

    # --- INFORMACIÓN DE CONTACTO ---
    st.subheader("Contacto")
    st.markdown("""
    - **Email:** [jesusprodriguez@gmail.com](mailto:jesusprodriguez@gmail.com)
    - **LinkedIn:** [linkedin.com/in/jesus-pedro...](https://www.linkedin.com/in/jes%C3%BAs-pedro-rodr%C3%ADguez-castro-b746394a/)
    - **GitHub:** [github.com/jesusprodriguez](https://github.com/jesusprodriguez)
    - **Blog:** [blogpersonal.vercel.app](https://blogpersonal-eta.vercel.app/)
    - **Teléfono:** [+34 670 402 450](tel:+34670402450)
    - **Ubicación:** Madrid, España
    """)
    
    st.divider()
    
    # --- IDIOMAS ---
    st.subheader("Idiomas")
    st.markdown("""
    - **Español:** Nativo
    - **Inglés:** Profesional
    """)

# --- CONTENIDO PRINCIPAL ---

# --- PERFIL PROFESIONAL ---
st.header("Perfil Profesional", divider="gray")
st.info("""
**Scrum Master y Líder Técnico Senior** con más de 15 años de experiencia en desarrollo de software enterprise. 
Especialista en tecnologías .NET y Angular con certificación Scrum Master. He liderado equipos de hasta 12 desarrolladores, 
implementado pipelines CI/CD que han reducido el tiempo de deployment en un 75%, y desarrollado sistemas críticos 
que procesan más de €2M en transacciones mensuales. Comprometido con la excelencia técnica y el crecimiento profesional 
de los equipos que lidero.
""")

# --- EXPERIENCIA PROFESIONAL ---
st.header("Experiencia Profesional", divider="gray")

# --- EXPERIENCIA 1: UNIR ---
with st.container(border=True):
    st.subheader("Responsable de Scrum y Líder Técnico")
    st.markdown("**UNIR (La Universidad en Internet)** | Feb 2020 - Presente (5+ años) | Madrid")
    st.markdown("""
    • **Liderazgo de Equipo:** Gestiono equipo de 12 desarrolladores aplicando metodologías ágiles Scrum
    • **Mentoría:** Capacitación y mentoría a 8 equipos de desarrollo, mejorando productividad en 35%
    • **Arquitectura:** Desarrollo de aplicaciones complejas en ERP Académico con arquitectura DDD
    • **DevOps:** Implementación de GitFlow, Pull Requests y testing automatizado (cobertura 85%+)
    • **CI/CD:** Gestión de pipelines con TeamCity y Azure DevOps, 150+ deployments exitosos
    • **Soporte:** Desarrollo de soluciones urgentes y hotfixes con tiempo de respuesta <4 horas
    """)
    st.markdown("**Stack principal:** `Angular 18`, `.NET Core 8.0`, `Python`, `TeamCity`, `Azure DevOps`, `Docker`")

# --- EXPERIENCIA 2: SOTEC ---
with st.container(border=True):
    st.subheader("Analista .NET / Analista Funcional")
    st.markdown("**SOTEC CONSULTING** | Jun 2010 - Feb 2020 (9 años 9 meses) | Madrid")
    st.markdown("""
    • **Proyecto Crítico:** Desarrollo en proyecto Fiba Solar para Santander Consumer (€2M+ en transacciones mensuales)
    • **Resolución Técnica:** Solución de problemas complejos en sistemas legacy, reduciendo downtime en 60%
    • **Bases de Datos:** Optimización de consultas Oracle, mejorando rendimiento en 300%
    • **Desarrollo Web:** Mantenimiento y evolución de aplicaciones bancarias con 50.000+ usuarios activos
    • **Migración Tecnológica:** Migración exitosa de .NET Framework 1.1 a 4.0 sin pérdida de funcionalidad
    • **Arquitectura:** Implementación de inyección de dependencias y patrones de diseño enterprise
    • **Reporting:** Desarrollo de sistemas de reporting avanzados con Crystal Reports y SSRS
    """)
    st.markdown("**Stack principal:** `C#`, `ASP.NET`, `VB.NET`, `Oracle`, `Web Services`")


# --- PROYECTOS DESTACADOS ---
st.header("Proyectos Destacados", divider="gray")

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.subheader("🏛️ ERP Académico UNIR")
        st.markdown("**Tecnologías:** Angular 18, .NET Core 8.0, SQL Server")
        st.markdown("""
        • Desarrollo de plataforma educativa completa con arquitectura DDD
        • Implementación de microservicios y APIs RESTful
        • Gestión de +50.000 usuarios concurrentes
        • Reducción del tiempo de carga en un 40% mediante optimizaciones
        """)

    with st.container(border=True):
        st.subheader("🏦 Sistema Bancario Santander")
        st.markdown("**Tecnologías:** C#, ASP.NET, Oracle, Web Services")
        st.markdown("""
        • Desarrollo de aplicación financiera crítica para Santander Consumer
        • Procesamiento de transacciones por valor de €2M+ mensuales
        • Migración exitosa de .NET Framework 1.1 a 4.0
        • Implementación de alta disponibilidad 99.9% uptime
        """)

with col2:
    with st.container(border=True):
        st.subheader("🚀 CI/CD Pipeline Empresarial")
        st.markdown("**Tecnologías:** TeamCity, Azure DevOps, Docker, GitFlow")
        st.markdown("""
        • Diseño e implementación de pipeline de CI/CD completo
        • Automatización de testing y deployment para 15+ equipos
        • Reducción del tiempo de release de 2 semanas a 2 días
        • Implementación de blue-green deployments
        """)

    with st.container(border=True):
        st.subheader("📊 Dashboard Ejecutivo")
        st.markdown("**Tecnologías:** Python, FastAPI, Angular, Docker")
        st.markdown("""
        • Desarrollo de dashboard en tiempo real para KPIs empresariales
        • Procesamiento de datos de múltiples fuentes heterogéneas
        • Implementación de caching y optimizaciones de rendimiento
        • Visualización de métricas críticas para toma de decisiones
        """)


# --- ÚLTIMAS ENTRADAS DEL BLOG ---
st.header("Mi Blog Personal", divider="gray")

# IMPORTANTE: Revisa que esta URL sea la correcta para tu feed RSS.
# Puede ser /feed.xml, /rss.xml, o algo similar.
BLOG_FEED_URL = "https://blogpersonal-eta.vercel.app/feed.xml"

def clean_html(raw_html):
    """Limpia el HTML de las descripciones del RSS."""
    if not isinstance(raw_html, str):
        return ""
    cleantext = re.sub(re.compile('<.*?>'), '', raw_html)
    return cleantext

@st.cache_data(ttl=3600) # Cachea el resultado por 1 hora
def fetch_blog_posts(feed_url):
    """Obtiene las últimas 3 entradas del blog."""
    try:
        feed = feedparser.parse(feed_url)
        if feed.bozo:
            # En lugar de mostrar error, devolver lista vacía para mostrar mensaje alternativo
            return []
            
        posts = []
        # Obtenemos las 3 entradas más recientes
        for entry in feed.entries[:3]:
            summary = clean_html(entry.get("summary", "No hay descripción disponible."))
            posts.append({
                "title": entry.get("title", "Sin Título"),
                "link": entry.get("link", "#"),
                "summary": summary[:150] + "..." if len(summary) > 150 else summary # Acortar resumen
            })
        return posts
    except Exception as e:
        # Silenciar errores de red/conexión y devolver lista vacía
        return []

# Mostramos las entradas del blog
blog_posts = fetch_blog_posts(BLOG_FEED_URL)

if blog_posts:
    for post in blog_posts:
        st.subheader(f"[{post['title']}]({post['link']})")
        st.write(post['summary'])
else:
    st.info("""
    📝 **Mi blog está disponible en:** [blogpersonal.vercel.app](https://blogpersonal-eta.vercel.app/)
    
    Actualmente no hay un feed RSS activo, pero puedes visitar mi blog directamente para leer mis últimas publicaciones sobre desarrollo de software, tecnologías y mejores prácticas.
    """)
    st.caption(f"URL del blog: `{BLOG_FEED_URL.replace('/feed.xml', '')}`")


# --- COMPETENCIAS TÉCNICAS ---
st.header("Competencias Técnicas", divider="gray")

# Nivel de experiencia
st.subheader("💡 Nivel de Dominio")

# Función para crear barras de progreso
def skill_progress(skill, level, color="#667eea"):
    """Crea una barra de progreso para una habilidad."""
    percentage = {"Principiante": 25, "Intermedio": 50, "Avanzado": 75, "Experto": 100}[level]
    st.markdown(f"""
    <div style="display: flex; align-items: center; margin-bottom: 0.5rem;">
        <div style="width: 120px; font-weight: 500; color: #4a5568;">{skill}</div>
        <div style="flex: 1; background-color: #e2e8f0; border-radius: 4px; height: 8px; margin: 0 1rem;">
            <div style="width: {percentage}%; background-color: {color}; height: 100%; border-radius: 4px; transition: width 0.3s ease;"></div>
        </div>
        <div style="width: 80px; text-align: right; color: #718096; font-size: 0.875rem;">{level}</div>
    </div>
    """, unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("**🚀 Tecnologías Principales**")
    skill_progress("Angular", "Experto", "#dd6b20")
    skill_progress(".NET Core", "Experto", "#3182ce")
    skill_progress("C#", "Experto", "#2d3748")
    skill_progress("Python", "Avanzado", "#38a169")
    skill_progress("SQL Server", "Avanzado", "#3182ce")
    skill_progress("Docker", "Avanzado", "#319795")

with col2:
    st.markdown("**🛠️ Herramientas & Metodologías**")
    skill_progress("Scrum", "Experto", "#805ad5")
    skill_progress("Azure DevOps", "Avanzado", "#3182ce")
    skill_progress("Git", "Experto", "#e53e3e")
    skill_progress("TeamCity", "Avanzado", "#38a169")
    skill_progress("Oracle", "Avanzado", "#dd6b20")
    skill_progress("CI/CD", "Experto", "#805ad5")

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("🎨 Frontend")
    st.markdown("""
    - **Angular 18** - Framework SPA avanzado
    - **JavaScript/TypeScript** - ES6+, módulos
    - **HTML5/CSS3** - Responsive design
    - **RxJS** - Programación reactiva
    """)

with col2:
    st.subheader("⚙️ Backend")
    st.markdown("""
    - **.NET Core 8.0** - APIs RESTful, microservicios
    - **C#** - LINQ, async/await, generics
    - **Python** - FastAPI, data processing
    - **ASP.NET MVC** - Web applications
    - **Web Services** - SOAP, REST, GraphQL
    """)

with col3:
    st.subheader("🗄️ DevOps & DB")
    st.markdown("""
    - **SQL Server/Oracle** - PL/SQL, optimización
    - **TeamCity/Azure DevOps** - CI/CD pipelines
    - **Docker** - Containerización
    - **GitFlow** - Branching strategy
    - **Monitoring** - Application Insights
    """)

# --- METODOLOGÍAS Y HERRAMIENTAS ---
st.subheader("🎯 Metodologías & Enfoques")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    **📋 Metodologías Ágiles**
    - **Scrum Master Certified** - Gestión de equipos ágiles
    - **Kanban** - Flujo de trabajo optimizado
    - **XP (eXtreme Programming)** - Prácticas de desarrollo
    - **TDD/BDD** - Desarrollo guiado por pruebas
    """)

with col2:
    st.markdown("""
    **🛠️ Herramientas de Productividad**
    - **GitHub Copilot** - IA para desarrollo acelerado
    - **JIRA/Confluence** - Gestión de proyectos
    - **Postman** - Testing de APIs
    - **Figma/Miro** - Diseño y colaboración
    """)


# --- LOGROS Y RECONOCIMIENTOS ---
st.header("🏆 Logros y Reconocimientos", divider="gray")

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.markdown("**🚀 Impacto Empresarial**")
        st.markdown("""
        • Reducción del tiempo de deployment de 2 semanas a 2 días
        • Implementación de CI/CD que soporta 150+ releases mensuales
        • Optimización de rendimiento que mejoró la experiencia de usuario en 40%
        • Desarrollo de sistemas con 99.9% de uptime en entornos críticos
        """)

with col2:
    with st.container(border=True):
        st.markdown("**👥 Liderazgo y Mentoría**")
        st.markdown("""
        • Mentoría a 8 equipos de desarrollo, mejorando productividad en 35%
        • Capacitación en metodologías ágiles a más de 50 profesionales
        • Implementación exitosa de Scrum en proyectos enterprise
        • Reconocimiento como Scrum Master certificado
        """)


# --- EDUCACIÓN Y CERTIFICACIONES ---
st.header("Educación y Certificaciones", divider="gray")

st.subheader("Educación")
st.markdown("Master en Bases de Datos - *Microforum (2001-2002)*")

st.subheader("Certificaciones")
st.markdown("""
- Microsoft Certified: Azure Fundamentals
- MCP 70-229: Designing and Implementing Databases with SQL Server 2000
- 70-515 TS: Web Applications Development with .NET Framework 4
""")

st.divider()

# --- FORMULARIO DE CONTACTO ---
st.header("Contacto Directo", divider="gray")
st.write("¿Interesado en mi perfil? Envíame un mensaje.")

# Usamos st.form para agrupar los campos
with st.form("contact_form", clear_on_submit=True):
    name = st.text_input("Tu Nombre", placeholder="Juan Pérez")
    email = st.text_input("Tu Email", placeholder="juan.perez@email.com")
    message = st.text_area("Tu Mensaje", placeholder="Me gustaría contactar contigo para...")
    
    # Botón de envío del formulario
    submitted = st.form_submit_button("Enviar Mensaje")
    
    if submitted:
        # Validación simple
        if name and email and message:
            # En un proyecto real, aquí es donde enviarías el email.
            # Podrías usar st.secrets para las credenciales SMTP
            # o un servicio de terceros como FormSubmit.
            
            # Por ahora, solo mostramos un mensaje de éxito.
            st.success(f"¡Gracias por tu mensaje, {name}! Te responderé pronto a {email}.")
        else:
            st.error("Por favor, completa todos los campos del formulario.")