# -*- coding: utf-8 -*-
from __future__ import division
# Da Paz e Kizzy Terra -- suggestor.py
import os

DEBUG_DIR = './debug/'
SIMULATION_DIR = './simulation/'

class Preprocessor:
	def __init__(self, source_dir, output_dir):
		self.TEST_DIR = source_dir
		self.PREPROCESSED_DIR = output_dir

		self.specialChars = {
			self.getSpecialId('á') : ord('A')%64,
			self.getSpecialId('à') : ord('A')%64,
			self.getSpecialId('Á') : ord('A')%64,
			self.getSpecialId('À') : ord('A')%64,
			self.getSpecialId('ã') : ord('A')%64,
			self.getSpecialId('Ã') : ord('A')%64,

			self.getSpecialId('é') : ord('E')%64,
			self.getSpecialId('É') : ord('E')%64,
			self.getSpecialId('ê') : ord('E')%64,
			self.getSpecialId('Ê') : ord('E')%64,

			self.getSpecialId('í') : ord('I')%64,
			self.getSpecialId('Í') : ord('I')%64,

			self.getSpecialId('ó') : ord('O')%64,
			self.getSpecialId('Ó') : ord('O')%64,
			self.getSpecialId('õ') : ord('O')%64,
			self.getSpecialId('Õ') : ord('O')%64,

			self.getSpecialId('ú') : ord('U')%64,
			self.getSpecialId('Ú') : ord('U')%64,

			self.getSpecialId('ç') : ord('C')%64,
			self.getSpecialId('Ç') : ord('C')%64
		}
		print self.specialChars

	def getSpecialId(self, specialChar):
		for c in specialChar:
			specialId = ord(c)
			if(specialId == 195):
				continue
			else:
				return specialId 

	def preProcessFile(self, inputName):
		f = open(self.TEST_DIR + inputName, 'r')
		text = f.read()
		text = text.upper()

		f.close()
		f = open(self.PREPROCESSED_DIR + "p_" + inputName, 'w')
		for c in text:
			aux = ord(c)
			if(aux == 195):
				continue
			elif(aux < 128):
				if(aux == 32):
					aux = 0
				elif(aux < 64 or aux > 90):
					continue
				else:
					aux = aux % 64
				f.write(str(aux)+ " ")
			else:
				try:
					f.write( str(self.specialChars[aux]) + " " )
				except Exception:
					pass
		f.close()

	def buildPreProcessedFiles(self):
		files = [f for f in os.listdir(self.TEST_DIR) if 'txt' in f ]

		for filename in files:
			self.preProcessFile(filename)

	def preProcessToSimulate(self, simulation_dir):
		files = [f for f in os.listdir(SIMULATION_DIR) if 'txt' in f ]

		for filename in files:
			inputFile = open(simulation_dir + filename, 'r')
			outputFile = open(simulation_dir +"preprocessed/" + "p_" + filename, 'w')
			for line in inputFile:
				line = line.upper()
				for c in line:
					aux = ord(c)
					if(aux == 195 or c == '\n'):
						continue
					elif(aux < 128):
						if(aux < 64 or aux > 90):
							outputFile.write('\n')
						else:
							outputFile.write(c)
					else:
						try:
							a = self.specialChars[aux]
							a += 64
							outputFile.write( chr( a ) ) 
						except Exception:
							#print aux
							pass
			inputFile.close()
			outputFile.close()

	def preProcessToDictionary(self, dictionary_dir):
		files = [f for f in os.listdir(SIMULATION_DIR) if 'txt' in f ]

		for filename in files:
			inputFile = open(self.TEST_DIR + filename, 'r')
			outputFile = open(dictionary_dir +"preprocessed/" + "p_" + filename, 'w')
			for line in inputFile:
				line = line.upper()
				for c in line:
					aux = ord(c)
					if(aux == 195 or c == '\n'):
						continue
					elif(aux < 128):
						if(aux < 64 or aux > 90):
							outputFile.write('\n')
						else:
							outputFile.write(c)
					else:
						try:
							a = self.specialChars[aux]
							a += 64
							outputFile.write( chr( a ) ) 
						except Exception:
							#print aux
							pass
			inputFile.close()
			outputFile.close()
