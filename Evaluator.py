from functools import reduce
from Helper import Helper
import time

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
        
        # for x in range(0, 2):
        # # print(f"POPULAÇÃO {self.population.generation} -- {self.population}")
        # print(self.population)

        # for individual in self.population.list_individual:
            
        #     self.process_backpack(individual.chromosomes.chain.get('mochila'))
            
        #     individual.points = self.fitness(individual.chromosomes.chain.get('mochila'))
            
        #     print(individual)

        return

    def mutation(self):
        pass
    
    def selection(self):
        pass

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
        for individual in self.population.list_individual:
            gene_backpack = individual.chromosomes.chain.get('mochila')
            self.sum_of_fitness += gene_backpack.weight
            # print(f"sum_of_fitness: {self.sum_of_fitness}")

    def calc_previous_probability(self, weight):
        fitness = self.previous_probability + (weight / self.sum_of_fitness)
        self.previous_probability = fitness
        return fitness

    def fitness(self):
        print("> Fitness")
        time.sleep(2)
        print("\n\n")
        self.calc_total_fitness()
        for individual in self.population.list_individual:
            gene_backpack = individual.chromosomes.chain.get('mochila')
            individual.probability = self.calc_previous_probability(gene_backpack.weight)
            print(f"ID#{individual.id} | Probability# {individual.probability} | Fitness# {self.previous_probability}")

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
