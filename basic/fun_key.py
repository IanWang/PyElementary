def func(a, b=5, c=10):
    print 'a is', a, 'and b is', b, 'and c is', c
func(3, 7)
func(25, c=24)
func(c=50, a=100)

# Only those parameters which are at the end of the parameter list can be given default argument values i.e. you cannot have a parameter with a default argument value before a parameter without a default argument value in the order of parameters declared in the function parameter list.

# def func(a, b=5) is valid, but def func(a=5, b) is not valid
