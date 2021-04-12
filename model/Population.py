
class Population:
    generation = 1
    
    def __init__(self, list_individual):
        self.list_individual = list_individual
    
    def modify_population(self, list_individual):
        self.increment_generation()
        self.list_individual = list_individual

    def increment_generation(self):
        Population.generation += 1
    
    def __str__(self):
        return f"POPULAÇÃO (GERAÇÃO {self.generation})"