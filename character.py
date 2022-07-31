from dataclasses import dataclass
import uuid

CHARACTERS = dict()


def create_character(mana_total, character_name, dnd_class):
    character_id = uuid.uuid4()
    CHARACTERS[character_id] = Character(mana_total, mana_total, character_id, character_name, dnd_class)
    return CHARACTERS[character_id]


def get_dnd_class(character_name):
    for character in CHARACTERS:
        if character['character_name'].casefold() == character_name.casefold():
            return character['dnd_class']


def get_character_id(character_name):
    for character in CHARACTERS:
        if character['character_name'].casefold() == character_name.casefold():
            return character['character_id']


@dataclass
class Character:
    mana: int
    mana_total: int
    character_id: uuid
    character_name: str
    dnd_class: str
