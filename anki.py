import genanki
import random

my_model = genanki.Model(
  1607392319,
  'Leons Model',
  fields=[
    {'name': 'Question'},
    {'name': 'Answer'},
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '{{Question}}',
      'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
    },
  ])


def dict_to_anki(section_text,deck_name):
    """Generates an anki deck with cards from dictionary and exports it as an apkg"""
    my_deck = genanki.Deck(
        random.randrange(1 << 30, 1 << 31),
        deck_name
    )

    for card in section_text:
        print(card)
        my_note = genanki.Note(
            model=my_model,
            fields=[card['title'],card['text']]
        )
        my_deck.add_note(my_note)
    genanki.Package(my_deck).write_to_file("output_files/{}.apkg".format(deck_name))
    return 
