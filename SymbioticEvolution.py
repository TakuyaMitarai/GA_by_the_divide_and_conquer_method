import numpy as np

np.random.seed(seed=65)

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

# 部分解個体
class PartialIndividual:
    def __init__(self):
        self.chrom = np.random.randint(0, 2, PCHROM_LEN)
        self.fitness = 1000000

# 部分解集団
class PartialPopulation:
    def __init__(self):
        self.population = []
        for i in range(PPOP_SIZE):
            individual = PartialIndividual()
            self.population.append(individual)

# 全体解個体
class WholeIndividual:
    def __init__(self):
        self.chrom = []
        for _ in range(WCHROM_LEN):
            index = np.random.randint(0, PPOP_SIZE)
            self.chrom.append(ppop.population[index])

        self.fitness = 1000000

# 全体解集団
class WholePopulation:
    def __init__(self):
        self.population = []
        for i in range(WPOP_SIZE):
            individual = WholeIndividual()
            self.population.append(individual)

# floyd問題
def evaluate_fitness():
    for i in range(WPOP_SIZE):
        fitness = 0.0
        for j in range(WCHROM_LEN):
            for k in range(PCHROM_LEN):
                fitness += (wpop.population[i].chrom[j].chrom[k] * 2 - 1) * np.sqrt(j*PCHROM_LEN+k+1)
        wpop.population[i].fitness = np.abs(fitness)
        for j in range(WCHROM_LEN):
            if wpop.population[i].chrom[j].fitness > wpop.population[i].fitness:
                wpop.population[i].chrom[j].fitness = wpop.population[i].fitness

#初期化
ppop = PartialPopulation()
wpop = WholePopulation()
evaluate_fitness()
