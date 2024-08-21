class Address:

    def __init__(self, index, city, street, home, apartmen):
        self.index = index
        self.city = city
        self.street = street
        self.number_home = home
        self.number_apartmen = apartmen


    def __str__(self):
        return f"{self.index}, {self.city}, {self.street}, {self.number_home} - {self.number_apartmen}"

