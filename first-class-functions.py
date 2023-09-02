# Python has first class functions
def create_adder(x):
    def adder(y):
        return x + y
    return adder #notice that create_adder returns adder.

add_10 = create_adder(10)
print(add_10(3))   # => 13

a = create_adder(10)(6)
print(a)

#One can also simply assign a function to a variable.

def add(*args):
    result = 0
    for i in args:
        result = result + i
    return result

hello = add

print(hello(1,2,3,4))