from dataclasses import dataclass
import uuid

CHARACTERS = dict()


def create_character(mana_total):
    character_id = uuid.uuid4()
    CHARACTERS[character_id] = Character(mana_total, mana_total, character_id)
    return CHARACTERS[character_id]


def use_magic(character_id, spell_level):
    character = CHARACTERS[character_id]
    character.mana -= spell_level
    return character.mana


@dataclass
class Character:
    mana: int
    mana_total: int
    character_id: uuid
