'''This script implements some custom behaviour to the Python special methods

* class representing a time interval is created
* the class will implement its own method for addition, subtraction on time interval class objects;
* the class will implement its own method for multiplication of time interval class objects by an integer-type value;
* the __init__ method will be based on keywords to allow accurate and convenient object initialization, but limit it to hours, minutes, and seconds parameters;
* the __str__ method will return an HH:MM:SS string, where HH represents hours, MM represents minutes and SS represents the seconds attributes of the time interval object;
* the argument type will be checked and and in case of a mismatch, will raise a TypeError exception.
'''

class MyTimeDelta:
    def __init__(self, hours = 0, minutes = 0, seconds = 0):
        
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        
        try:
            if not (isinstance(self.hours, int) and isinstance(self.minutes, int) \
                    and isinstance(self.seconds, int)):
                raise TypeError 

        except TypeError:
            print("Only intiger type arguments are accepted for object initialization")
        except:
            print("Something else went wrong: ")
    
    
    def __str__(self):
        return "{}:{}:{}".format(self.hours, self.minutes, self.seconds)

    def __add__(self,other):
        sec_interv_self = self.hours * 3600 + self.minutes * 60 + self.seconds
        sec_interv_other = other.hours * 3600 + other.minutes * 60 + other.seconds

        add_interv = sec_interv_self + sec_interv_other

        interv_hours = add_interv // 3600
        interv_minutes = (add_interv % 3600) // 60 
        interv_seconds = (add_interv % 3600) % 60

        return MyTimeDelta(hours = interv_hours, minutes = interv_minutes, seconds = interv_seconds) 
    
    def __sub__(self,other):
        return other.hours - self.hours
    
    def __mul__(self,other):
        return other.hours * int(other)
    

#Test data
fti = MyTimeDelta(21, 58, 50)
sti = MyTimeDelta(1, 45, 22)

print(fti + sti)
    
