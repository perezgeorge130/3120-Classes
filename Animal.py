class Animal:
    def __init__(self, name):
        self.__name = name 
        print("hello, I am", self.__name)

    def talk(self):
        print("hi")
    
    # describing the animal by providing the species 
    def describe(self, species):
        print(f"I am a {species} and my name is {self.__name}.") 