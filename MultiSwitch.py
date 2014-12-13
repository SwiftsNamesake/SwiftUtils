#
# MultiSwitch
# Description...
#
# Jonatan H Sundqvist
# date
#

# TODO | -
#        -
#
# SPEC | -
#        -



class MultiSwitch(object):

	'''
	Maps multiple values to one and the same value, as
	specified by a mapping of iterables to any other object.

	'''

	def __init__(self, mapping):
		self.mapping = self.unpack(mapping)
		# self.__getitem__ = self.mapping.__getitem__
		# self.__setitem__ = self.mapping.__setitem__
		# self.__delitem__ = self.mapping.__delitem__


	def unpack(self, mapping):

		'''
		Unpacks the initial compacted mapping into
		a conventional dictionary for easy access.
		'''

		unpacked = {}
		for keys, value in mapping.items():
			for key in keys:
				unpacked[key] = value
		return unpacked


	def get(self, key, default):
		return self.mapping.get(key, default)


	def __getitem__(self, key): return self.mapping[key]
	def __delitem__(self, key): del self.mapping[key]
	def __setitem__(self, key, value): self.mapping[key] = value


def main():
	
	'''
	Test suite

	'''

	switch = MultiSwitch({('red', 'green', 'blue'): 'colour', ('drill', 'hammer', 'saw'): 'tool'})
	assert switch['red'] is 'colour'
	assert switch['saw'] is 'tool'



if __name__ == '__main__':
	main()