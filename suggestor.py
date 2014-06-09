# -*- coding: utf-8 -*-
from __future__ import division
# Da Paz e Kizzy Terra -- suggestor.py
import os
import random

DEBUG_DIR = './debug/'
SIMULATION_DIR = './simulation/'
PREPROCESSED = 'preprocessed/'
DICTIONARY_DIR = './dictionary/'

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

	def simulateThreeValues(self):
		directory = SIMULATION_DIR + PREPROCESSED
		simulationFiles = [f for f in os.listdir(directory) if 'txt' in f ]

		for filename in simulationFiles:
			f = open(directory + filename, 'r')
			for line in f:
				previsionList = None
				for c in line:
					if(previsionList is not None):
						if(c in previsionList):
							self.matches += 1
						else:
							self.mistakes += 1

					self.state = ord(c)%64
					previsionList = []
					row = self.transitionMatrix[self.state]
					for i in range(3):
						#print(row)
						r = self.predictManyTimes(row)
						previsionList.append(r)
						index = ord(r)
						if(index == 32):
							index = 0
						else:
							index = index%64
						#value = row[index]/(len(row)-1)
						
						#row[index] = 0#- value
						#row = [x+value for x in row]

					
		result = open("result3.txt", 'w')
		result.write("Matches = " + str(self.matches) + "\n")
		result.write("Mistakes = " + str(self.mistakes) + "\n")
		rate = self.matches/(self.matches+ self.mistakes )
		result.write("Sucess Rate = " + str( rate*100 ) + "%\n")

		result.close()
		print("Simulation with 3 Done")

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
		index = -1
		while( aux < p):
			#print str(index) + " " + str(aux)
			index += 1
			aux += self.transitionMatrix[self.state][index]
			

		#self.state = index
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


	def predictManyTimes(self, transitions):
			p = random.random()
			aux = 0
			index = -1
			while( aux < p):
				index += 1
				aux += transitions[index]
					 
			if(index == 0):
				return ' '
			return chr(index+64)

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

	def predictUsingDictionary(self, dictionary, word):
		predicted = None
		while(predicted is None):
			predicted = self.generateRandomChar()
			queryResult = [x for x in dictionary if word in x]
			if(len(queryResult) == 0):
				predicted = None

		return predicted

	def simulateUsingDictionary(self):
		directory = SIMULATION_DIR + PREPROCESSED
		simulationFiles = [f for f in os.listdir(directory) if 'txt' in f ]
		matches = 0
		mistakes = 0
		for filename in simulationFiles:
			f = open(directory + filename, 'r')
			for line in f:
				prevision = None
				word = ""
				miniDictionary = None
				for c in line:
					if(len(word) > 0):
						if(len(word) == 1):
							print("UHHUUULL " + DICTIONARY_DIR + word + ".txt")
							f = open(DICTIONARY_DIR + word + ".txt", 'r')
							miniDictionary = f.read().split()
						if(c == prevision):
							matches += 1
						else:
							mistakes += 1
					word += c
					self.state = ord(c)%64
					if(len(word) > 1):
						prevision = self.predictUsingDictionary(miniDictionary, word)
						miniDictionary = [x for x in miniDictionary if word in x]

				f.close()
		result = open("resultDictionary.txt", 'w')
		result.write("Matches = " + str(matches) + "\n")
		result.write("Mistakes = " + str(mistakes) + "\n")
		rate = matches/(matches+ mistakes )
		result.write("Sucess Rate = " + str( rate*100 ) + "%\n")

		result.close()
		print("Simulation Using Dictionary Done")


