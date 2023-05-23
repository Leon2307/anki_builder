from docx.api import Document

def get_paragraphes(doc):
    """Gets all paragraphes from the doc and returns a dictionary with 
    {"title": ..., "text": ...}"""
    document = Document(doc)
    
    text = []

    for paragraph in document.paragraphs:
        if paragraph.style.name == 'Heading 2':
            text.append({"title":paragraph.text, "text":""})
            continue
        elif paragraph.style.name.startswith("Heading"):
            continue

        if(len(text) > 0):
            text[len(text)-1]["text"] += "\n" + paragraph.text
        
    return text

if __name__ == '__main__':
    get_paragraphes('word/Test for Anki.docx')