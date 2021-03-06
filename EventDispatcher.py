#
# EventDispatcher.py
# Event dispatcher for PyGame
#
# Jonatan H Sundqvist
# November 14 2014
#

# TODO | - Look into get_mods, key.get_repeat and get_pressed
#        -
#
# SPEC | -
#        -



import pygame
import sys
from pygame.constants import *
from collections import defaultdict



class EventDispatcher:

	'''
	Introduces dynamic event binding to Pygame.

	Add, replace and query event handlers

	'''

	# TODO: Normalize event data (?)
	# TODO: Event aliases, tkinter-style event definitions (?)
	# eg. type=KEYDOWN key=LEFT
	# TODO: Hierachies of events, multiple handlers, replace or add
	# TODO: Pattern or Event class implementing aliases, comparisons, etc.
	# TODO: Queries
	# TODO: Composite events, control keys (eg. Ctrl+Alt+A, Mousemotion+Left mouse button)
	# TODO: Nested dicts or objects (?)
	# TODO: Handle polling as well (?)
	# TODO: Annotations, error handling

	class Pattern(object):

		''' Docstring goes here '''

		def __init__(self, attributes):
			self.also = attributes.pop('also', tuple()) # Keys that must be pressed to for the pattern to match
			self.doc  = attributes.pop('doc', '')
			self.attributes = frozenset(attributes.items())


	def __init__(self):
		
		'''
		Docstring goes here

		'''

		# TODO: Is this the optimal data structure (w.r.t RAM and CPU)
		# TODO: Allow multiple handlers per pattern
		self.handlers 	= defaultdict(lambda: defaultdict(list)) # Maps event types to patterns and their respective handlers
		self.always 	= lambda event: None # Runs on each iteration of the main loop (configurable)
		self.debug 		= False

		self.keys = defaultdict(bool) # TODO: Use class with default __getattr__ instead (?)


	def DEBUG(self, *messages):

		'''
		Docstring goes here

		'''

		if self.debug: print(*messages)


	def setKey(self, event):

		'''
		Updates internal key state dictionary

		'''

		# TODO: Implement
		# TODO: Rename (?)

		self.keys[0] = event.type in (MOUSEBUTTONDOWN, KEYDOWN) # True when pressed


	def handle(self, event):
		
		'''
		Dispatches an event to all matching event handlers.

		'''

		for pattern, handler in self.query(event): #getattr(self, event.type)
			handler(pattern, event)
			self.DEBUG('Invalid handler type')


	def query(self, event):

		'''
		Retrieves all event handlers whose pattern
		matches that of the incoming event (cf. bind for details).

		'''

		# TODO: Use issubset for comparisons
		# TODO: Determine and - if necessary - improve performance
		# TODO: Complete overview of event types and related data

		# TODO: Optionally return mapping between matching patterns and their corresponding handlers (?)
		return ((pattern, handler) for pattern, handlers in self.handlers[event.type].items() for handler in handlers if self.matches(pattern, event))


	def matches(self, pattern, event):

		'''
		Verifies that a given pattern matches the event.

		'''

		# TODO: Catch match object creation
		# TODO: Document meaning of pattern fields (eg. 'also', 'type', 'rel')

		match = frozenset((attr, getattr(event, attr)) for attr in ['type', 'key', 'button', 'rel', 'unicode', 'scancode', 'mod'] if hasattr(event, attr))
		# self.DEBUG(match)
		# NOTE: all([]) is True
		pressed = [pygame.key.get_pressed()[key] for key in pattern.also]

		return pattern.attributes.issubset(match) and all(pressed)


	def bind(self, pattern, handler, replace=False):

		'''
		Binds a handler to an event pattern, optionally
		replacing any pre-existing handlers.

		A pattern is defined as a set of properties which an event must have
		to be considered a match (eg. event.type is KEYDOWN and event.key is K_LEFT)
		

		Returns an ID associated with the particular handler.

		'''

		# TODO: Implement replace option
		# TODO: Use issubset for comparisons
		# TODO: Should the type property be mandatory (?)
		# TODO: Proper handling of also property

		# NOTE: The 'also' property is treated differently since
		# it is independent from the current event
		# key.also = also
		key = EventDispatcher.Pattern(pattern)
		self.DEBUG('Bound pattern:', key)
		self.handlers[pattern['type']][key].append(handler)
		return hash(key), id(handler)


	def mainloop(self):
		
		'''
		Docstring goes here

		'''

		self.clock = pygame.time.Clock()
		self.bind({'type': QUIT}, lambda p, e: sys.exit())
		self.bind({'type': KEYDOWN, 'key': K_ESCAPE}, lambda p, e: sys.exit())

		while True:
			self.clock.tick(30)
			for event in pygame.event.get():
				self.DEBUG(event)
				self.setKey(event)
				self.handle(event)
			self.always(event)