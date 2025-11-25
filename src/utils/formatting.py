import re

def clean_html(raw_html):
    """Limpia el HTML de las descripciones del RSS."""
    if not isinstance(raw_html, str):
        return ""
    cleantext = re.sub(re.compile('<.*?>'), '', raw_html)
    return cleantext
