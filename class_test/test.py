
class Animal:

    _energy = 0

    def __init__(self, name):
        self.name = name    

    def speak(self):
        print("Hello my name is " + self.name)

    def feed(self, food):
        self._energy += food
        print("Yum: {0}".format(self._energy) )

class Cat(Animal):

     def speak(self):
        Animal.speak(self)
        print("Meow my name is " + self.name)


dog = Animal("Dave")
dog.speak()
dog.feed(10)
dog.feed(3)

print("")

cat = Cat("Chris")
cat.speak()
cat.feed(20)
cat.feed(2)

print("Data container class")

class Foob():
    pass

foob = Foob()
foob.name = "Frank"
foob.age = 27

fooa = Foob()
fooa.name = "Billy"
fooa.age = 46

print(foob.name)
print(fooa.name)

print(foob.age)
print(fooa.age)

