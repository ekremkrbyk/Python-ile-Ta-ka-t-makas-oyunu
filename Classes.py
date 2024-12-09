from abc import ABC, abstractmethod
from typing import override
import random as rd

class ComputerPlayer(ABC) :
    def __init__(self,isim,strateji):
        self.isim = isim
        self.strateji = strateji
    def getIsim(self):
        return self.isim
    def getStrateji(self):
        return self.strateji
    def setIsim(self,value):
        if len(value) > 5 :
            self.strateji = value
        else:
            print("İsim bilgisi en az 5 karakter olmalıdır !")
    def setStrateji(self,value:int):
        if value <= 2: 
            self.strateji = value
        else: print("Geçersiz bilgi !")
    @abstractmethod
    def Oyna():
        pass
        

class Player(ABC) : 
    def __init__(self,isim:str,strateji:int):
        self.isim = isim
        self.strateji = strateji
    def getIsim(self):
        return self.isim
    def getStrateji(self):
        return self.strateji
    def setIsim(self,value:str):
        self.isim = value
    def setStrateji(self,value:int):
        if value <= 2:
            self.strateji = value
        else:
            print("Geçersiz strateji !")
    @abstractmethod
    def Oyna():
        pass
    
class HumanPlayer(Player):
    def __init__(self, isim, strateji):
        self.isim = isim
        self.strateji = strateji

    @override
    def Oyna(self,sayı:int):
        return sayı
    
class RandomComputerPlayer(ComputerPlayer):
    def __init__(self, isim, strateji):
        super().__init__(isim, strateji)

    @override
    def Oyna(self):
        secim = rd.randint(0,3)
        return int(secim)