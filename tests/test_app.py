import pytest
from src.utils.formatting import clean_html

def test_clean_html():
    raw_html = "<p>This is <b>bold</b> text.</p>"
    cleaned = clean_html(raw_html)
    assert cleaned == "This is bold text."

def test_clean_html_empty():
    assert clean_html("") == ""

def test_clean_html_none():
    assert clean_html(None) == ""
