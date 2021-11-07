import random
#pay name habitat
# pay is 16.5$
#Reptiles: Alligator, Crocodiles, Snakes, 
#Birds: Hawks, Owl, PEacock, penguin
#Big Cats: Cougars, Ocelot, Lion, 
#Large Animals: Elephant, Giraffes, Bears
#Monkeys: Chimpanzees, Gorilla
Habitat = ["Reptiles","Birds","Big Cats","Large Animals","Monkeys"]
class ZooKeeper:
    def __init__(self, pay, id):
        self.pay = pay
        self.id = id
        self.habitat = random.choice(Habitat)
