import csv


class Student:

    def __init__(self, last_name: str, subjects_file="subjects.csv"):
        self.name = last_name
        # self.subjects_file = subjects_file
        self.subjects = {}
        self.all_grads = []

        with open(subjects_file, 'r', newline='', encoding='utf-8') as f:
            csv_file = csv.DictReader(f, fieldnames=["Математика", "Физика","История","Литература"], restkey="new", restval="No definition" ,
                                  delimiter=' ', quoting=csv.QUOTE_NONNUMERIC)
            self.all_grads = csv_file.fieldnames
            for line in csv_file:
                self.subjects[self.name] = line

    # def __setattr__(self, last_name, value):
    #     if last_name == 'name':
    #         self.__dict__["name"] = value
    #         # print(last_name, value)
    #         # print("!!!!!!!!!!!!!!!!!")
    #         # print(self.__dict__)
    #     if last_name == "subjects_file":
    #         print("+++++++++++++++")
    #         self.__dict__["subjects_file"] = value
    #         with open(self.__dict__["subjects_file"], 'r', newline='', encoding='utf-8') as f:
    #             csv_file = csv.DictReader(f, fieldnames=["Математика", "Физика", "История", "Литература"],
    #                                       restkey="new", restval="No definition",
    #                                       delimiter=' ', quoting=csv.QUOTE_NONNUMERIC)
    #             for line in csv_file:
    #                 self.subjects[self.name] = line
        # if value != "smith":
        #     print("ФИО должно состоять только из букв и начинаться с заглавной буквы")
        #     raise AttributeError("недопустимое имя атрибута")
        # else:
        #     self.__dict__["name"] = value
        #     # object.__setattr__(self, last_name, value)

    @property
    def last_name(self):
        if self.name != self.name.capitalize():
            print("ФИО должно состоять только из букв и начинаться с заглавной буквы")
        else:
            return self.name

    @last_name.setter
    def last_name(self, name):
        if not isinstance(name, str):
            raise ValueError('Должна быть строка')
        self.name = name

    def get_file(self):
        for row in self.subjects:
            # print(', '.join(row))
            print(row)

    def add_grade(self, obj:str, grade:int):
        if obj in self.all_grads:
            pass
        else:
            print(f'Предмет {obj} не найден')
        if grade in range(1,6):
            pass
        else:
            print("Оценка должна быть целым числом от 2 до 5")
    def add_test_score(self, obj:str, grade:int):
        if obj in self.all_grads:
            pass
        else:
            print(f'Предмет {obj} не найден')
        if grade in range(-1, 101):
            pass
        else:
            print("Результат теста должен быть целым числом от 0 до 100")
    def get_average_grade(self):
        pass
    def get_average_test_score(self, obj:str):
        pass
    def __str__(self):
        # nm = self.subjects.keys()
        # dt = self.subjects.values()
        name = self.name
        grade = self.subjects.pop(self.name)
        grade_list = []
        for key, value in grade.items():
            grade_list.append((key,value))
            # print(grade_list)
        return f'Студент: {name}\nПредметы:{grade}'


if __name__ == "__main__":
    # person = Student('smith')
    # person.last_name
    # print(person.subjects)
    # person.add_grade("Математика", 5)
    # person.add_test_score("Математика", 100)
    # print(person)
    student = Student("Иван Иванов", "subjects.csv")

    student.add_grade("Математика", 4)
    student.add_test_score("Математика", 85)

    student.add_grade("История", 3)
    student.add_grade("История", 4)
    student.add_test_score("История", 92)

    average_grade = student.get_average_grade()
    print(f"Средний балл: {average_grade}")

    average_test_score = student.get_average_test_score("Математика")
    print(f"Средний результат по тестам по математике: {average_test_score}")

    print(student)