class Individual:
    id = 1

    def __init__(self, chromosomes):
        self.id = Individual.id
        self.chromosomes = chromosomes
        self.probability = 0
        Individual.id+=1    

    def __str__(self):
        return f"{self.id}#\t{self.chromosomes} #Probability {self.probability}"