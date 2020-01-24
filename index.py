import os
from uuid import uuid1


from arboretum import Arboretum
from actions import (
    annex_biome,
    release_animal,
    build_facility_report,
    cultivate_plant,
    feed_animal,
)
from plants import (
    Plant,
    RainbowEucalyptusTree,
    Sliversword,
    MountainAppleTree,
    BlueJadeVine
)

from animals import (RiverDolphin, nenegoose, Ulae, Kīkākapu, Pueo, Opeapea, HHFSpider, GDDGecko)



keahua = Arboretum("Keahua Arboretum", "123 Paukauila Lane")

def build_menu():
    os.system("cls" if os.name == "nt" else "clear")
    print("1. Annex Habitat")
    print("2. Release Animal into Habitat")
    print("3. Feed Animal")
    print("4. Add Plant to Habitat")
    print("5. Display Facility Report")
    print("6. Exit")


def main_menu():
    """Show Keahua Action Options

    Arguments: None
    """
    build_menu()
    choice = input(">> ")

    if choice == "1":
        annex_biome(keahua)


    if choice == "2":
        release_animal(keahua)

    if choice == "3":
        feed_animal(keahua)

    if choice == "4":
        cultivate_plant(keahua)

    if choice == "5":
        build_facility_report(keahua)
        pass

    if choice != "6":
        main_menu()


main_menu()
