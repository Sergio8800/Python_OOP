from random import choice
class Pet:
    def __new__(cls):
        # выбираем класс случайным образом
        other = choice([Dog, Bird, Cat])
        # подставляем вместо собственного класса `cls`
        # случайно выбранный `other`
        instance = super().__new__(other)
        print(f"Я {type(instance).__name__}!")
        return instance

    def __init__(self):
        print("Класс `Pet` никогда не запустится!")

class Dog:
    def communicate(self):
        print("Гав! Гав!")

class Cat:
    def communicate(self):
        print("Мяу! Мяу!")

class Bird:
    def communicate(self):
        print("Чик! Чирик!")

pet = Pet()
pet.communicate()