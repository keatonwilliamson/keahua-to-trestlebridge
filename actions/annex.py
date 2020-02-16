# ANNEX.PY

# This module is resposible for providing the user with a menu of available biomes. Once chosen by the user, an instance of the selected biome is added to the arboretum dictionary.

# Author(s): Cassie Boyd, Ryan Crowley, Ken Boyd


import os
from arboretum import Arboretum
from biome import River, Forest, Grassland, Mountain, Coastline, Swamp, GrazingField, PlowedField, NaturalField, ChickenHouse, DuckHouse

# Function for adding a biome to the arboretum
def annex_biome(arboretum):

    # Clears the terminal of previous contents
    os.system("cls" if os.name == "nt" else "clear")

    # Printing the header
    print( ''' +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+
 |  T  R  E  S  T  L  E  B  R  I  D  G  E      F  A  R  M  |
 +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+\n''')

    # Printing menu options to the console
    # print("1. Mountain")
    # print("2. Swamp")
    # print("3. Grassland")
    # print("4. Forest")
    # print("5. River")
    # print("6. Coastline")
    print("1. Grazing Field")
    print("2. Plowed Field")
    print("3. Natural Field")
    print("4. Chicken House")
    print("5. Duck House")
    print("6. Coastline")

    # Capturing user input and assigning it to "choice" variable
#     choice = input('''
# Choose habitat to annex or
# Type M to return to the main menu.

# > ''')
    choice = input('''
Choose what you want to create.
Type M to return to the main menu.
> ''')

    # if statements check user input, when one evaluates to true the selected biome list is appended in arboretum dictionary
    # if choice == "1":
    #     mountain = Mountain("Mountain")
    #     arboretum.mountains.append(mountain)
    if choice == "1":
        grazingField = GrazingField("GrazingField")
        arboretum.grazingFields.append(grazingField)
    if choice == "2":
        plowedField = PlowedField("PlowedField")
        arboretum.plowedFields.append(plowedField)
    if choice == "3":
        naturalField = NaturalField("NaturalField")
        arboretum.naturalFields.append(naturalField)
    if choice == "4":
        chickenHouse = ChickenHouse("ChickenHouse")
        arboretum.chickenHouses.append(chickenHouse)
    if choice == "5":
        duckHouse = DuckHouse("DuckHouse")
        arboretum.duckHouses.append(duckHouse)
    if choice == "6":
        coastline = Coastline("Coastline")
        arboretum.coastlines.append(coastline)
    elif choice.lower() == "m":
        return