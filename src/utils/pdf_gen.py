from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Logo (if exists)
        # self.image('Imagen.jpeg', 10, 8, 33)
        # Font
        self.set_font('Helvetica', 'B', 15)
        # Title
        self.cell(0, 10, 'Jesus Pedro Rodriguez Castro', align='C', new_x="LMARGIN", new_y="NEXT")
        self.set_font('Helvetica', 'I', 10)
        self.cell(0, 5, 'Scrum Master & Team Lead', align='C', new_x="LMARGIN", new_y="NEXT")
        self.ln(10)

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', align='C')

    def chapter_title(self, label):
        self.set_font('Helvetica', 'B', 12)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 6, label, fill=True, new_x="LMARGIN", new_y="NEXT")
        self.ln(4)

    def chapter_body(self, body):
        self.set_font('Helvetica', '', 10)
        self.multi_cell(0, 5, body)
        self.ln()

def sanitize_text(text):
    """Replace unsupported characters."""
    if isinstance(text, str):
        return text.replace("€", "EUR").replace("–", "-").replace("’", "'").replace("“", '"').replace("”", '"')
    return text

def create_pdf(profile_data):
    pdf = PDF()
    pdf.add_page()
    
    # Contact Info
    pdf.set_font('Helvetica', '', 9)
    pdf.cell(0, 5, f"Email: {profile_data.get('email', '')} | Phone: {profile_data.get('phone', '')}", align='C', new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 5, f"Location: {sanitize_text(profile_data.get('location', ''))}", align='C', new_x="LMARGIN", new_y="NEXT")
    pdf.ln(5)

    # Profile
    pdf.chapter_title('Professional Profile')
    pdf.chapter_body(sanitize_text(profile_data.get('summary', '')))

    # Experience
    pdf.chapter_title('Experience')
    for exp in profile_data.get('experience', []):
        pdf.set_font('Helvetica', 'B', 10)
        pdf.cell(0, 5, f"{sanitize_text(exp['role'])} at {sanitize_text(exp['company'])}", new_x="LMARGIN", new_y="NEXT")
        pdf.set_font('Helvetica', 'I', 9)
        pdf.cell(0, 5, f"{sanitize_text(exp['period'])} | {sanitize_text(exp['location'])}", new_x="LMARGIN", new_y="NEXT")
        pdf.set_font('Helvetica', '', 9)
        pdf.multi_cell(0, 5, sanitize_text(exp['description']))
        pdf.ln(2)

    # Skills
    pdf.chapter_title('Skills')
    pdf.set_font('Helvetica', '', 9)
    skills_text = ", ".join(profile_data.get('skills', []))
    pdf.multi_cell(0, 5, skills_text)
    
    return pdf.output()
