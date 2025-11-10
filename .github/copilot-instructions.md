# Copilot Instructions - Resume App

## Project Overview

This is a **professional Streamlit-based interactive resume/CV application** for Jesús Pedro Rodríguez Castro. The entire application is contained in a single `app.py` file that renders a modern, professional web-based curriculum vitae with advanced styling and interactive elements.

## Architecture

- **Single-file application**: All code lives in `app.py`
- **Framework**: Streamlit (Python web app framework)
- **Layout**: Wide mode with sidebar navigation
- **Design**: Modern professional styling with custom CSS, gradients, and animations
- **Interactive elements**: RSS blog feed integration, contact form, skill progress bars

## Key Patterns

### Page Configuration
The app uses `st.set_page_config()` at the top with:
- Wide layout for better space utilization
- Custom page title and icon
- Expanded sidebar by default

### Content Structure
The app follows this professional layout pattern:
1. **Sidebar** (`with st.sidebar:`): Professional photo, contact info, languages
2. **Main content**: Professional sections in optimal order:
   - Professional Profile (summary with key metrics)
   - Professional Experience (detailed with quantifiable achievements)
   - Featured Projects (specific project highlights with metrics)
   - Blog Feed (latest posts from RSS)
   - Technical Skills (visual progress bars + categorized lists)
   - Achievements & Recognition (professional accomplishments)
   - Education & Certifications (academic background)
   - Contact Form (interactive contact functionality)

### Advanced Styling Patterns
- **Custom CSS**: Professional color scheme with Inter font family
- **Gradient backgrounds**: Subtle gradients for containers and buttons
- **Hover effects**: Smooth transitions and shadow effects
- **Progress bars**: Custom skill level visualization
- **Icon integration**: Emojis and visual elements for better UX
- **Responsive columns**: 2-3 column layouts for optimal space usage

### Content Enhancement Patterns
- **Quantifiable achievements**: All experience entries include specific metrics and impact
- **Professional terminology**: Industry-standard language and certifications
- **Visual hierarchy**: Clear section separation with dividers and containers
- **Action-oriented descriptions**: Bullet points starting with strong verbs
- **Technology stack highlighting**: Code-formatted tech stack references

## Professional Sections

The CV includes these main sections in professional order:
1. **Perfil Profesional**: Executive summary with key qualifications and metrics
2. **Experiencia Profesional**: Detailed work history with quantifiable achievements
3. **Proyectos Destacados**: Featured projects with specific impact metrics
4. **Mi Blog Personal**: RSS feed integration showing latest technical posts
5. **Competencias Técnicas**: Visual skill assessment with progress bars and categorized lists
6. **Logros y Reconocimientos**: Professional achievements and leadership impact
7. **Educación y Certificaciones**: Academic background and professional certifications
8. **Contacto Directo**: Interactive contact form for professional inquiries

## Language & Localization

- **Primary language**: Spanish (ES)
- All content labels, descriptions, and UI text are in Spanish
- Professional terminology appropriate for Spanish-speaking markets
- Contact links use Spanish format for phone numbers and locations

## Advanced Features

- **RSS Blog Integration**: Automatic fetching of latest blog posts with error handling
- **Interactive Contact Form**: Form validation and success messaging
- **Skill Progress Visualization**: Custom progress bars for technical competencies
- **Responsive Design**: Optimized for different screen sizes
- **Professional Color Scheme**: Modern blue/purple gradient theme
- **Hover Animations**: Interactive elements with smooth transitions

## Running the Application

```bash
streamlit run app.py
```

The app will launch in a web browser, typically at `http://localhost:8501`

## Dependencies

Required packages (install with pip):
- `streamlit`: Web framework
- `feedparser`: RSS feed parsing for blog integration

## Maintenance Guidelines

When updating this professional CV:
- **Quantify achievements**: Always include specific metrics and impact measurements
- **Maintain professional tone**: Use industry-standard terminology and certifications
- **Update metrics regularly**: Keep quantifiable achievements current
- **Test visual elements**: Ensure progress bars and styling work across devices
- **Keep content concise**: Focus on most impactful achievements and skills
- **Update blog RSS URL**: Verify the feed URL remains active
- **Maintain responsive design**: Test column layouts on different screen sizes

## Content Update Patterns

- **Experience entries**: Start with role impact, include team size, quantifiable results
- **Project highlights**: Focus on business impact, technical challenges overcome, results achieved
- **Skills assessment**: Use progress bars for current proficiency levels
- **Blog integration**: Automatically pulls latest technical content
- **Contact form**: Includes validation and professional success messaging

No other frameworks, databases, or external services are required beyond the RSS feed.
