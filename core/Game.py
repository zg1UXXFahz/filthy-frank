"""
	main game file
"""

from core.util.console import Console
from core.player.player import Player

class Game(object):

	"""
		Main game class
	"""

	def __init__(self):

		super(Game, self).__init__()

		self.player = Player()

	def start(self):

		"""
			Start a new game
		"""

		Console.dialogue("You slowly emerge from the darkness.")
		Console.dialogue("The ground parts beneath your feet, rocks slip through the cracks.")
