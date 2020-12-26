class Pet:
    def __init__(self, name, fullness=50, happiness=50, hunger=5, mopiness=5):
        self.name = name
        self.fullness = fullness
        self.happiness = happiness
        self.hunger = hunger
        self.mopiness = mopiness
        self.toy = []
    
    def eat_food(self):
        self.fullness += 30
    
    def get_love(self):
        self.fullness += 30
    
    def be_alive(self):
        self.fullness -= self.hunger
        self.happiness -= self.mopiness

    def get_toy(self, toy):
        self.toy.append(toy)
        self.happiness += toy.bonus

    def get_treat(self, treat):
        self.fullness += treat.yum
        self.happiness += treat.joy

    def __str__(self):
        return """
        %s:
        Fullness: %d
        Happiness: %d
        """ % (self.name, self.fullness, self.happiness)  


class CuddlyPet(Pet):
    def __init__(self, name, fullness=50, hunger=5, cuddle_level=1):
        super().__init__(name, fullness, 100, hunger, 1)
        self.cuddle_level = cuddle_level

    def be_alive(self):
        self.fullness -= self.hunger
        self.happiness -= self.mopiness/2

    def cuddle(self, other_pet):
        for i in range(self.cuddle_level):
            other_pet.get_love()

    def __str__(self):   
        return """
        Extra cuddly %s:
        Fullness: %d
        Happiness: %d
        """ % (self.name, self.fullness, self.happiness)  


# benji = CuddlyPet("Benji")
# cujo = Pet("Cujo")
# print(cujo.name, cujo.fullness, cujo.happiness, cujo.hunger, cujo.mopiness)

# benji.cuddle(cujo)
# print(cujo.name, cujo.fullness, cujo.happiness, cujo.hunger, cujo.mopiness)

