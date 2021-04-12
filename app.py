from model.DNA import DNA
from Evaluator import Evaluator
from Factory import Factory
from Helper import Helper

DNA_strand = [
    DNA('Saco de dormir', 15, 15), 
    DNA('Corda', 3, 7),
    DNA('Canivete', 2, 10), 
    DNA('Tocha', 5, 5), 
    DNA('Garrafa', 9, 8), 
    DNA('Comida', 20, 17)
]


factory = Factory(DNA_strand)
population = factory.create_population()
Helper.display_population(population)

population.modify_population([])
Helper.display_population(population)

population.modify_population([])
Helper.display_population(population)
