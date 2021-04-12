#Chromosomes
from model.DNA import DNA

#População
from model.Individual import Individual
from model.Population import Population

from Evaluator import Evaluator
from Factory import Factory

DNA_strand = [
    DNA('Saco de dormir', 15, 15), 
    DNA('Corda', 3, 7),
    DNA('Canivete', 2, 10), 
    DNA('Tocha', 5, 5), 
    DNA('Garrafa', 9, 8), 
    DNA('Comida', 20, 17)
]


factory = Factory(DNA_strand)
first_population = factory.create_population()

print("\n\n\n")
print(f"População : {first_population}")
for individual in first_population.list_individual:
    genome_backpack = individual.chromosomes.chain.get('mochila')
    
    print(f"Individual #{individual.id}")
    for dna in genome_backpack.dna_strand:
        print(dna)
    print("-"*10)
    print(f"\t\t KG: {genome_backpack.weight}\t\t Pontos: {genome_backpack.points}")
    print("\n\n\n")


