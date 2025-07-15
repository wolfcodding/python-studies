'''
'''

class Person:
    def __init__(self,weight, age, salary):
        self.weight = weight
        self.age = age
        self.salary = salary

p1 = Person(30,40,50)
p2 = Person(35,45,55)

#print(p1 + p2)# when we do this Python will not now how to do addition on these 
#two objects as they do not have or inherit special purpose methods for core operators

#lets add these special method to our class

class NewPerson:
    def __init__(self,weight, age, salary):
        self.weight = weight
        self.age = age
        self.salary = salary
    
    def __add__(self, other):
        return self.weight + other.weight
    
np1 = NewPerson(30, 40, 50)
np2 = NewPerson(35, 45, 55)

print(np1 + np2)