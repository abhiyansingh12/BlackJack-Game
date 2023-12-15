from unittest import TestCase, main
from unittest.mock import patch
from test_helper import run_test

class TestBlackjack(TestCase):

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_example(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand less than 21.
        The dealer wins by having a higher hand than the user.

        This does not count as one of your tests.
        '''
        output = run_test([3, 5, 8], ['y', 'n'], [3, 5, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "You have 8. Hit (y/n)? y\n" \
                   "Drew an 8\n" \
                   "You have 16. Hit (y/n)? n\n" \
                   "Final hand: 16.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "Dealer has 8.\n" \
                   "Drew a 10\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

    # Make sure all your test functions start with test_ 
    # Follow indentation of test_example
    # WRITE ALL YOUR TESTS BELOW. Do not delete this line.
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_wins1(self,input_mock, randint_mock):

        '''
            Both the user and dealer gets card value less than 21 but
            since user's hand value is more than dealer so user wins.
        '''
        
        output = run_test([11,13], ['n'], [7, 5, 6], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a Jack\n" \
                   "Drew a King\n" \
                   "You have 20. Hit (y/n)? n\n" \
                   "Final hand: 20.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 7\n" \
                   "Drew a 5\n" \
                   "Dealer has 12.\n" \
                   "Drew a 6\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)
    
   
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_wins2(self,input_mock, randint_mock):

        '''
         User gets less than 21 while the dealer gets more than 21, 
         thus the user wins as dealer busts  
        '''
        
        output = run_test([6,8,6], ['y','n'], [13,5,8], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 6\n" \
                   "Drew an 8\n" \
                   "You have 14. Hit (y/n)? y\n" \
                   "Drew a 6\n" \
                   "You have 20. Hit (y/n)? n\n" \
                   "Final hand: 20.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a King\n" \
                   "Drew a 5\n" \
                   "Dealer has 15.\n" \
                   "Drew an 8\n" \
                   "Final hand: 23.\n" \
                   "BUST.\n"\
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_wins3(self, input_mock, randint_mock):
     '''
      Dealer draws less than 21 while
      User gets 21 and hits a BLACKJACK
     '''

     output = run_test([8, 11, 3], ['y'], [7, 6, 5], randint_mock, input_mock)
     expected = "-----------\n" \
               "YOUR TURN\n" \
               "-----------\n" \
               "Drew an 8\n" \
               "Drew a Jack\n" \
               "You have 18. Hit (y/n)? y\n" \
               "Drew a 3\n" \
               "Final hand: 21.\n" \
               "BLACKJACK!\n" \
               "-----------\n" \
               "DEALER TURN\n" \
               "-----------\n" \
               "Drew a 7\n" \
               "Drew a 6\n" \
               "Dealer has 13.\n" \
               "Drew a 5\n" \
               "Final hand: 18.\n" \
               "-----------\n" \
               "GAME RESULT\n" \
               "-----------\n" \
               "You win!\n"
     self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_wins4(self, input_mock, randint_mock):
     '''
        Both the dealer and user receive cards that end up with a hand less than 21.
        The user wins by having a higher hand than the dealer.
     '''

     output = run_test([5, 7, 7], ['y', 'n'], [12, 8], randint_mock, input_mock)
     expected = "-----------\n" \
               "YOUR TURN\n" \
               "-----------\n" \
               "Drew a 5\n" \
               "Drew a 7\n" \
               "You have 12. Hit (y/n)? y\n" \
               "Drew a 7\n" \
               "You have 19. Hit (y/n)? n\n" \
               "Final hand: 19.\n" \
               "-----------\n" \
               "DEALER TURN\n" \
               "-----------\n" \
               "Drew a Queen\n" \
               "Drew an 8\n" \
               "Final hand: 18.\n" \
               "-----------\n" \
               "GAME RESULT\n" \
               "-----------\n" \
               "You win!\n"
     self.assertEqual(output, expected)


    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_push1(self, input_mock, randint_mock):
     '''
       Both the user and the dealer gets blackjack.
       It's push
     '''

     output = run_test([10, 6, 5], ['y', 'n'], [11, 1], randint_mock, input_mock)
     expected = "-----------\n" \
               "YOUR TURN\n" \
               "-----------\n" \
               "Drew a 10\n" \
               "Drew a 6\n" \
               "You have 16. Hit (y/n)? y\n" \
               "Drew a 5\n" \
               "Final hand: 21.\n" \
               "BLACKJACK!\n" \
               "-----------\n" \
               "DEALER TURN\n" \
               "-----------\n" \
               "Drew a Jack\n" \
               "Drew an Ace\n" \
               "Final hand: 21.\n" \
               "BLACKJACK!\n" \
               "-----------\n" \
               "GAME RESULT\n" \
               "-----------\n" \
               "Push.\n"
     self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_push2(self, input_mock, randint_mock):
     '''
      When both the user and the dealer gets same hand value.
      That is less than 21
     '''

     output = run_test([8, 2, 8], ['y', 'n'], [10, 8], randint_mock, input_mock)
     expected = "-----------\n" \
               "YOUR TURN\n" \
               "-----------\n" \
               "Drew an 8\n" \
               "Drew a 2\n" \
               "You have 10. Hit (y/n)? y\n" \
               "Drew an 8\n" \
               "You have 18. Hit (y/n)? n\n" \
               "Final hand: 18.\n" \
               "-----------\n" \
               "DEALER TURN\n" \
               "-----------\n" \
               "Drew a 10\n" \
               "Drew an 8\n" \
               "Final hand: 18.\n" \
               "-----------\n" \
               "GAME RESULT\n" \
               "-----------\n" \
               "Push.\n"
     self.assertEqual(output, expected)  

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer_wins1(self, input_mock, randint_mock):
     '''
      Both the user and the dealer has less than 21.
      The dealer wins by having a higher hand than the user.
     '''

     output = run_test([7, 1], ['n'], [1, 3, 6], randint_mock, input_mock)
     expected = "-----------\n" \
               "YOUR TURN\n" \
               "-----------\n" \
               "Drew a 7\n" \
               "Drew an Ace\n" \
               "You have 18. Hit (y/n)? n\n" \
               "Final hand: 18.\n" \
               "-----------\n" \
               "DEALER TURN\n" \
               "-----------\n" \
               "Drew an Ace\n" \
               "Drew a 3\n" \
               "Dealer has 14.\n" \
               "Drew a 6\n" \
               "Final hand: 20.\n" \
               "-----------\n" \
               "GAME RESULT\n" \
               "-----------\n" \
               "Dealer wins!\n"
     self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer_wins2(self, input_mock, randint_mock):
     '''
      Both the user and dealer gets more than 21. 
      Dealer wins because dealer wins if both user and dealer busts
     '''

     output = run_test([11, 12, 6], ['y', 'n'], [11, 5, 9], randint_mock, input_mock)
     expected = "-----------\n" \
               "YOUR TURN\n" \
               "-----------\n" \
               "Drew a Jack\n" \
               "Drew a Queen\n" \
               "You have 20. Hit (y/n)? y\n" \
               "Drew a 6\n" \
               "Final hand: 26.\n" \
               "BUST.\n" \
               "-----------\n" \
               "DEALER TURN\n" \
               "-----------\n" \
               "Drew a Jack\n" \
               "Drew a 5\n" \
               "Dealer has 15.\n" \
               "Drew a 9\n" \
               "Final hand: 24.\n" \
               "BUST.\n" \
               "-----------\n" \
               "GAME RESULT\n" \
               "-----------\n" \
               "Dealer wins!\n"
     self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer_wins3(self, input_mock, randint_mock):
     '''
      User draws less than 21 but the dealer draws 21.
      The dealer gets blackjack and wins
     '''

     output = run_test([2, 10, 8], ['y', 'n'], [10, 5, 6], randint_mock, input_mock)
     expected = "-----------\n" \
               "YOUR TURN\n" \
               "-----------\n" \
               "Drew a 2\n" \
               "Drew a 10\n" \
               "You have 12. Hit (y/n)? y\n" \
               "Drew an 8\n" \
               "You have 20. Hit (y/n)? n\n" \
               "Final hand: 20.\n" \
               "-----------\n" \
               "DEALER TURN\n" \
               "-----------\n" \
               "Drew a 10\n" \
               "Drew a 5\n" \
               "Dealer has 15.\n" \
               "Drew a 6\n" \
               "Final hand: 21.\n" \
               "BLACKJACK!\n" \
               "-----------\n" \
               "GAME RESULT\n" \
               "-----------\n" \
               "Dealer wins!\n"
     self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer_wins4(self, input_mock, randint_mock):
     '''
      User gets more than 21 and gets burst
      The dealer has less than 21 and wins
     '''

     output = run_test([1, 7, 7], ['y', 'n'], [6, 6, 8], randint_mock, input_mock)
     expected = "-----------\n" \
               "YOUR TURN\n" \
               "-----------\n" \
               "Drew an Ace\n" \
               "Drew a 7\n" \
               "You have 18. Hit (y/n)? y\n" \
               "Drew a 7\n" \
               "Final hand: 25.\n" \
               "BUST.\n" \
               "-----------\n" \
               "DEALER TURN\n" \
               "-----------\n" \
               "Drew a 6\n" \
               "Drew a 6\n" \
               "Dealer has 12.\n" \
               "Drew an 8\n" \
               "Final hand: 20.\n" \
               "-----------\n" \
               "GAME RESULT\n" \
               "-----------\n" \
               "Dealer wins!\n"
     self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer_wins5(self, input_mock, randint_mock):
     '''
      User and dealer gets less than 21.
      Dealer wins as it's hand value is greater
     '''

     output = run_test([10, 7, 2], ['y', 'n'], [6, 6, 8], randint_mock, input_mock)
     expected = "-----------\n" \
               "YOUR TURN\n" \
               "-----------\n" \
               "Drew a 10\n" \
               "Drew a 7\n" \
               "You have 17. Hit (y/n)? y\n" \
               "Drew a 2\n" \
               "You have 19. Hit (y/n)? n\n" \
               "Final hand: 19.\n" \
               "-----------\n" \
               "DEALER TURN\n" \
               "-----------\n" \
               "Drew a 6\n" \
               "Drew a 6\n" \
               "Dealer has 12.\n" \
               "Drew an 8\n" \
               "Final hand: 20.\n" \
               "-----------\n" \
               "GAME RESULT\n" \
               "-----------\n" \
               "Dealer wins!\n"
     self.assertEqual(output, expected)

    # Write all your tests above this. Do not delete this line.

if __name__ == '__main__':
    main()