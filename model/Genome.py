
class Genome:
    def __init__(self, name, dna_strand):
        self.name = name 
        self.dna_strand = dna_strand
        self.points = None
        self.weight = None

    def __str__(self):
        return f"GENOME:{self.name} #[dna_strand] -> {self.dna_strand} #points - {self.points} #weight - {self.weight}"