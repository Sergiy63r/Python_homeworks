class Mailing:
    
    to_address = "Address"
    from_address = "Address"
    cost = int()
    track = str()

    def __init__(self, to_address, from_address):
        self.to_address = to_address
        self.from_address = from_address

    def track(self, track, cost):
         print(track, 'Из', self.to_address, 'в', self.from_address, 'Итого: ', cost)

