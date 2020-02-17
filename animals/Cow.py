# Authors: Lauren and James
# defines a class for creating the GDDGecko
from animals import Animal
from interfaces import IWalking
from interfaces import Identifiable
from interfaces import ITerrestrial
import os
class Cow(Animal, IWalking, ITerrestrial, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Cow")
        IWalking.__init__(self)
        Identifiable.__init__(self)
        ITerrestrial.__init__(self)
        self.__prey = { "Grass", "Hay"}

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        os.system('cls' if os.name == 'nt' else 'clear')
        print( ''' +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+
 |  K  e  a  h  u  a    A  r  b  o  r  e  t  u  m  |
 +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+\n''')
        if prey in self.__prey:
            print(f"The Cow ate {prey} for a meal\n")
            input("Press any button to continue...")
        else:
            print(f"The Cow rejects the {prey}")


    def __str__(self):
        return f"Cow {self.id}. I want more Grass dude!"