add_two_numbers = lambda x,y: x+y
print(add_two_numbers(3,6))

print(list(map(add_two_numbers, (1, 3), (4, 4))))

##note there is no return statement in inline a.k.a anonymous functions. It returns by default.