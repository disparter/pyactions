from dataclasses import dataclass
import uuid

CHARACTERS = []


def create_character(mana_total: int, character_name, dnd_class):
    character_id = uuid.uuid4()
    created_character = Character(mana_total, mana_total, character_id, character_name, dnd_class)
    CHARACTERS.append(created_character)
    return created_character


def get_dnd_class(character_name):
    user_character = get_user_character(character_name)
    return user_character.dnd_class


def get_user_character(character_name):
    for character in CHARACTERS:
        if character.character_name.casefold() == character_name.casefold():
            return character
    raise Exception()


@dataclass
class Character:
    mana: int
    mana_total: int
    character_id: uuid
    character_name: str
    dnd_class: str
