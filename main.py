from pets import Pet, CuddlyPet
from toy import Toy
from treat import ColdPizza, Bacon, VeganSnack
from menu import Menu
# Begin with no pets.
pets = []

main_menu = [
    "Adopt a Pet",
    "Play with Pet",
    "Feed Pet",
    "View status of pets",
    "Give a toy to all your pets",
    "Do Nothing",
]
adoption_menu = [
    "Pet",
    "Cuddly Pet"
]
treat_menu = [
    "ColdPizza",
    "Bacon",
    "VeganSnack"
]

def print_menu_error():
    print("That was not a valid coice. Try again.\n\n\n")

def choices_to_string(choice_list):
    choice_string = ""
    num = 1
    for choice in choice_list:
        choice_string += "%d: %s\n" % (num, choice)
        num += 1
    choice_string += "Please choose an option: "
    return choice_string
def get_user_choice(choice_list):
    choice = -1
    choice_string = choices_to_string(choice_list)
    while choice == -1:
        try:
            choice = int(input(choice_string))
            if choice <=0 or choice > len(choice_list):
                raise ValueError
        except ValueError:
                print_menu_error()
        return choice

def main():
    app = Menu("Please choose an option ", main_menu)
    types = Menu("Please choose the type of pet: ", adoption_menu)
    treats = Menu("Please choose a treat: ", treat_menu)
    while True:
        choice = app.get_choice()
        if choice == 1:
            pet_name = input("What would you like to name your pet? ")
            type_choice = types.get_choice()
            if type_choice == 1:
                pets.append(Pet(pet_name))
            elif type_choice == 2:
                pets.append(CuddlyPet(pet_name))
            print("You now have %d pets" % len(pets))
        if choice == 2:
            for pet in pets:
                pet.get_love()
        if choice ==3:
            for pet in pets:
                pet.eat_food()
        if choice == 4:
            for pet in pets:
                print(pet)
        if choice == 5:
            for pet in pets:
                pet.get_toy(Toy())
        if choice == 6:
            # Pet levels naturally lower.
            for pet in pets:
                pet.be_alive()
        if choice == 7:
            treat_choice = treats.get_choice()
            if treat_choice == 1:
                for pet in pets:
                    pet.eat_treat(ColdPizza())
            if treat_choice == 2:
                for pet in pets:
                    pet.eat_treat(Bacon())
            if treat_choice == 3:
                for pet in pets:
                    pet.eat_treat(VeganSnack())
        

main()