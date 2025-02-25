class Animal:
    def __init__(self, name, kind, age=1, weight=5):
        self.__name = name 
        self.__age = age
        self.__weight = weight
        self.__kind = kind
        print(f"hello, I am {self.__name} and I am a {self.__kind}")

    def born(self, name, kind):
        print(f"Hello world!, my name is {self.__name}. I am a {self.__kind} and I am {self.__age}")
    
    def weight(self):
        print(f'My current weight is {self.__weight}')

    def gain(self, weight):
        self.__weight+=weight
        print(f'I gained {weight} pounds. Current weight: {self.__weight}')