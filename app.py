import functions as func
from abc import ABC, abstractmethod


class UserPattern(ABC):
    def __init__(self, full_name, phone_number, email_address):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email_address = email_address

    @abstractmethod
    def get_user_info(self):
        pass


class User(UserPattern):
    def __init__(self, full_name, phone_number, email_address):
        super().__init__(full_name, phone_number, email_address)

    def get_user_info(self):
        return f'{self.full_name} | {self.phone_number} | {self.email_address}'


user_x = User('James Bond', 555888999, 'jamesbond@ukr.net')
print(user_x.get_user_info())



