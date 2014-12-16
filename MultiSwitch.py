#
# MultiSwitch
# Description...
#
# Jonatan H Sundqvist
# date
#

# TODO | - Simplify implementation by inheriting from userDict and overriding __init__ or __new__ (?)
#        -
#
# SPEC | -
#        -



class MultiSwitch(object):

	'''
	Maps multiple values to one and the same value, as
	specified by a mapping of iterables to any other object.

	'''

	_cache = {} # Ugh, underscore


	def __new__(MSwitch, mapping, mnemonic=None):

		'''
		Retrieves switch from the cache if it already exists

		'''

		if mnemonic in MSwitch._cache:
			return MSwitch._cache[mnemonic]
		else:
			# TODO: Safe to rely on id (?)
			switch = super(MultiSwitch, MSwitch).__new__(MSwitch)
			MSwitch._cache[mnemonic or id(switch)] = switch # Relies on logic short-circuiting
			return switch


	def __init__(self, mapping, mnemonic=None):
		self.mapping = self.unpack(mapping)
		self.mnemonic = mnemonic
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