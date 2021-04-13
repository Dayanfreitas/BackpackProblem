from model.Genome import Genome
from model.Chromosomes import Chromosomes
from model.Individual import Individual
from model.Population import Population
from Evaluator import Evaluator
from Helper import Helper

import copy

class Factory:
    DNA_strand = None 
    
    def __init__(self, DNA_strand):
        Factory.DNA_strand = DNA_strand

    @staticmethod
    def create_individual():
        print("Create Individual...")
        chromosomes = Chromosomes()
        chromosomes.add_gene(Genome('mochila', copy.deepcopy(Factory.DNA_strand), 30))

        individual = Individual(chromosomes)
        Factory.process_backpack(individual.chromosomes.chain.get('mochila'))

        return individual

    @staticmethod
    def process_backpack(genome_backpack):
        print("process_process_backpack...")

        print("\n")
        print(f"Cromossomos Mochila {genome_backpack}")
        print("\n")
        print("DNA TRADUZIDO")
        
        for x in genome_backpack.dna_strand:
            x.contains = Helper.random_contains()
            print(x)

    @staticmethod
    def create_population():
        list_individual = []
        print('Create Population....')
        print("Get number population pair")

        for i in range(0, Helper.get_pair_number()): 
            individual = Factory.create_individual()

            while not Evaluator.individual_is_valid(individual):
                individual = Factory.create_individual()
            
            list_individual.append(individual)

        return Population(list_individual)
