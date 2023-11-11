import numpy as np

class PartialIndividual:
    def __init__(self, PCHROM_LEN):
        self.chrom = np.random.randint(0, 2, PCHROM_LEN)
        self.fitness = 1000000

def partialpopulation_init():

class WholeIndividual:

def wholepopulation_init():

#hyperparameter
WPOP_SIZE = 200
PPOP_SIZE = 200
MAX_GENERATION = 400
WCROSSOVER_PROB = 0.8
PCROSSOVER_PROB = 0.8
WMUTATE_PROB = 0.01
PMUTATE_PROB = 0.01

