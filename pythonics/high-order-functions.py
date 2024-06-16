def create_adder(x): #first-class-function
    def adder(y):
        return x + y
    return adder #notice that create_adder returns adder.

add_10 = create_adder(10)

# There are built-in higher order functions
list(map(add_10, [1, 2, 3]))          # => [11, 12, 13]

print(list(map(max, [1, 2, 3], [4, 2, 1], [6, 9, 1])))  # => [6, 9, 3]

list(filter(lambda x: x > 5, [3, 4, 5, 6, 7]))  # => [6, 7]

a = lambda x: x>2
print(list(filter(a,[3,4,5,6])))

long_strings = filter(lambda s: len(s) > 5, ["a", "blaster", "c", "demons", "e"])
print(list(long_strings))
