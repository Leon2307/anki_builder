import argparse
import anki
import word
import test_alternative

if __name__ == "__main__":

    """Config file and deck name as terminal argument"""
    parser = argparse.ArgumentParser()
    parser.add_argument('--docx_path', required=True)
    parser.add_argument('--deck_name', required=True)
    args = parser.parse_args()

    """Gets the headers and subsection as a dictionary from a word file"""
    section_text = test_alternative.get_paragraphes(args.docx_path)

    """Convert dictionary to Anki file"""
    anki.dict_to_anki(section_text, args.deck_name)
