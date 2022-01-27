import functions as func


class UserPattern:
    def __init__(self, first_name, last_name, email, phone, location):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.location = location


class ManagementPattern():
    def __init__(self, access_level):
        self.access_level = access_level


class Guest(UserPattern):
    def __init__(self, first_name, last_name, email, phone, location):
        super().__init__(first_name, last_name, email, phone, location)


class User(UserPattern):
    def __init__(self, first_name, last_name, email, phone, location):
        super().__init__(first_name, last_name, email, phone, location)
        self.username = ''
        self.password = ''

    def set_username(self):
        self.username = str(f'{self.first_name.lower()}.{self.last_name.lower()}')
        return self.username

    def set_password(self):
        self.password = str(f'{func.get_random_password(15)}')
        return self.password

    def set_corporate_email(self):
        return str(f'{User.set_username(self)}@hsbc-{self.location}.com').lower()


class Admin(UserPattern, ManagementPattern):
    def __init__(self, first_name, last_name, email, phone, location, access_level):
        super(UserPattern, self).__init__(first_name, last_name, email, phone, location)
        super(ManagementPattern, self).__init__(access_level)


u = User('Maksym', 'Bondaruk', 'mb@gmail.com', 888555999, 'Ukraine')
print(u.set_username())
print(u.set_password())