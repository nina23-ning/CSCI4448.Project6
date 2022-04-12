import Skin

class Player:
    __skin:Skin = None
    __instance = None
    def __new():
        if (instance == None):
            instance = Player()