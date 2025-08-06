# let's create a function – simple_hello() is one of the simplest functions 
# we could think of. 

def simple_hello():
    print("Hello from simple function!")

# let's create another function, simple_decorator(), that 
# accepts an object as a parameter, displays a __name__ 
# attribute value of the parameter, and returns an accepted object

def simple_decorator(function):
    print(('We are about to call "{}"'.format(function.__name__)))
    return function

#now we invoke both methods
decorated = simple_decorator(simple_hello)
decorated()

#We have created a simple decorator – a function which accepts another 
# function as its only argument, prints some details, and returns a 
# function or other callable object.
print()

#now lets decorate the simple function in a proper syntax
@simple_decorator
def simple_goodbye():
    print("Hello from simple_goodby function!")

simple_goodbye()