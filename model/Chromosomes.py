class Chromosomes:
    def __init__(self):
        self.chain = {}

    def add_gene(self, chain):
        self.chain[chain.name] = chain

    def print_chain(self):
        pass

    def __str__(self):
        list_of_genes = list(self.chain.keys())
        return f"GENES: {self.chain}"