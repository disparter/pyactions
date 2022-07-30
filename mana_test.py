import unittest
import mana


class ManaTestCase(unittest.TestCase):
    def test_Decrease_Mana(self):
        # given
        expected = 22
        character = mana.create_character(30)
        magic_circle = 8

        # when
        result = mana.use_magic(character.character_id, magic_circle)

        # then
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
