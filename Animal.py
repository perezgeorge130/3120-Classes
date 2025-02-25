class Animal:

    def __init__(self, name, animal, color): 
        self.__name = name
        self.__animal = animal
        self.color = color
        print("hello, I am", self.__name)
        self.__type= type
        self.__sound= sound
        self.__age= age
        self.__play= play

    def talk(self):
        print("hi")

    def animal_type(self, animal):  
        print (f"I am a {animal}")
    

    def animal_color(self, color):
        print (f"Animal color:{color}")



    def play (self):
        print(f"{self.__name} plays {self.__play} for hours!")

    def age (self):
        print(f"{self.__name} is {self.__age} years old!")

    def sound (self):
        print(f"{self.__name} {self.__sound} all night long.")

    def type (self):
        print(f"{self.__name} is a {self.__type}")
    
    # describing the animal by providing the species 
    def describe(self, species):
        print(f"I am a {species} and my name is {self.__name}.") 
