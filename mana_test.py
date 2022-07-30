import unittest
import mana
import uuid


class ManaTestCase(unittest.TestCase):
    def test_decreaseMana(self):
        # given
        expected = 22
        character_id = uuid.uuid4()
        magic_circle = 8

        # when
        result = mana.useMagic(character_id, magic_circle)

        # then
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
