from docx.api import Document
import docx2txt as d2t
import logging

def get_paragraphes(doc, settings):
    """Gets all paragraphes from the doc and returns a dictionary with 
    {"title": ..., "text": ...}"""

    document = Document(doc)
    text = []
    image_count = 1
    logging.info("Reading Text from document...")
    for paragraph in document.paragraphs:
        if paragraph.style.name == settings['heading_style']:
            text.append({"title":paragraph.text, "text":"", "images":[]})
            continue
        elif paragraph.style.name.startswith("Heading"):
            continue
        length = len(text)
        if length < 1:
            continue
        if not (paragraph.text == ""):
            text[length-1]["text"] += '<li>' + paragraph.text
        if has_image(paragraph):
            text[length-1]["images"].append(image_count)
            image_count += 1
    
    extract_images_from_docx(doc, 'images/')
    text = match_images_with_text(text)
    return text

def match_images_with_text(dict):
    for card in dict:
        if card["images"] == []:
            continue
        for i in range(len(card["images"])):
            card['images'][i] = 'image{}.png'.format(card['images'][i])
    return dict

def has_image(paragraph):
    if 'graphicData' in paragraph._p.xml:
        return True
    return False

def extract_images_from_docx(file_path, img_folder, get_text=False):
    """Gets all the images included in the Word document and saves them to the img_folder"""
    logging.info("Extracting images from document...")
    text = d2t.process(file_path, img_folder)

    if(get_text):
        return text