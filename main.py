import argparse
import anki
import word

if __name__ == "__main__":

    """Config file as terminal argument"""
    parser = argparse.ArgumentParser()
    parser.add_argument('--docx_path', required=True)
    parser.add_argument('--deck_name', required=True)
    args = parser.parse_args()

    """Gets the headers and subsection from a word file"""
    section_text = word.get_section_text(args)

    """Convert dictionary file to Anki file"""
    anki.dict_to_anki(section_text, args.deck_name)
