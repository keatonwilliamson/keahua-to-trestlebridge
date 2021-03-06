# ICONTAINSANIMALS.PY
#
# This file is an interface for biomes containing
# animals. It keeps a count of current animals, a
# max amount allowed, a check to see if it's full,
# and a function to add a new animal to the
# animals dictionary
#
# Author(s): Ken Boyd


class IContainsAnimals:
    def __init__(self, maximum_animals=0):
        self.__animals = dict()
        self.__maximum_animals = maximum_animals
        self.__current_animals = 0

    @property
    def animals(self):
        return self.__animals

    @property
    def maximum_animals(self):
        return self.__maximum_animals

    def is_animals_full(self):
        return self.__current_animals >= self.__maximum_animals

    @property
    def current_animals(self):
        return self.__current_animals

    def add_animal_to_list(self, animal):
        if animal.species not in self.animals.keys():
            self.animals.update({f"{animal.species}": [animal]})
        else:
            self.animals[animal.species].append(animal)
        self.__current_animals += 1
