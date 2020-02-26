import unittest
import shiritori_game


class TestShiritoriGame(unittest.TestCase):

    def setUp(self):
        self.game = shiritori_game.Shiritori()

    def tearDown(self):
        self.game.restart()

    def test_normal_play(self):
        # Test rule 1: letters match
        self.game.play("hello")
        self.assertEqual(self.game.play("octopus"), ["hello", "octopus"])
        self.assertEqual(self.game.play("silly"), ["hello", "octopus", "silly"])

    def test_break_rule_1(self):
        # Test breaking rule 1: letters don't match
        self.game.play("hello")
        self.assertEqual(self.game.play("world"), "game over")
        self.assertEqual(self.game.game_over, True)

    def test_break_rule_2(self):
        # Test breaking rule 2: repeated word
        self.game.play("hello")
        self.assertEqual(self.game.play("hello"), "game over")
        self.assertEqual(self.game.game_over, True)


if __name__ == '__main__':
    unittest.main()
