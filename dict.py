# -*- coding: utf-8 -*-
from __future__ import division
# Da Paz e Kizzy Terra -- dict.py
import os

DICTIONARY_DIR = './dictionary'
TEST_DIR = './testbase/'

class Dictionary:

	def _init_ (DICTIONARY_DIR):
		self.DIR = DICTIONARY_DIR

	def makePersistent(self, records):
		sortedArray = []
		for i in range(26):
			c = chr(i + 65)
			sortedArray.append([x for x in records if x[0] == c ])

		index = 65
		for line in sortedArray:
			f = open(chr(index)+ ".txt", 'a')
			for word in line:
				f.write(word + '\n')
			f.close()
			index += 1


	def organizeRegisters(self):
		files = [f for f in os.listdir(self.DIR) if 'txt' in f ]

		for filename in files:
			f = open (filename, 'r')
			records = f.read().split()
			records = list(set(records))
			records.sort()
			f.close()
			f = open (filename, 'w')
			for record in records:
				f.write(record + '\n')
			f.close()

	def buildDictionary(self):
		files = [f for f in os.listdir(self.DIR) if 'txt' in f ]
		for filename in files:
			f = open(filename, 'r')
			everything = f.read()
			words = everything.split()
			words = list(set(words))
			words.sort()
			self.makePersistent(words)
			f.close()
		
