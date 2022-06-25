import random
from game.terminal_service import TerminalService 

class Word_list:
    """A class to maintain a the current word and possible words. 
    
    Attributes:
        terminal_service: For getting and displaying information on the terminal.
        list_of_words(List): a list of possible words
        current_secret: The word for this game
    """
    def __init__(self, terminal_service):
        """ Constructs a new Word_list.

        Args:
            self (Word_list): An instance of Word_list.
            terminal_services: an instance of the terminal services class
        """

        self.terminal_service = terminal_service
        self._list_of_words = ['computer', 'laptop', 'python', 'mouse', 'keyboard']
        self._current_secret = self._get_secret_word()

    def draw_state(self, list_of_guesses):
        """ Draws the current word filled in with guesses

        Args:
            self (Word_list): An instance of Word_list.
            list_of_guesses (list): list of characters that represents Guesses so far
            
        """

        output = ""
        for letter in self._current_secret:
            if letter.lower() in list_of_guesses:
                output = output + letter + " "
            else:
                output = output + "_ "
        self.terminal_service.write_text(output)

    def is_letter_in_secret(self, letter):
        """ Checks the letter agains the secret

        Args:
            self (Word_list): An instance of Word_list.
            letter: a letter representing the current guess
            
        """
        return letter.lower() in self._current_secret.lower()

    def is_guessed(self, letters):
        """ Checks if the word is guessed based on letters

        Args:
            self (Word_list): An instance of Word_list.
            letter: the letters representing the current guess
            
        """
        result = True
        for letter in self._current_secret:
            if not letter.lower() in letters:
                result = False
        return result

    def too_many_guesses(self, letters):
        """ Checks if the there have been too many bad guesses

        Args:
            self (Word_list): An instance of Word_list.
            letter: the letters representing the current guess
            
        """
        badGuesses = 0
        for guess in letters:
            if not guess in self._current_secret.lower():
                badGuesses += 1
        return badGuesses > 4

    def _get_secret_word(self):
        """Gets a secret word for the puzzle.

        Args:
            self (Puzzle): An instance of Puzzle.
        
        Returns:
            string: A secret word
            ]        """
        index = random.randrange(0, len(self._list_of_words))
        secretWord = self._list_of_words[index].upper()
        return secretWord
