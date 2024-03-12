"""
Задание №3
📌 Добавьте к задачам 1 и 2 строки документации для классов.
"""

"""
MyStr - class, наследует все возможности класса str
также имеет дополнительные атрибуты
"""

# для def __new__(cls, value, author_name):
"""
Создает экземпляр класса с дополнительными атрибутами
value: Переданная строка
author_name: имя автора-создателя
creation_time = datetime.datetime.now() - время создания
"""

"""
класс Archive хранит свойства:
число и строку, а также list-архивы предыдущих экземпляров класса.
При нового экземпляра класса, старые данные из ранее созданных экземпляров 
сохраняются в два списковархивов
"""


class Archive:
    """
    класс Archive хранит свойства:
    число и строку, а также list-архивы предыдущих экземпляров класса.
    При нового экземпляра класса, старые данные из ранее созданных экземпляров
    сохраняются в два списковархивов
    """
    nums_archive = []
    strs_archive = []
    last_num = None
    last_str = None

    def __init__(self, num, new_str):
        self.num = num
        self.new_str = new_str

        if Archive.last_num is not None:
            Archive.nums_archive.append(Archive.last_num)
        if Archive.last_str is not None:
            Archive.strs_archive.append(Archive.last_str)

        Archive.last_num = num
        Archive.last_str = new_str


cl_a = Archive(33, "класс Archive")
print(cl_a.__doc__)
