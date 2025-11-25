import pytest
from src.utils.pdf_gen import create_pdf

def test_create_pdf():
    profile_data = {
        "name": "Test User",
        "role": "Test Role",
        "email": "test@example.com",
        "phone": "123456789",
        "location": "Test Location",
        "summary": "Test Summary with special char €",
        "experience": [
            {
                "role": "Role 1",
                "company": "Company 1",
                "period": "2020-2021",
                "location": "Loc 1",
                "description": "Desc 1"
            }
        ],
        "skills": ["Skill 1", "Skill 2"]
    }
    
    pdf_bytes = create_pdf(profile_data)
    print(f"DEBUG: Type of pdf_bytes is {type(pdf_bytes)}")
    assert isinstance(pdf_bytes, (bytes, bytearray))
    assert len(pdf_bytes) > 0
