
class Population:
    generation = 1
    
    def __init__(self, list_individual):
        self.list_individual = list_individual
        self.current_best_individual = None
    
    def modify_population(self, list_individual):
        self.increment_generation()
        self.list_individual = list_individual

    def increment_generation(self):
        Population.generation += 1

    def getBestIndividual(self):
        def testOrden(individual):
            genome_backpack = individual.chromosomes.chain.get('mochila')
            return genome_backpack.points

        return sorted(self.list_individual, key=testOrden, reverse=True)[0]

    def setBestCurrentIndividual(self, individual):
        self.current_best_individual = individual
    
    def __str__(self):
        return f"POPULAÇÃO (GERAÇÃO {self.generation})"