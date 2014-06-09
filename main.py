# -*- coding: utf-8 -*-
# Da Paz e Kizzy Terra - main.py
from __future__ import division

from preprocessor import Preprocessor
from suggestor import Suggestor


TEST_DIR = './testbase/'
PREPROCESSED_DIR = './preprocessed_texts/'
MATRIX_DIR = './transition_matrix/'
DEBUG_DIR = './debug/'
SIMULATION_DIR = './simulation/'


processor = Preprocessor(TEST_DIR, PREPROCESSED_DIR)
completer = Suggestor(PREPROCESSED_DIR, MATRIX_DIR)


processor.buildPreProcessedFiles()
processor.preProcessToSimulate(SIMULATION_DIR)

completer.simulate()

word = ""
for i in range(10):
	word += completer.generateRandomChar()
print word