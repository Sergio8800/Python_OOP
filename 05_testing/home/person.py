class Human:

    def __init__(self, last_name, first_name, age):
        self._last_name = last_name
        self._first_name = first_name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value > 70:
            raise ValueError('староват')
        self.__age = value

    def up_birthday(self):
        self.__age += 1

    def get_fullname(self):
        return f'{self._last_name}, {self._first_name}'


if __name__ == "__main__":
    person = Human('Smith', 'Johan', 80)

    # print(person._first_name)
    # # print(person.__age())
    # print(person.age)
    # person.up_birthday()
    # print(person.age)
    # print(person.get_fullname())
    #
    person.age = 70
    print(person.age)