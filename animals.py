class Human:
    def move(self):
        print("walk")
class Snake:
    def move(self):
        print("slithers")
    
class Fish:
    def move(self):
        return "swims"

for animal in [Human(),Snake(),Fish()]:
    print(animal.move())

    