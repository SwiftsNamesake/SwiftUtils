#
# EulerTemplate.py
# Creates templates for Project Euler solutions
#
# Jonatan H Sundqvis
# August 1 2014
#


from urllib import request
from bs4 import BeautifulSoup
from sys import argv

from time import localtime, strftime


python = '''
# 
# Project Euler - Problem {number}
#
# {desc}
#
# {auth}
# {date}
#


def main():
	pass


if __name__ == \'__main__\':
	main()

'''.lstrip('\n')

haskell = '''
-- 
-- Project Euler - Problem {number}
--
{desc}
--
-- {auth}
-- {date}
--

main :: IO ()
main = do
	-- Code goes here --

'''.lstrip('\n')


templates = {
	'Haskell': (haskell, 'hs'),
	'Python': (python, 'py')
}


def loadProblemData(problem):
	url 	= 'http://projecteuler.net/problem=%d' % problem
	resp 	= request.urlopen(url)
	DOM 	= BeautifulSoup(resp.read())
	
	return {
		'number': problem,
		'desc': [p.text for p in DOM.find_all('p') if 'problem_content' in p.parent['class']],
		'auth': 'Firstname Lastnameson',
		'date': strftime('%B %d %Y', localtime())
	}


def fillTemplate(template, data):
	# TODO: Do more advanced formatting
	# NOTE: Format seems to ignore keys not found in format string
	prefix = template.split()[0] + ' '
	lines = chunks(''.join(data['desc']).split(), 10)
	data['desc'] = '\n'.join(prefix + ' '.join(line) for line in lines)
	return template.format(**data)


def save(fn, template):
	with open(fn, 'w+', encoding='utf-8') as f:
		f.write(template)


def chunks(data, length):
	return [ data[n:n+length] for n in range(0, len(data), length) ]


def lineWrap(string, width):
	return '\n'.join(chunks(string, width))


def loadAndSave(problem, language):
	data 		= loadProblemData(int(problem))
	template 	= fillTemplate(templates[language][0], data)
	save('Problem %s.%s' % (problem, templates[language][1]), template)


def main():
	#url 	= 'http://projecteuler.net/problem=1'
	#resp 	= request.urlopen(url)
	#DOM 	= BeautifulSoup(resp.read())
	#print(DOM.title)
	if len(argv) > 1:
		if argv[1] == '--help':
			print(lineWrap('This program creates a solution template for the problem you specify on the command line', 40))
		elif argv[1].isdigit() and len(argv) > 2:
			loadAndSave(argv[1], argv[2])
		else:
			print('Invalid arguments: %r' % argv[1:])
	else:
		print('Too few arguments. Use \'--help\' for more information.')


if __name__ == '__main__':
	main()