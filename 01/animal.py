import sys


class Animal:
    def __init__(self, name: str):
        self.name = name


class Bird(Animal):
    def __init__(self, wingspan: int, name: str):
        super().__init__(name)
        self.wingspan = wingspan

    def wing_length(self):
        return print(self.wingspan)


class Fish(Animal):
    def __init__(self, max_depth: int, name: str):
        super().__init__(name)
        self.max_depth = max_depth

    def depth(self):
        if self.max_depth < 10:
            print("Мелководная рыба")
        elif 10 < self.max_depth < 100:
            print("Средневодная рыба")
        elif 100 < self.max_depth:
            print("Глубоководная рыба")


class Mammal(Animal):
    def __init__(self, weight: int, name: str):
        super().__init__(name)
        self.weight = weight

    def category(self):
        if self.weight < 1:
            print("Малявка")
        elif 1 < self.weight < 200:
            print("Обычный")
        elif 200 < self.weight:
            print("Гигант")


class AnimalFactory:
    
    def __new__(cls):
        LIST_CR = {'Bird': Bird, 'Fish': Fish, 'Mammal': Mammal}
        instance = super().__new__(LIST_CR['Bird'])
        print(f"Я {type(instance).__name__}!")
        
    # def __init__(self, animal_type: str):
    #     self.animal_type = animal_type
    #     # self.args = args
    #     # self.kwadrgs = kwargs

    # def write(self):
    #     print(self.name)

    def create_animal(self):
        # print(self.animal_type.capitalize())
        # class_object = globals()[self.animal_type.capitalize()]()
        # class_object = getattr(sys.modules[__name__], self.animal_type)()
        class_name = "Bird"
        class_object = getattr(sys.modules[__name__], class_name)()
        class_object3=class_object()
        if self.animal_type in self.LIST_CR.keys():

            print(self.animal_type.capitalize())
            # module = sys.modules[__name__]
            # class_ = getattr(module, self.animal_type.capitalize())
            # instance = class_()
            # instance.write()
            class_ = globals()[self.animal_type.capitalize()]()


        return class_object3

an = AnimalFactory()
# an1 = an.create_animal()
print(an)





