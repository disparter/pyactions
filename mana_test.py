import unittest

import mana
import spell
import character


class ManaTestCase(unittest.TestCase):
    def test_Decrease_Mana(self):
        # given
        expected = 22
        random_character = character.create_character(30, 'gandalf', 'wizard')
        spell_slot = 8

        # when
        result = mana.get_current_mana_after_spell(random_character, spell_slot)

        # then
        self.assertEqual(expected, result)

    def test_Decrease_Mana_FireballAndSorcerer(self):
        # given
        expected = 37
        character_class = 'sorcerer'
        random_character = character.create_character(40, 'skeletor', character_class)
        spell_name = 'fireball'

        # when
        spell_slot = spell.get_mana(spell_name=spell_name, dnd_class=character_class)
        result = mana.get_current_mana_after_spell(random_character, spell_slot)

        # then
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
