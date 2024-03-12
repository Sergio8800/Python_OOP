from json import load, dump
from users_class import User


class NameError(Exception):
    pass


class LevelError(Exception):
    pass


class Repo:
    users = []

    @staticmethod
    def load_users(path):
        with open(path, encoding='utf-8') as f:
            data = load(f)
            for level, value in data.items():
                for id, name in value.items():
                    Repo.users.append(User(name, id, level))

    @staticmethod
    def check_login(name):
        try:
            for user in Repo.users:
                if user.name == name:
                    return f"{name} Пользователь найден!"
            raise NameError
        except NameError:
            return f'{name} - Пользователь не найден'

    @staticmethod
    def create_user(name, id_user, level):
        try:
            if level > 3:
                raise LevelError
        except LevelError:
            return 'Ошибка уровня'
        else:
            Repo.users.append(User(name, id_user, level))


if __name__ == '__main__':
    repo = Repo()
    repo.load_users('user.json')
    # print(repo.check_login('Новиков'))
    repo.create_user('Семенов', '8', 3)
    repo.load_users('user.json')
    print(*repo.users, sep='\n')
    print(repo.check_login("Семенов"))
    print(repo.check_login("Ivanov"))
    print(repo.users[0] == repo.users[0])
