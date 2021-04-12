from functools import reduce

class Evaluator:
    def __init__(self, population):
        self.population = population
        self.finish = False
    
    def process_better_individual(self):
        # print(f"POPULAÇÃO {self.population.generation} -- {self.population}")
        print(self.population)

        for individual in self.population.list_individual:
            
            self.process_backpack(individual.chromosomes.chain.get('mochila'))
            
            individual.points = self.fitness(individual.chromosomes.chain.get('mochila'))
            
            print(individual)

        return

    def process_backpack(self, chromosomes_backpack):
        print("\n")
        print(f"Cromossomos Mochila {chromosomes_backpack}")
        print("\n")
        print("DNA TRADUZIDO")

        for x in chromosomes_backpack:
            # x.contains = radom_contains()
            
            print(x)

        return 

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
    def fitness(individual):
        print("Fitness !!!")
        # points = individual.chromosomes.chain.get('mochila').points
        weight = individual.chromosomes.chain.get('mochila').weight
        
        if weight > 30 or weight < 0:
            return False
        
        return True

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

        return Evaluator.fitness(individual)
