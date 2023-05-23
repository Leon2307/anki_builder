from docx.api import Document

def get_paragraphes(doc, settings):
    """Gets all paragraphes from the doc and returns a dictionary with 
    {"title": ..., "text": ...}"""

    document = Document(doc)
    text = []
    for paragraph in document.paragraphs:
        if paragraph.style.name == settings['heading_style']:
            text.append({"title":paragraph.text, "text":""})
            continue
        elif paragraph.style.name.startswith("Heading"):
            continue
        length = len(text)
        if length > 0 and not (paragraph.text == ""):
            text[length-1]["text"] += '<li>' + paragraph.text
        
    return text