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
    pass



benji = CuddlyPet("Benji", 50, 20, 20, 1)
cujo = Pet("Cujo", 50, 10, 30, 10) # CUJO IS DIFFERENT FROM BENJI BECAUSE HE IS NOT AS HAPPY AS BENJI TO START OFF.
print(benji.fullness, benji.happiness)
# 50 20
benji.be_alive()
print(benji.fullness, benji.happiness)
# 30 19
