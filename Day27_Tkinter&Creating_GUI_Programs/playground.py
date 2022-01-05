def add(*args):
    return sum(args)

print(add(1,2,3,4,5,6,7,10))

class Car:
    def  __init__(self,**kw):
        self.make = kw["make"]
        self.model = kw["model"]
        self.color = kw["color"]
        self.seats = kw["seats"]

my_car = Car(make="Nissan",model="GTR")
print(my_car.model)