'''Polymorphism
'''

#To briefly demonstrate polymorphism on integers and strings, execute the following code in the Python interpreter:

a = 10
print(a.__add__(20))
b = 'abc'
print(b.__add__('def'))

#Below, there is a code implementing both inheritance and polymorphism:
'''
inheritance: class Radio inherits the turn_on() method from its superclass — that is why we see The device was turned on string twice. Other subclasses override that method and as a result we see different lines being printed;

polymorphism: all class instances allow the calling of the turn_on() method, even when you refer to the objects using the arbitrary variable element.
'''

class Device:
    def turn_on(self):
        print("The device was turned on")

class Radio(Device):
    pass

class PortableRadio(Device):
    def turn_on(self):
        print('PortableRadio type object was turned on')

class TvSet(Device):
    def turn_on(self):
        print('TvSet type object was turned on') 
    
device = Device()
radio = Radio()
portableRadio = PortableRadio()
tvset = TvSet()

for element in (device, radio, portableRadio, tvset):
    element.turn_on()


print()
#another way to achive polymorphism is by dack-typing
#In duck typing, we believe that objects own the methods that are called. If they do not own them, then we should be prepared to handle exceptions.
'''
Below - Both the Wax and Cheese classes own melt() methods, but there is no relation between the two. Thanks to duck typing, we can call the melt() method. Unfortunatelly, the Wood class is not equipped with this method, so an AttributeError exception occurs.'''

class Wax:
    def melt(self):
        print("Wax can be used to form a tool")

class Cheese:
    def melt(self):
        print("Cheese can be eaten")

class Wood:
    def fire(self):
        print("A fire has been started!")

for element in Wax(), Cheese(), Wood():
    try:
        element.melt()
    except AttributeError:
        print("No melt() method")