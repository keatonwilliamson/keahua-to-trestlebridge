from interfaces import Identifiable
from interfaces import IContainsAnimals
from interfaces import IContainsPlants
from .biome import Biome


class Grassland(IContainsAnimals, IContainsPlants, Identifiable, Biome):
    def __init__(self, name):
        IContainsAnimals.__init__(self, 22)
        IContainsPlants.__init__(self, 15)
        Identifiable.__init__(self)
        Biome.__init__(self, name)

    def add_animal(self, animal):
        # Add in checks for animal type
        self.add_animal_to_list(animal)

    def add_plant(self, plant):
        # Add in checks for plant type
        self.add_plant_to_list(plant)

