"""
	player class file
"""

from core.characters.character import Character

class Player(object):

	"""
		player class
	"""

	def __init__(self):

		super(Player, self).__init__()

		self.name = "Default"
		self.character = None

	def set_character(self, character):

		"""
			change player's character
		"""

		if not isinstance(character, Character):

			return

		self.character = character()

	def set_name(self, new):

		"""
			change player's name
		"""

		if len(new) < 2:

			return

		self.name = new
