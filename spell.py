import json


def get_mana(spell_name, dnd_class):
    spells = json.load(open('spells.json'))
    for spell in spells:
        if spell['Spell name'] == spell_name:
            return spell[dnd_class]

    raise Exception("Spell not found")



