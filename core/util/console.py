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

		print text

	@staticmethod
	def get(question=""):

		"""
			custom get input
		"""

		print question
		return input()

	@staticmethod
	def dialogue(text):

		"""
			print dialogue and wait for enter
		"""

		if isinstance(text, str):

			raw_input("%s " % text)

		elif isinstance(text, list):

			for i in text:

				raw_input(i)
