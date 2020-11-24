class animal(object):
    def run(self):
        print("animal can run")

class dog(animal):
    def eat(self):
        print("dog can eat")

class cat:
    def eat(self):
        print("cat can eat")
    def __add__(self, other):
        return other


tommy=dog()
tommy.run()
tommy.eat()
catty=cat()
a=catty.__add__(tommy)
print(a)
print(isinstance(cat,animal))
print(type(tommy))