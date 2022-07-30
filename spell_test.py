import unittest

import pytest

import spell


class SpellTestCase(unittest.TestCase):
    def test_Spell_Mana(self):
        #given
        SPELL_NAME = 'Aberrate'
        DND_CLASS = 'Wizard'
        EXPECTED = 1

        #when
        result = spell.get_mana(SPELL_NAME, DND_CLASS)

        #then
        self.assertEqual(EXPECTED, result)

    @pytest.mark.xfail(raises=Exception('Spell not found'))
    def test_Invalid_Spell(self):
        #given
        SPELL_NAME = 'Super Spell'
        DND_CLASS = 'Wizard'

        #when
        with pytest.raises(Exception) as exec_info:
            spell.get_mana(SPELL_NAME, DND_CLASS)



if __name__ == '__main__':
    unittest.main()
