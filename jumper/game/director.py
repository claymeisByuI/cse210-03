from pyparsing import Word
from game.terminal_service import TerminalService
from game.jumper import Jumper
from game.wordList import Word_list

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        is_playing (boolean): Whether or not to keep playing.
        terminal_service: For getting and displaying information on the terminal.
        jumper (Jumper) = class to track state and attriburtes of jumper
        word_list (Word_list): Word_list class to maintaing the class
        current_guesses ( List ):  current guesses 
        recent_letter: the most recent letter
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._terminal_service = TerminalService()
        self._jumper = Jumper(self._terminal_service)
        self._is_playing = True
        self._word_list = Word_list(self._terminal_service)
        self.current_guesses = []
        self.recent_letter = ''

        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        self._do_outputs()
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
        self._terminal_service.write_text("Good Game!")


    def _do_outputs(self):
        """clears the screen
           Draws wordlist guesses
           draw the jumper
           check for game over
        Args:
            self (Director): An instance of Director.
        """
        self._terminal_service.write_text('\033c')
        self._word_list.draw_state(self.current_guesses)
        self._terminal_service.write_text("")
        self._jumper.draw()
        self._terminal_service.write_text("")
        if self._word_list.too_many_guesses(self.current_guesses):
            self._is_playing = False
        


    def _get_inputs(self):
        """Gets the user input for the next letter

        Args:
            self (Director): An instance of Director.
        """
        self.recent_letter = self._terminal_service.read_text("Guess a letter [a-z]: ")
        self.current_guesses.append(self.recent_letter.lower())

    def _do_updates(self):
        """Update the wordlist and state of the jumper.

        Args:
            self (Director): An instance of Director.
        """
        if self._word_list.is_letter_in_secret(self.recent_letter) == False:
            self._jumper.made_bad_guess()

        if self._word_list.is_guessed(self.current_guesses):
            self._is_playing = False
