import genanki
import random

text_model = genanki.Model(
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

image_model = genanki.Model(
  1091735104,
  'Simple Model with Images',
  fields=[
    {'name': 'Question'},
    {'name': 'Answer'},
    {'name': 'MyMedia1'},
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '{{Question}}',
      'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}<br>{{MyMedia1}}',
    },
  ])

def dict_to_anki(dict,deck_name, settings):
    """Generates an anki deck with cards from dictionary and exports it as an apkg"""
    my_deck = genanki.Deck(
        random.randrange(1 << 30, 1 << 31),
        deck_name
    )
    for card in dict:
        my_note = None
        if not (card['images'] == []):
          field = [card['title'],card['text']]
          field.append('<img src="{}">'.format(card["images"][0]))
          my_note = genanki.Note(
          model=image_model,
          fields=field
          )

        else:
          my_note = genanki.Note(
              model=text_model,
              fields=[card['title'],card['text']]
          )
        my_deck.add_note(my_note)
      
    my_package = genanki.Package(my_deck)
    my_package.media_files = get_media_files(dict, settings["abs_path_img"])
    my_package.write_to_file("{}/{}.apkg".format(settings['output_path'], deck_name))
    return 


def get_media_files(dict, abs_path):
    files = []
    for i in dict:
        for j in i['images']:
            files.append('{}{}'.format(abs_path, j))
            
    return files