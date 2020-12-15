from pet import Pet, CuddlyPet

# Begin with no pets.
pets = []

main_menu = [
    "Adopt a Pet",
    "Play with Pet",
    "Feed Pet",
    "View status of pets",
    "Do Nothing",
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
    while True:
        choice = get_user_choice(main_menu)
        if choice == 1:
            pet_name = input("What would you like to name your pet? ")
            pets.append(Pet(pet_name))
            print("You now have %d pets" % len(pets))
            
main()