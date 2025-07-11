'''Application that monitors the process of apple packaging before apples are sent to the shop.

    * total order is set to 1000 and not more;
    * total weight cannot exceed 300 units;
    * Assume that each apple's weight is random, and can vary between 0.2 
      and 0.5 of an imaginary weight unit;

    Code creates objects representing apples as long as both limitations are met.
    When any limitation is exceeded, than the packaging process is stopped, and 
    application prints the number of apple class objects created, and the total weight.

    Keep track of two parametets:
    - the number of apples processed
    - the total weight of the apples processed
'''
from random import uniform

class Apple:
    total_apples = 0
    total_weight = 0

    def __init__(self):
        self.apple_weight = uniform(0.2, 0.5)
        Apple.total_weight += self.apple_weight
        Apple.total_apples += 1
      

while Apple.total_apples < 1000:
    if  Apple.total_weight > 300:
        print("The order has reached weight limitation of 300 units")
        break
    else:
        apple = Apple()
    
print("The total weight for your order is {:.2f}".format(apple.total_weight - apple.apple_weight))