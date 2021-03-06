#!/usr/bin/env python3.4

from urllib.request import urlopen
from argparse import ArgumentParser
from bs4 import BeautifulSoup
from random import choice

class color:
	PURPLE = '\033[95m'
	CYAN = '\033[96m'
	DARKCYAN = '\033[36m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	END = '\033[0m'

url = 'http://www.dictionary.com/browse/'

randomurl = 'http://www.thefreedictionary.com/dictionary.htm'

ran = str(urlopen(randomurl).read())
randomsoup = BeautifulSoup(ran, 'html.parser')
randomlist = randomsoup.select(".lst")
randomitem = BeautifulSoup(str(randomlist), 'html.parser')
randomcon = randomitem.select("a")
randomword = BeautifulSoup(str(randomcon), 'html.parser')

words = []

for i in randomword.strings:
	words.append(i)

words.remove('[')
words.remove(']')

n = words.count(', ')

for i in range(n):
	words.remove(', ')

word = choice(words)

parser = ArgumentParser()
parser.add_argument("-w", "--word", help="Enter a word to search")
args = parser.parse_args()
if args.word:
	word = str(args.word)

conurl = url + str(word)

print()
print()
print(color.CYAN + color.BOLD + color.UNDERLINE + str(word).capitalize() + color.END)
print()
print()

contents = str(urlopen(conurl).read())
soup = BeautifulSoup(contents, 'html.parser')
lists = soup.find_all('div', class_='def-list')
lists = lists[0]
lists = lists.find_all('section', class_='def-pbk')

for i in range(len(lists)):
	head = lists[i].find_all('span', class_='dbox-pg')
	defi = lists[i].find_all('div', class_='def-set')
	for j in range(len(head)):
		print(color.BOLD + color.RED + head[j].string.capitalize() + color.END)
		print()
		for k in range(len(defi)):
			num = defi[k].find_all('span', class_='def-number')
			defin = defi[k].find_all('div', class_='def-content')
			for l in range(len(num)):
				string = num[l].string + " " + str(defin[l].get_text())[12:]
				string = str(string)
				string = list(string)
				for A, B in enumerate(string):
					if (B == '\\' and string[A + 1] == 'r' and string[A + 2] == '\\' and string[A + 3] == 'n') or B == '\\' and string[A + 1] == 'x':
						del string[A: A + 4]
					if B == '\\' and string[A + 1] == "'":
						string[A + 1] = "\'"
						del string[A]

				for A, B in enumerate(string):
					if B == '\\' and string[A + 1] == 'x':
						del string[A: A + 4]

				string = ''.join(string)
				
				print(color.YELLOW + string + color.END)
				print()
