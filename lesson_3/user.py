class User():

    def __init__(self, first_name):
        print("Имя ", first_name)
        self.first_name = first_name


    def last_name_1(self, last_name):
        print("Фамилия ", last_name)
        self.last_name = last_name


    def full_name(self):
            print("Вас зовут ", self.first_name, self.last_name)

