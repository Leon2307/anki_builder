import argparse
import src.anki as anki
import src.word as word
import yaml

if __name__ == "__main__":

    """Config file and deck name as terminal argument"""
    parser = argparse.ArgumentParser()
    parser.add_argument('--docx_path', required=True)
    parser.add_argument('--deck_name', required=True)
    args = parser.parse_args()

    """Loading Settings from settings.yaml"""
    with open("settings.yaml", 'r') as stream:
        settings = yaml.safe_load(stream)

    """Gets the headers, images and subsection as a dictionary from a word file"""
    text_dict = word.get_paragraphes(args.docx_path, settings)

    """Convert dictionary to Anki file"""
    anki.dict_to_anki(text_dict, args.deck_name, settings)
