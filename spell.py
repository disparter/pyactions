import json


def get_mana(spell_name, dnd_class):
    spells = json.load(open(f'data/{dnd_class}.json'))

    for spell in spells:
        if spell['spell_name'].casefold() == spell_name.casefold():
            return spell['spell_level']

    raise Exception("Spell not found")
