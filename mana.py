from character import CHARACTERS


def get_current_mana_after_spell(character_id, spell_level):
    character = CHARACTERS[character_id]
    character.mana -= spell_level
    return character.mana

