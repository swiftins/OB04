class Bird():
    def __init__(self, name):
        self.name = name
    def fly(self):
        print("bird is flying")
class Ping(Bird):
    pass
p = Ping ("Sara")
p.fly()
# код работает не совсем верно. Пингвины не летают.

class Bird():
    def fly(self):
        print("bird is flying")
class Duck(Bird):
    def fly(self):
        print("Flying very fast")
def fly_in_the_sky(animal):
    animal.fly()
b = Bird()
d = Duck()
fly_in_the_sky(b)
fly_in_the_sky(d)