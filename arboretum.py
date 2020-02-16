# ARBORETUM.PY
#
# This file is responsible for defining the arboretum base
# class that holds the lists of each annexed biome
#
# Author(s): Ken Boyd


class Arboretum:
    def __init__(self, name, address):
        self.__name = name
        self.__address = address
        self.__biomes = {
            # "rivers": [],
            # "coastlines": [],
            # "forests": [],
            # "grasslands": [],
            # "mountains": [],
            # "swamps": [],
            "grazingFields": [],
            "plowedFields": [],
            "naturalFields": [],
            "chickenHouses": [],
            "duckHouses": []
        }

    @property
    def grazingFields(self):
        return self.__biomes["grazingFields"]
    @property
    def plowedFields(self):
        return self.__biomes["plowedFields"]
    @property
    def naturalFields(self):
        return self.__biomes["naturalFields"]
    @property
    def chickenHouses(self):
        return self.__biomes["chickenHouses"]
    @property
    def duckHouses(self):
        return self.__biomes["duckHouses"]


    # @property
    # def name(self):
    #     return self.__name

    # @property
    # def address(self):
    #     return self.__address

    # @property
    # def rivers(self):
    #     return self.__biomes["rivers"]

    # @property
    # def coastlines(self):
    #     return self.__biomes["coastlines"]

    # @property
    # def forests(self):
    #     return self.__biomes["forests"]

    # @property
    # def grasslands(self):
    #     return self.__biomes["grasslands"]

    # @property
    # def mountains(self):
    #     return self.__biomes["mountains"]

    # @property
    # def swamps(self):
    #     return self.__biomes["swamps"]

    @property
    def biomes(self):
        return self.__biomes
