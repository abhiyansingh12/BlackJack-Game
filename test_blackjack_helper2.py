from blackjack_helper2 import *
from test_helper import *
import unittest

class TestBlackjackHelper(unittest.TestCase):
  """
  Class for testing blackjack helper functions.
  """

  def test_print_card_name_example(self):
    """
    Example of a test to compare printed statements with expected

    This does not count as one of your tests
    """
    self.assertEqual(get_print(print_card_name, 2), "Drew a 2\n")

  def test_mock_randint_example(self):
    """
    Example of a test to compare output for a function that calls randint

    This does not count as one of your tests
    """
    self.assertEqual(mock_random([3], draw_card), 3)
    self.assertEqual(mock_random([3, 5], draw_starting_hand, "DEALER"), 8)

  
  def test_print_card_name(self):
     self.assertEqual(get_print(print_card_name, 12), "Drew a Queen\n")
     self.assertEqual(get_print(print_card_name, 15), "BAD CARD\n")
     self.assertEqual(get_print(print_card_name, 1), "Drew an Ace\n")
     self.assertEqual(get_print(print_card_name, 3), "Drew a 3\n")
  
  def test_draw_card(self):
     self.assertEqual(mock_random([12],draw_card), 10)
     self.assertEqual(mock_random([1],draw_card), 11)
     self.assertEqual(mock_random([6],draw_card), 6)
     self.assertEqual(mock_random([13],draw_card), 10)

  def test_print_header(self):
    expected_output = '-----------\nTest\n-----------\n'
    self.assertEqual(get_print(print_header, 'Test'), expected_output)
  
  def test_draw_starting_hand(self):
    mock_value = [2, 7]
    expected_output = 9
    self.assertEqual(mock_random(mock_value, draw_starting_hand, 'YOUR' ), expected_output)
    self.assertEqual(mock_random([1,6], draw_starting_hand, "DEALER"), 17)
  
  def test_print_end_turn_status(self):
    expected_output = 'Final hand: 23.\nBUST.\n'
    self.assertEqual(get_print(print_end_turn_status, 23), expected_output)
    expected_output = 'Final hand: 21.\nBLACKJACK!\n'
    self.assertEqual(get_print(print_end_turn_status, 21), expected_output)

  def test_print_end_game_status(self):
    expected_output = '-----------\nGAME RESULT\n-----------\nDealer wins!\n'
    self.assertEqual(get_print(print_end_game_status, 18, 21), expected_output)
    expected_output = '-----------\nGAME RESULT\n-----------\nDealer wins!\n'
    self.assertEqual(get_print(print_end_game_status, 25, 21), expected_output)
    expected_output = '-----------\nGAME RESULT\n-----------\nDealer wins!\n'
    self.assertEqual(get_print(print_end_game_status, 24, 19), expected_output)
    expected_output = '-----------\nGAME RESULT\n-----------\nPush.\n'
    self.assertEqual(get_print(print_end_game_status, 16, 16), expected_output)
    expected_output = '-----------\nGAME RESULT\n-----------\nPush.\n'
    self.assertEqual(get_print(print_end_game_status, 21, 21), expected_output)
    expected_output = '-----------\nGAME RESULT\n-----------\nYou win!\n'
    self.assertEqual(get_print(print_end_game_status, 19, 23), expected_output)
    expected_output = '-----------\nGAME RESULT\n-----------\nYou win!\n'
    self.assertEqual(get_print(print_end_game_status, 21, 17), expected_output)
if __name__ == '__main__':
    unittest.main()