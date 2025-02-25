class Animal:

    def __init__(self, name, kind, color, kind, age=1, weight=5): 
        self.__name = name
        self.__age = age
        self.__weight = weight
        self.__kind = kind
        self.__animal = animal
        self.__color = color
        print(f"hello, I am {self.__name} and I am a {self.__kind}")
        self.__type= type
        self.__sound= sound
        self.__age= age
        self.__play= play

    def born(self, name, kind):
        print(f"Hello world!, my name is {self.__name}. I am a {self.__kind} and I am {self.__age}")
    
    def weight(self):
        print(f'My current weight is {self.__weight}')
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

    def gain(self, weight):
        self.__weight+=weight
        print(f'I gained {weight} pounds. Current weight: {self.__weight}')