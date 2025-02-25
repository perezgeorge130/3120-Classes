class Animal:

    def __init__(self, name, animal, color): 
        self.__name = name
        self.__animal = animal
        self.color = color
        print("hello, I am", self.__name)

    def talk(self):
        print("hi")

    def animal_type(self, animal):  
        print (f"I am a {animal}")
    

    def animal_color(self, color):
        print (f"Animal color:{color}")


