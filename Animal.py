import random
# 15 animals 5 sections
#Reptiles: Alligator, Crocodiles, Snakes, 
#Birds: Hawks, Owl, PEacock, penguin
#Big Cats: Cougars, Ocelot, Lion, 
#Large Animals: Elephant, Giraffes, Bears
#Monkeys: Chimpanzees, Gorilla


class Animal:
  def __init__(self, type,nutrition,size):
    self.Id = random.random()*100
    self.type =type
    self.nutrition = nutrition 
    self.size = size 

  def CostOfLiving(self):
    return ((self.nutrition)*(self.size))

  def DisplayAnimal(self):
    return str(str(int(self.Id))) + " " + str(self.type) + " " + str(self.nutrition) + " " + str(self.size)