'''Does something with your precious dots'''

def add(a, b):
    '''Adds a and b'''
    return a+b

def sub(a, b):
    '''Subtracts a and b'''
    return a[0:max(0, len(a)-len(b))]

def div(a, b):
    '''Divides a and b'''
    return to_dots(int(len(a) / len(b)))

def mul(a, b):
    '''Multiplies a and b'''
    return a * len(b)

def to_dots(number):
    '''Returns numbers a and b as dots'''
    return '.'*number

def to_number(dots):
    '''Returns dots a and b as number'''
    return len(dots)