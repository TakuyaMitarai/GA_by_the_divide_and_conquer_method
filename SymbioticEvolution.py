import numpy as np

# 部分解個体
class PartialIndividual:
    def __init__(self, PCHROM_LEN):
        self.chrom = np.random.randint(0, 2, PCHROM_LEN)
        self.fitness = 1000000

# 部分解集団
class PartialPopulation:
    def __init__(self, PPOP_SIZE, PCHROM_LEN):
        self.population = []
        for i in range(PPOP_SIZE):
            individual = PartialIndividual(PCHROM_LEN)
            self.population.append(individual)


# 全体解個体
class WholeIndividual:
    def __init__(self, ppop, WCHROM_LEN, PPOP_SIZE):
        self.chrom = ppop[np.random.randint(0, PPOP_SIZE, WCHROM_LEN)]
        self.fitness = 1000000

# 全体解集団
class WholePopulation:
    def __init__(self, ppop, WPOP_SIZE, WCHROM_LEN, PPOP_SIZE):
        self.population = []
        for i in range(WPOP_SIZE):
            individual = WholeIndividual(ppop, WCHROM_LEN, PPOP_SIZE)
            self.population.append(individual)

def evaluate_fitness(wpop, ppop):
    #なんか書く

# ハイパーパラメータ
WPOP_SIZE = 200
PPOP_SIZE = 200
MAX_GENERATION = 400
WCROSSOVER_PROB = 0.8
PCROSSOVER_PROB = 0.8
WMUTATE_PROB = 0.01
PMUTATE_PROB = 0.01
WCHROM_LEN = 8
PCHROM_LEN = 8

#初期化
ppop = PartialPopulation(PPOP_SIZE, PCHROM_LEN)
wpop = WholePopulation(ppop, WPOP_SIZE, WCHROM_LEN, PPOP_SIZE)
evaluate_fitness(wpop, ppop)


