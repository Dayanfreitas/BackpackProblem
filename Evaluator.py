from functools import reduce
from Helper import Helper
from model.Genome import Genome
from model.Chromosomes import Chromosomes 
from model.Individual import Individual
import random
import copy


class Evaluator:
    def __init__(self, population):
        self.population = population
        self.sum_of_fitness = 0
        self.previous_probability = 0.0
        self.finish = False
    # def get_sum_of_fitness(population):
    #     pass

    def process_better_individual(self):
        Helper.display_population(self.population)
 

        while not self.isFinish():
            self.fitness()
            arr = []
            newPopulation = []

            for i in self.population.list_individual:
                arr.append(self.selection())
                print(f"conta: {i}")

            for i in range(0,len(arr),2):
                [indA,indB] = self.mutation(arr[i], arr[i+1])
                newPopulation.append(indA)
                newPopulation.append(indB)
            print(f"LISTA ANTIGA: {self.population.list_individual}")
            print(f"LISTA NOVA: {newPopulation}")
            break

        # [a,b] = self.selection()
        # [indA,indB] = self.mutation(a, b)
        # self.population.list_individual.append(indA)
        # self.population.list_individual.append(indB)
        # Helper.display_population(self.population)
        return self.population.current_best_individual

    def roulette(self):
        point = random.random()
        interval = {'a': None, 'b': None }

        for index, individual in enumerate(self.population.list_individual, start=0):
            if index == 0:
                interval['a'] = 0
            else:
                previous = self.population.list_individual[index - 1]
                interval['a'] = previous.probability

            interval['b'] = individual.probability

            if point > interval['a'] and point <= interval['b']:
                #del(self.population.list_individual[index])
                return [individual, index]
            
    def mutation(self, a, b):
        #Helper.display_population(self.population)
        print("> Mutação....")
        
        ind = []

        while True:
            cadeiaA = copy.deepcopy(a.get('DNA'))
            cadeiaB = copy.deepcopy(b.get('DNA'))
            
            index_random = random.randint(0, len(cadeiaA) - 1)
            print(index_random)

            print(cadeiaA[index_random].contains)
            print(cadeiaB[index_random].contains)

            #individual = Individual(chromosomes )        
            aux = cadeiaA[index_random].contains
            cadeiaA[index_random].contains = cadeiaB[index_random].contains
            cadeiaB[index_random].contains = aux

            chromosomesA = Chromosomes()
            chromosomesB = Chromosomes()
            chromosomesA.add_gene(Genome('mochila', cadeiaA, 30))
            chromosomesB.add_gene(Genome('mochila', cadeiaB, 30))

            individualA = Individual(chromosomesA)
            individualB = Individual(chromosomesB)

            if  Evaluator.individual_is_valid(individualA) and Evaluator.individual_is_valid(individualB):
                ind.append(individualA)
                ind.append(individualB)
                break

        return ind

        #print(f"{a.get('DNA')}")
        #print(f"{b.get('DNA')}")
        
        #print(f"{a.get('index')}")
        #print(f"{b.get('index')}")
        pass
    
    def selection(self):
        [individualA, indexA] = self.roulette()
        
        gene_backpackA = individualA.chromosomes.chain.get('mochila').dna_strand
        
        return {'DNA': gene_backpackA, 'index': indexA}

    def process_backpack(self, chromosomes_backpack):
        print("\n")
        print(f"Cromossomos Mochila {chromosomes_backpack}")
        print("\n")
        print("DNA TRADUZIDO")

        for x in chromosomes_backpack:
            # x.contains = radom_contains()
            
            print(x)

        return 

    def calc_total_fitness(self):
        print("+- Calculando o Fitness total da população")
        # Helper.loading()
        for individual in self.population.list_individual:
            gene_backpack = individual.chromosomes.chain.get('mochila')
            self.sum_of_fitness += gene_backpack.points
            # print(f"sum_of_fitness: {self.sum_of_fitness}")

    def calc_previous_probability(self, points):
        fitness = self.previous_probability + (points / self.sum_of_fitness)
        self.previous_probability = fitness
        return fitness

    def fitness(self):
        print("+ Calculando Fitness")
        print("|")

        self.calc_total_fitness()
        # Helper.loading()

        print("\n\n")
        print("Tabela individios vs probabilidade")

        for individual in self.population.list_individual:
            gene_backpack = individual.chromosomes.chain.get('mochila')
            individual.probability  = self.calc_previous_probability(gene_backpack.points)
            print(f"ID#{individual.id} \t| Probability# {individual.probability}")
        # Helper.display_population(self.population)

    def pick_up_individual_with_probability(self, probability):
        pass
    

    @staticmethod
    def sum_points(a, b):
        if b.contains:
            return a + b.point
        return a

    @staticmethod
    def sum_weight(a, b):
        if b.contains:
            return a + b.weight

        return a

    @staticmethod
    def calulate_points(individual):
        print('calulate_points')
        return 0

    @staticmethod
    def calulate_weight(individual):
        print('calulate_weight')
        return 0

    @staticmethod
    def individual_is_valid(individual):
        print(f"Individual : {individual}")

        genome_backpack = individual.chromosomes.chain.get('mochila')
        print(f"chromosomes {individual.chromosomes}")

        points = reduce(Evaluator.sum_points, genome_backpack.dna_strand, 0) 
        weight = reduce(Evaluator.sum_weight, genome_backpack.dna_strand, 0) 
        
        genome_backpack.points = points
        genome_backpack.weight = weight
        
        print(f"genome_backpack.points {genome_backpack.points}")
        print(f"genome_backpack.weight {genome_backpack.weight}")

        if genome_backpack.weight > genome_backpack.load_limit or genome_backpack.weight <= 0:
            return False
        
        return True
    
    def isFinish(self):
        individual   = self.population.getBestIndividual()
        best_current = self.population.current_best_individual

        if best_current == None:
            return False

        genome_backpack_individual = individual.chromosomes.chain.get('mochila')
        genome_backpack_current_best_individual = best_current.chromosomes.chain.get('mochila')

        isEquals = True
        for dna_ind in genome_backpack_individual.dna_strand:
            for dna_current_ind in genome_backpack_current_best_individual.dna_strand:
                if dna_ind.contains != dna_current_ind.contains:
                    isEquals = False

        print('---------------------')
        print(f'Finish:  { isEquals}')
        print('---------------------')
        self.population.setBestCurrentIndividual(individual)
        return isEquals

        # return Evaluator.fitness(individual)
