# MATREE.PY
#
# This module is responsible for creating the MountainAppleTree class.
# MountainAppleTree inherits from the Plant class.
#
# Author(s): Ryan Crowley

from plants import Plant


class Sunflower(Plant):
    def __init__(self):
        Plant.__init__(self, "Sunflower", "partial", 17, "high")
        self.add_location("plowedFields")


