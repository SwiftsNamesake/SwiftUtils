#
# Vexillologist.py
# Creates national flags
#
# Jonatan H Sundqvist
# July 31 2014
#

from PIL import Image, ImageDraw
from math import floor


def demo():
	size 	= 255, 255
	img 	= Image.new('RGB', size)
	pixels 	= img.load()

	for x in range(img.size[0]):
		for y in range(img.size[1]):
			pixels[x, y] = (x, y, 100)

	img.show()


def Sweden():
	size 	= 100, 100
	
	#field, cross = (0, 0, 255), (0xF7, 0xDB, 0x3E) # Sweden
	field, cross = (200, 0, 0), (255, 255, 255)		# Denmark

	img 	= Image.new('RGB', size, field)
	pixels 	= img.load()

	for x in range(floor(img.size[0]*0.4), floor(img.size[0]*0.6)):
		for y in range(img.size[1]):
			pixels[x, y] = cross
			pixels[y, x] = cross

	return img
	#img.show()
	#img.save('sweden.png')


def India():

	size = 120, 120

	#white 	= tuple(int(ch*255*72.6/100.0) for ch in (0.313, 0.319, 0.368))
	#saffron = tuple(int(ch*255*21.5/100.0) for ch in (0.538, 0.360, 0.102))
	#green 	= tuple(int(ch*255*8.90/100.0) for ch in (0.288, 0.395, 0.317))

	white 	= (255, 255, 255)
	saffron = (255, 153, 51)
	green 	= (18, 136, 7)

	print(white, saffron,green)
	img 	= Image.new('RGB', size, white)
	pixels 	= img.load()

	for x in range(img.size[0]):
		for y in range(img.size[1]//3):
			pixels[x, y] = saffron
			pixels[x, y+img.size[1]//3*2] = green

	return img


def UK():
	pass


def US():
	pass


def Spain():
	pass


def main():
	swe = Sweden()
	ind = India()

	swe.show()
	ind.show()


if __name__ == '__main__':
	main()