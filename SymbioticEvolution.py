import numpy as np

# ハイパーパラメータ
WPOP_SIZE = 200
PPOP_SIZE = 200
MAX_GENERATION = 400
WCROSSOVER_PROB = 0.1
PCROSSOVER_PROB = 0.9
WMUTATE_PROB = 0.01
PMUTATE_PROB = 0.01
WCHROM_LEN = 8
PCHROM_LEN = 8

# 部分解個体
class PartialIndividual:
    def __init__(self):
        self.chrom = np.random.randint(0, 2, PCHROM_LEN)
        self.fitness = 1000000

    def crossover(self, parent1, parent2, index1, index2):
        if index1 > index2:
            tmp = index1
            index1 = index2
            index2 = tmp
        for i in range(0, index1):
            self.chrom[i] = parent1.chrom[i]
        for i in range(index1, index2):
            self.chrom[i] = parent2.chrom[i]
        for i in range(index2, PCHROM_LEN):
            self.chrom[i] = parent1.chrom[i]

# 部分解集団
class PartialPopulation:
    def __init__(self):
        self.population = []
        for i in range(PPOP_SIZE):
            individual = PartialIndividual()
            self.population.append(individual)
    
    def crossover(self):
        for i in range(int(PPOP_SIZE * (1 - WCROSSOVER_PROB)), PPOP_SIZE):
            # 二点交叉
            parent1 = np.random.randint(0, int(PPOP_SIZE/4))
            parent2 = np.random.randint(0, int(PPOP_SIZE/4))
            index1 = np.random.randint(0, PCHROM_LEN)
            index2 = np.random.randint(0, PCHROM_LEN)
            self.population[i].crossover(self.population[parent1], self.population[parent2], index1, index2)


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
    ppop.population.sort(key=lambda individual: individual.fitness)

# 初期化
ppop = PartialPopulation()
wpop = WholePopulation()
evaluate_fitness()

# 世代交代
for i in range(MAX_GENERATION):
    print(f"第{i+1}世代")
    # 交叉
    ppop.crossover()
