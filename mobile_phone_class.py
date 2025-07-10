'''A class representing a mobile phone;

    * class implements the following methods:
        - __init__ expects a number to be passed as an argument; this method stores the number in an instance variable self.number
        - turn_on() returns the message 'mobile phone {number} is turned on';
        - turn_off() returns the message 'mobile phone is turned off';
        - call(number) returns the message 'calling {number}';
   * the code creats two objects representing two different mobile phones; assigning any random phone numbers to them;
   * implements a sequence of method calls on the objects to turn them on, calls any number. Prints the methods' outcomes;
   * turns off both mobiles.
'''

class MobilePhone:
    def __init__(self, number):
        self.number = number

    def turn_on(self):
        print(f'mobile phone {self.number} is turned on')
    
    def turn_off(self):
        print('mobile phone is turned off')
    
    def call(self, number):
        print(f'calling {number}')

Mobile1 = MobilePhone('0978634512')
Mobile2 = MobilePhone('0888634111')

Mobile1.turn_on()
Mobile2.turn_on()

Mobile1.call('555-34343')

Mobile1.turn_off()
Mobile2.turn_off()