import random
ZooList = ["Alligators", "Hawks", "Crocodiles", "Giraffes","Bears" ,"Owl", "Snakes" , "Ocelot", "Lion",
 "Cougars", "Penguins", "Chimpanzees", "Gorilla","Peacock","Elephants"]
#Customer has traits to help determine how much money they will spend at the zoo and how much
#money animals will make
class customer:
    def __init__(self, id):
        self.lst = None
        self.age=random.random()*100
        self.id=id
        self.hunger=random.random()*100
        self.thirst=random.random()*100
        self.attention=random.random()*100
        self.favorite=random.choice(ZooList)

    def profit(cus):
        admission=15
        hun= cus.hunger / 10
        thir= cus.thirst / 20
        retVal=admission+hun+thir
        return retVal



def moneyMade(lst):
    total=0
    for customer in lst:
        total=(customer.profit()+total)
    return '%.2f' % total