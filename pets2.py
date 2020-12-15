class Pet:
    def __init__(self, name, fullness=50, happiness=50, hunger=5, mopiness=5):
        self.name = name
        self.fullness = fullness
        self.happiness = happiness
        self.hunger = hunger
        self.mopiness = mopiness
    
    def eat_food(self):
        self.fullness += 30
    
    def get_love(self):
        self.fullness += 30
    
    def be_alive(self):
        self.fullness -= self.hunger
        self.happiness -= self.mopiness


class CuddlyPet(Pet):
    def __init__(self, name, fullness=50, happiness=50, hunger=5, mopiness=5):
        self.name = name
        self.fullness = fullness
        self.happiness = 100
        self.hunger = hunger
        self.mopiness = 1
        
    def be_alive(self):
        self.fullness -= self.hunger
        self.happiness -= self.mopiness/2

    def cuddle(self, other_pet):
        other_pet.get_love()



benji = CuddlyPet("Benji", 50, 20, 20, 1)
cujo = Pet("Cujo", 50, 10, 30, 10) # CUJO IS DIFFERENT FROM BENJI BECAUSE HE IS NOT AS HAPPY AS BENJI TO START OFF.
print(cujo.happiness)
# 10
benji.cuddle(cujo)
print(cujo.happiness)
# 40    BUT FOR SOME REASON IM ONLY GETTING 10
