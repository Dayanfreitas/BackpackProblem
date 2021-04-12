from functools import reduce
import random

class Helper:

    def is_valid_point ():
        pass

    def multi_dna_of_valid(genoma):
        print(genoma)

    @staticmethod
    def get_pair_number():
        return 4

    @staticmethod
    def random_contains():
        random_number = random.randint(0,9)
        if random_number % 2 == 0:
            return True
        else:   
            return False


    def display_population(population):
        print("\n\n\n")
        print(f"População : {population}")
        for individual in population.list_individual:
            genome_backpack = individual.chromosomes.chain.get('mochila')
            
            print(f"Individual #{individual.id}")
            for dna in genome_backpack.dna_strand:
                print(dna)
            print("-"*10)
            print(f"\t\t KG: {genome_backpack.weight}\t\t Pontos: {genome_backpack.points}")
            print("\n\n\n")

