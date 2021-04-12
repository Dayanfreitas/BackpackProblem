class DNA:
    def __init__ (self, name, weight ,point):
        self.name   = name
        self.weight = weight
        self.point  = point
        self.contains = False

    def __str__(self):
        return f"Name - {self.name}\tPeso - {self.weight}\tPontos - {self.point}\tNa Mochila - {self.contains}"
