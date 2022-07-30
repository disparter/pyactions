import json


def get_mana(spell_name, dnd_class):
    spells = json.load(open(dnd_class + '.json'))

    for spell in spells:
        if spell['Spell name'] == spell_name:
            return spell['Circle']

    raise Exception("Spell not found")
