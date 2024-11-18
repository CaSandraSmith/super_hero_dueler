class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")
    
    def drink(self):
        print(f"{self.name} is drinking")

# Note that the class Dog takes in Animal as a parameter!
class Frog(Animal):
    def jump(self):
        print(f"{self.name} is jumping")
        
        
if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    bat = Animal("Bat")
    bat.eat()
    bat.drink()
    frog = Frog("Stan")
    frog.eat()
    frog.drink()
    frog.jump()
    