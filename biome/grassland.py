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
        if not self.is_animals_full():
            self.animals.append(animal)
            
        else:
            print("Biome is full, choose another biome")

    def add_plant(self, plant):
        if not self.is_plants_full():
            self.plants.append(plant)
            
        else:
            print("Biome is full, choose another biome")

