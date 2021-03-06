# Author: Lauren Riddle
# Purpose: Holds the choices that call the create a new animal function
from animals import RiverDolphin, nenegoose, Ulae, Kikakapu, Pueo, Opeapea, HHFSpider, GDDGecko
from animals import Chicken, Duck, Cow, Goat, Ostrich, Pig, Sheep
import os
from .create_animal import create_animal_two_habitats, create_animal_one_habitat
def release_animal(arboretum):
    animal = None
    # clears the screen
    os.system("cls" if os.name == "nt" else "clear")

    # Printing the header
    print( ''' +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+
 |  K  e  a  h  u  a    A  r  b  o  r  e  t  u  m  |
 +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+\n''')

    # creates the add animal menu
    # print("1. River Dolphin")
    # print("2. Gold Dust Day Gecko")
    # print("3. Nene Goose")
    # print("4. Kikakapu")
    # print("5. Pueo")
    # print("6. 'Ulae")
    # print("7. Ope'ape'a")
    # print("8. Happy-Face Spider")

    print("1. Chicken")
    print("2. Cow")
    print("3. Duck")
    print("4. Goat")
    print("5. Ostrich")
    print("6. Pig")
    print("7. Sheep")
    # print("8. Happy-Face Spider")


    # Capturing user input and assigning it to "choice" variable
    choice = input('''
Choose an animal to release or
Type M to return to the main menu.

> ''')

    if choice == "1":
        animal = Chicken()
        create_animal_one_habitat(arboretum.chickenHouses, arboretum, animal)


    if choice == "2":
        os.system("cls" if os.name == "nt" else "clear")
        animal = Cow()
        create_animal_one_habitat(arboretum.grazingFields, arboretum, animal)


    if choice == "3":
        os.system("cls" if os.name == "nt" else "clear")
        animal = Duck()
        create_animal_one_habitat(arboretum.duckHouses, arboretum, animal)
        

    if choice == "4":
        os.system("cls" if os.name == "nt" else "clear")
        animal = Goat()
        create_animal_one_habitat(arboretum.grazingFields, arboretum, animal)


    if choice == "5":
        os.system("cls" if os.name == "nt" else "clear")
        animal = Ostrich()
        create_animal_one_habitat(arboretum.grazingFields, arboretum, animal)


    if choice == "6":
        os.system("cls" if os.name == "nt" else "clear")
        animal = Pig()
        create_animal_one_habitat(arboretum.grazingFields, arboretum, animal)
       
    if choice == "7":
        os.system("cls" if os.name == "nt" else "clear")
        animal = Sheep()
        create_animal_one_habitat(arboretum.grazingFields, arboretum, animal)

    # if choice == "8":
    #     os.system("cls" if os.name == "nt" else "clear")
    #     animal = HHFSpider()
    #     create_animal_one_habitat(arboretum.swamps, arboretum, animal)