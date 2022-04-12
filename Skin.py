from numpy import double

class Skin:
    __imgFile:str = None
    __description:str = None
    __cost:double = None
    __active:bool = None
    __sold:bool = None
    __name:str = None
    def __init__(self, imgFile, desc, cost, active, sold, name):
        self.__imgFile = imgFile
        self.__description = desc
        self.__cost = cost
        self.__active = active
        self.__sold = sold
        self.__name = name
        return
    def renderImage():
        pass
    def getDesc(self) -> str:
        return self.__description
    def getCost(self) -> double:
        return self.__cost
    def isActive(self) -> bool:
        return self.__active
    def isSold(self) -> bool:
        return self.__sold
    def getName(self) -> str:
        return self.__name
    