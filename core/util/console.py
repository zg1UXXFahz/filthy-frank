"""
	console class
"""

class Console(object):

	"""
		Console class for io
	"""

	@staticmethod
	def out(text):
		"""
			custom print out
		"""

		print(text)

	@staticmethod
	def get(question=""):

		"""
			custom get input
		"""

		print(question)
		return input()
