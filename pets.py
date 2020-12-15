class Pet:
    def __init__(self, name, fullness=50, happiness=50, hunger=5, mopiness=5):
        self.name = name
        self.fullness = fullness
        self.happiness = happiness
        self.hunger = hunger
        self.mopiness = mopiness
        self.toys = []

    def eat_food(self):
        self.fullness += 30

    def get_love(self):
        self.happiness +=30
    
    def be_alive(self):
        self.fullness -= self.hunger
        self.happiness -= self.mopiness
        for toy in self.toys:
            self.happiness += toy.use()
    
    def get_toy(self, toy):
        self.toys.append(toy)

    def eat_treat(self, treat):
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

    def be_alive(self): # REDEFINE be_alive() for CuddlyPet - CuddlyPet stays happy for twice as long as Pet
        super().be_alive()
        self.happiness -= self.mopiness/2

    def cuddle(self, other_pet):
        for i in range(self.cuddle_level):
            other_pet.get_love()
    
    def __str__(self):
        return """
        Extra Cuddly %s:
        Fullness: %d
        Happiness: %d
        """ % (self.name, self.fullness, self.happiness)

class Dog(Pet):
    def bark(self): # bark is a method that is unique to Dog
        return "Woof Woof"

class Cat(Pet):
    def meow(self):
        return "Meow"

# benji = CuddlyPet("Benji", 50, 20, 20, 1) #Benji is an extension, not just a Pet. Benji is a type of Pet, a CuddlyPet
# ralphie = Dog("Ralphie") # Ralphie is a Dog is a Pet
# gus = Cat("Guster") # Gus is a Cat is a Pet





# # Define a dictionary that holds our pet's attributes.
# puppy = {
#     "name": "Cujo",
#     "fullness": 50,
#     "happiness": 20,
# }

# # Define functions that increase a pet's attribute levels.
# def feed_pet(pet):
#     pet["fullness"] += 10


# def play_with_pet(pet):
#     pet["happiness"] += 10

# # Decrease a pet's attribute levels.
# def get_hungry_and_mopey(pet):
#     pet["fullness"] -= 5
#     pet["happiness"] -= 5


# # Prompt the user to interact with the pet
# while True:

#     print("""
# %s's stats:
# Fullness: %d
# Happiness: %d
# """ % (puppy["name"], puppy["fullness"], puppy["happiness"]))

#     choice = int(input("""
# 1. Feed puppy
# 2. Play with puppy
# 3. Do nothing
# """))
#     if choice == 1:
#         feed_pet(puppy)
#     elif choice == 2:
#         play_with_pet(puppy)
#     else:
#         pass

#     # Each time the loop runs, the pet
#     # will need some attention!
#     get_hungry_and_mopey(puppy)


