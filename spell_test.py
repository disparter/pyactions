import unittest
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


if __name__ == '__main__':
    unittest.main()
