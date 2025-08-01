'''Combiner functions

    - combiner function used for forwarding arbitrary number of arguments function to 
      another function of the same functionality
    - second_combiner function shows how the functionality will change when we pass only 
      handlers of the arbitrary positional and keyword arguments

'''

def combiner(a, b, *args, **kwargs):
    super_combiner(*args, **kwargs)

def super_combiner(*my_args, **my_kwargs):
    print('my_args:', my_args)
    print('my_kwargs', my_kwargs)

combiner(10, '20', 40, 60, 30, argument1=50, argument2='66')


def second_combiner(a, b, *args, **kwargs):
    super_combiner2(args, kwargs)

def super_combiner2(*my_args, **my_kwargs):
    print('my_args:', my_args)
    print('my_kwargs', my_kwargs)

second_combiner(10, '20', 40, 60, 30, argument1=50, argument2='66')