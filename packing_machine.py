'''program helping us to pack products into desired materials:

    * the decorator will allow us to pass the packing material as its argument
    * we can handle different material using different argument names
    * the multilevel closure will handle arguments at all cal levels 

'''

#the decorator below will allow us to pass the packing material defined in its argument
def warehouse_decorator(material):
    def wrapper(our_function):
        def internal_wrapper(*args):
            print('<strong>*</strong> Wrapping items from {} with {}'.format(our_function.__name__, material))
            our_function(*args)
            print()
        return internal_wrapper
    return wrapper

@warehouse_decorator('kraft')
def pack_books(*args):
    '''executes as follows:
        - the warehouse_decorator('kraft') function will return the wrapper funcion
        - returned wrapper function will take the function it is supposed to decorate as an argument
        - the wrapper will return the internal_wrapper funcition, which ads new functionality 
          and runs the decorated function.'''
    print("We'll pack books:", args)

@warehouse_decorator('foil')
def pack_toys(*args):
    print("We'll pack toys:", args)

@warehouse_decorator('cardboard')
def pack_fruits(*args):
    print("we'll pack fruits:", args)


pack_books('Allice in Wonderland', 'Winne the Pooh')
pack_toys('doll', 'car')
pack_fruits('plum', 'pear')
