# INDEX.PY
#
# This module is responsible for running the application. This module is
# specifically responsible for establishing the initial view and menu for
# the user.
#
# Author(s): Ken Boyd, Cassie Boyd, Lauren Riddle, James Chapman, Ryan Crowley

import os
from uuid import uuid1


from arboretum import Arboretum
from actions import (
    annex_biome,
    release_animal,
    build_facility_report,
    cultivate_plant,
    feed_animal,
    create_animal_one_habitat
)
from plants import (
    Plant,
    RainbowEucalyptusTree,
    Sliversword,
    MountainAppleTree,
    BlueJadeVine,
)

from animals import (
    RiverDolphin,
    nenegoose,
    Ulae,
    Kikakapu,
    Pueo,
    Opeapea,
    HHFSpider,
    GDDGecko,
)



keahua = Arboretum("Keahua Arboretum", "123 Paukauila Lane")

# os.system("say Welcome to Arboretum!" if os.name != "nt" else "cls")

def build_menu():
    os.system("cls" if os.name == "nt" else "clear")
    print( ''' +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+
 |  K  e  a  h  u  a    A  r  b  o  r  e  t  u  m  |
 +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+\n''')
    print("1. Create Facility")
    print("2. Purchase Animals")
    print("3. Purchase Seeds")
    # print("4. Somethin")
    print("4. Display Farm Report")
    print("5. Exit")


def main_menu():
    """Show Keahua Action Options

    Arguments: None
    """
    build_menu()
    choice = input('''
Choose a KILLER option.

>  ''')

    if choice == "1":
        annex_biome(keahua)

    if choice == "2":
        release_animal(keahua)

    if choice == "3":
        cultivate_plant(keahua)

    # if choice == "4":
    #     feed_animal()

    if choice == "4":
        build_facility_report(keahua)
        pass

    if choice != "5":
        main_menu()


main_menu()
