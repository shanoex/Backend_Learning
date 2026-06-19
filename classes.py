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

class Aeroplane(Vehicle):
    def __init__(self,make,model,faa_id):
        super().__init__(make,model)
        self.faa_id=faa_id
    def moves(self):
        print("Whoosh aeroplane files")
raphael=Aeroplane("Boeing", "747", "N12345")
raphael.get_make_model()
raphael.moves()
