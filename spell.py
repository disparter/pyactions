import json


def get_mana(spell_name, dnd_class):
    spells = json.load(open(dnd_class + '.json'))

    for spell in spells:
        if spell['spell_name'] == spell_name:
            return spell['spell_level']

    raise Exception("Spell not found")
