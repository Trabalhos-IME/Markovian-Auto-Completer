# -*- coding: utf-8 -*-
from __future__ import division
# Da Paz e Kizzy Terra -- suggestor.py
import os
import random

DEBUG_DIR = './debug/'
SIMULATION_DIR = './simulation/'
PREPROCESSED = 'preprocessed/'

class Suggestor:

	def __init__(self, source_dir, matrix_dir):
		self.MATRIX_DIR = matrix_dir
		self.SOURCE_DIR = source_dir
		self.state = 0
		try:
			self.readMatrix()
		except Exception:	
			self.processedTokens = 0
			self.transitionMatrix = self.buildTransitionMatrix()
			self.saveMatrix( "matrix.txt" )

		self.matches = 0
		self.mistakes = 0

	def buildTransitionMatrix(self):
		transitionMatrix = [[0 for x in range(27)] for x in range(27)]
		processedFiles = [f for f in os.listdir(self.SOURCE_DIR) if 'txt' in f ]

		for filename in processedFiles :
			f = open(self.SOURCE_DIR + filename, 'r')
			for line in f:
				array = line.split()
				for i in range( len(array)-1 ):
					try:
						transitionMatrix[ int(array[i]) ][ int(array[i+1]) ] += 1
					except:
						print("indice doido " + str(array[i]))
					self.processedTokens += 1
			f.close()
		sumRow = [sum(row) for row in transitionMatrix]
		#divide all element by the number of tokens to get the percentage
		index = 0
		for elem in sumRow:
			if(elem != 0):
				transitionMatrix[index] = [ cell/float(elem) for cell in transitionMatrix[index]]
				index += 1
		return transitionMatrix

	def saveMatrix(self, filename):
		filename = self.MATRIX_DIR + filename
		f = open(filename, 'w')
		f.write(str( self.processedTokens ) + '\n')
		for row in self.transitionMatrix:
			for cell in row:
				f.write(str(cell) + " ")
			f.write('\n')
		f.close()

	def generateRandomChar(self):
		if(self.state == 32):
			self.state = 0
		p = random.random()
		#print p
		aux = 0
		index = 0
		while( aux < p):
			#print str(index) + " " + str(aux)
			aux += self.transitionMatrix[self.state][index]
			index += 1

		self.state = index
		if(index == 0):
			return ' '
		return chr(index+64)

	def readMatrix(self):
		self.transitionMatrix = [[0 for x in range(27)] for x in range(27)]
		try:
			f = open(self.MATRIX_DIR + "matrix.txt")
		except Exception:
			raise Exception('file not found')
		
		self.processedTokens = f.readLine()
		index = 0
		for line in f:
			self.transitionMatrix[index] = line.split()
			index += 1

	def simulate(self):
		directory = SIMULATION_DIR + PREPROCESSED
		simulationFiles = [f for f in os.listdir(directory) if 'txt' in f ]

		uniformMatches = 0
		uniformMistakes = 0

		for filename in simulationFiles:
			f = open(directory + filename, 'r')
			for line in f:
				prevision = None
				uniformPrevision = None
				for c in line:
					if(prevision is not None):
						if(c == prevision):
							self.matches += 1
						else:
							self.mistakes += 1

						if(c == uniformPrevision):
							uniformMatches += 1
						else:
							uniformMistakes += 1

					self.state = ord(c)%64
					prevision = self.generateRandomChar()
					uniformPrevision = chr(random.randint(1, 26) + 64)
		result = open("result.txt", 'w')
		result.write("Matches = " + str(self.matches) + "\n")
		result.write("Mistakes = " + str(self.mistakes) + "\n")
		rate = self.matches/(self.matches+ self.mistakes )
		result.write("Sucess Rate = " + str( rate*100 ) + "%\n")


		result.write("At Random Matches = " + str(uniformMatches) + "\n")
		result.write("At Random Mistakes = " + str(uniformMistakes) + "\n")
		rate = uniformMatches/(uniformMatches+ uniformMistakes )
		result.write("Sucess Rate at Random = " + str( rate*100 ) + "%")
		result.close()
		print("Simulation Done")



