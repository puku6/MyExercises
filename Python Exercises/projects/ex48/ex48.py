class lexicon(object):
	directions = {'north', 'south', 'east', 'west', 'down', 
				  'up', 'left', 'right', 'back'}
	verbs = {'go', 'stop', 'kill', 'eat'}
	stops = {'the', 'in', 'of', 'from', 'at', 'it'}
	nouns = {'door', 'bear', 'princess', 'cabinet'}

	def scan(self, stuff):
		stuff2 = stuff.lower()
		words = stuff2.split()
		if directions in words:
			return ('directions', directions)