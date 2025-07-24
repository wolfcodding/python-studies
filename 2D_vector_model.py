'''Create a custom class to model a 2D vector (x,y) parameters

    * create an initializer
    * implement vector addition so that  v + u = (v(x) + u(x), v(y) + u(y))
    * appropraitrly comment
    * implement methods to print vector  (x,y)
'''

class Vector(object):
    ''' A class for 2D vectors which implements vector addtion '''
    def __init__(self, x, y):
        ''' Initialize the Vector object '''
        self.x = x
        self.y = y

    def __add__(self, other):
        ''' Implement the method for the "+" operator '''
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x,y)

    def __repr__(self):
        ''' Provide a useful representation of the Vector object '''
        return 'Vector(' + str(self.x) + ', ' + str(self.y) + ') '

alpha = Vector(3,4)
beta = Vector(5,6)

gamma = alpha + beta

print(gamma)
