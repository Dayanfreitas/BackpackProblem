from functools import reduce
from Helper import Helper
import random

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
        self.fitness()
        [a,b] = self.selection()
        self.mutation(a, b)
        return

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
                return [individual, index]
            
    def mutation(self, a, b):
        print("> Mutação....")

        print(f"{a.get('DNA')}")
        print(f"{b.get('DNA')}")
        
        print(f"{a.get('index')}")
        print(f"{b.get('index')}")
        pass
    
    def selection(self):
        [individualA, indexA] = self.roulette()
        [individualB, indexB] = self.roulette()
        
        gene_backpackA = individualA.chromosomes.chain.get('mochila').dna_strand
        gene_backpackB = individualB.chromosomes.chain.get('mochila').dna_strand
        
        return [{'DNA': gene_backpackA, 'index': indexA}, {'DNA': gene_backpackB, 'index': indexB}]

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

        # return Evaluator.fitness(individual)
