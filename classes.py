class Vehicle:
    def __init__(self , make, model):
        self.make=make
        self.model= model
    def moves(self):
        print("Broooom vehicle moves")
    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}")

my_car=Vehicle("Toyota", "Corolla")
my_car.get_make_model()
my_car.moves()