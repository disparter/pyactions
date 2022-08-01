def get_current_mana_after_spell(user_character, spell_level):
    user_character.mana -= spell_level
    return user_character.mana

