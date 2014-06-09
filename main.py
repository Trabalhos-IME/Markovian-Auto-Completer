# -*- coding: utf-8 -*-
# Da Paz e Kizzy Terra - main.py
from __future__ import division

from preprocessor import Preprocessor
from suggestor import Suggestor
from dictionary import ImprovisedDictionary


TEST_DIR = './testbase/'
PREPROCESSED_DIR = './preprocessed_texts/'
MATRIX_DIR = './transition_matrix/'
DEBUG_DIR = './debug/'
SIMULATION_DIR = './simulation/'
DICTIONARY_DIR = './dictionary/'

dictionary = ImprovisedDictionary(DICTIONARY_DIR)
processor = Preprocessor(TEST_DIR, PREPROCESSED_DIR)
completer = Suggestor(PREPROCESSED_DIR, MATRIX_DIR)

## Uncomment this lines if text is not preprocessed yet

#processor.preProcessToDictionary(DICTIONARY_DIR)
#processor.buildPreProcessedFiles()
#processor.preProcessToSimulate(SIMULATION_DIR)

## Uncomment this lines if you need to build your dictionary

#dictionary.buildDictionary()
#dictionary.organizeRegisters()


#completer.simulate()
#completer.simulateThreeValues()


completer.simulateUsingDictionary()