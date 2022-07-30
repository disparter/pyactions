import json


def get_mana(spell_name, dnd_class):
    spells = json.load(open('spells.json'))
    return spells[spell_name][dnd_class]

