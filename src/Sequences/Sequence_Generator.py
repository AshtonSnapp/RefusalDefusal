#####################################################################
# Name: Carrick Inabnett, Ashton Snapp, Justin Crouch
# Last Update: 12 May 19
# Changes: Created class to handle storing and loading sequences
#####################################################################
# Library to pick a random sequence
from random import choice

# Class to generate sequences
class SequenceGenerator(object):

	# Initialize holders for each difficulty's sequence and hints
	# Initialize holders for current sequence and hints
	def __init__(self):
		self.easy_sequences = []
		self.easy_hints = []

		self.medium_sequences = []
		self.medium_hints = []

		self.hard_sequences = []
		self.hard_hints = []

		self.realLife_sequences = []
		self.realLife_hints = []

		self.sequence = []
		self.hints = []

	# Choose a random sequence given a difficulty
	def genSequence(self, diff):
		if(diff == "Easy"):
			self.sequence = choice(self.easy_sequences)
			self.hints = self.easy_hints[ self.easy_sequences.index(self.sequence) ]

		elif(diff == "Medium"):
			self.sequence = choice(self.medium_sequences)
			self.hints = self.medium_hints[ self.medium_sequences.index(self.sequence) ]

		elif(diff == "Hard"):
			self.sequence = choice(self.hard_sequences)
			self.hints = self.hard_hints[ self.hard_sequences.index(self.sequence) ]

		elif(diff == "RealLife"):
			self.sequence = choice(self.realLife_sequences)
			self.hints = self.realLife_hints[ self.realLife_sequences.index(self.sequence) ]

	# Return the first activity in the current sequence
	def getAct(self):
		return self.sequence[0]

	# Return the first hint in the current sequence
	def getHint(self):
		return self.hints[0]

	# Return the length of the current sequence
	def getSeqLen(self):
		return len( self.sequence )

	# Remove the first element of the current sequence and hints holder
	def remAct(self):
		del self.sequence[0]
		del self.hints[0]

	# Add a sequence and hints to a given difficulty
	def addSeq(self, diff, sequence, hints):
		if(diff == "Easy"):
			self.easy_sequences.append(sequence)
			self.easy_hints.append(hints)

		elif(diff == "Medium"):
			self.medium_sequences.append(sequence)
			self.medium_hints.append(hints)

		elif(diff == "Hard"):
			self.hard_sequences.append(sequence)
			self.hard_hints.append(hints)

		elif(diff == "RealLife"):
			self.realLife_sequences.append(sequence)
			self.realLife_hints.append(hints)

	# Erase data from current sequence and hints
	def clearSeq(self):
		self.sequence = []
		self.hints = []