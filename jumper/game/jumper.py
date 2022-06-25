import random
import game.terminal_service

class Jumper:
    """The person falling from the sky 
    
    The responsibility of the jumper is to track the state of the parachute and count of letters guessed so far
    
    Attributes:
        _terminal : the terminal services object
        _location (int): The location of the hider (1-1000).
        _bad_guess_count (int) : the guesses made so far 
        _distance (List[int]): The distance from the seeker.
    """

    def __init__(self, terminal_service):
        """Constructs a new Jumper.

        Args:
            self (Jumper): An instance of Jumper.
            terminal_services: an instance of the terminal services class
        """
        self.terminal = terminal_service
        self.bad_guess_count = 0
        self._parachute = [
            "  _____  ",
            " /_____\ ",
            " \     / ",
            "  \   /  ",
            "    O    ",
            "  / | \  ",
            "   / \   ",
            "         ",
            "^^^^^^^^^"
            ]
    def made_bad_guess(self):
        """ Mark that a bad guess has occured and removed a line from the parachute
        
        Args:
            self (Jumper): an instance of Jumper
        """
        if self.bad_guess_count >= 5:
            return
        self.bad_guess_count += 1
        self._parachute.pop(0)

    def draw(self):
        """ Draw the current state of the jumper
        
        Args:
            self (Jumper): an instance of Jumper
        """

        if self.bad_guess_count >= 5:
            self.terminal.write_text("    X    ")
        for line in self._parachute:
            self.terminal.write_text(line)


