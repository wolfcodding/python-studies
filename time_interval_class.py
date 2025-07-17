'''This script implements some custom behaviour to the Python special methods

* class representing a time interval is created
* the class will implement its own method for addition, subtraction on time interval class objects;
* the class will implement its own method for multiplication of time interval class objects by an integer-type value;
* the __init__ method will be based on keywords to allow accurate and convenient object initialization, but limit it to hours, minutes, and seconds parameters;
* the __str__ method will return an HH:MM:SS string, where HH represents hours, MM represents minutes and SS represents the seconds attributes of the time interval object;
* the argument type will be checked and and in case of a mismatch, will raise a TypeError exception.
'''

class MyTimeDelta:
    def __init__(self, hours, minutes, seconds):
        try:
            self.hours = hours
            self.minutes = minutes
            self.seconds = seconds
        except:
            print("Only intiger type arguments are accepted for object initialization")
    
    def __str__(self):
        return "{}:{}:{}".format(self.hours, self.minutes, self.seconds)

    def __add__(self,other):
        return self.hours + other.hours
    
    def __sub__(self,other):
        return other.hours + self.hours
    
    def __mul__(self,other):
        return other.hours * int(other)
    
