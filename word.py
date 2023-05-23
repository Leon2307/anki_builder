import zipfile    
import xml.etree.ElementTree as ET

ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}

def get_text(docx_path):
    """Loading Word document and converting to XML"""
    file_path = docx_path
    doc = zipfile.ZipFile(file_path).read('word/document.xml')
    root = ET.fromstring(doc)
    f= open("document.xml", "w")
    f.write(str(doc))

    """Get text sections from XML file"""
    body = root.find('w:body', ns)
    p_sections = body.findall('w:p', ns)

    """Get text in each section"""
    text_elems = []
    for p in p_sections:
        text_elems.append(p.findall('.//w:t', ns))
        print([t.text for t in p])
        print()

    """Differentiating between header and subsection"""
    section_labels = [get_section_text(s,text_elems) if is_heading2_section(s) else '' for s in p_sections]
    section_text = [{"title": t, "text": get_section_text(p_sections[i+1],text_elems)} for i, t in enumerate(section_labels) if len(t) > 0]
    return section_text

def is_heading2_section(p):
    """Returns True if the given paragraph section has been styled as a Heading2"""
    return_val = False
    heading_style_elem = p.find(".//w:pStyle[@w:val='Heading2']", ns)
    if heading_style_elem is not None:
        return_val = True
    return return_val
 
 
def get_section_text(p, text_elems):
    """Returns the joined text of the text elements under the given paragraph tag"""
    return_val = ''
    text_elems = p.findall('.//w:t', ns)
    if text_elems is not None:
        return_val = ''.join([t.text for t in text_elems])
    return return_val
