# print("Hello")

# with open("hello.txt", "a") as file:
#     file.write("\nZinda tilismath")

# with open("hello.txt") as file:
#     # print (hello)
#     for line in file:
#         print (line)

my_dict = {"a": "Hello", "b": "World"}
a = my_dict.keys()
print(type(a))

iterable_a=iter(a)
print(type(iterable_a))
# print(iterable_a.next()) This is a mistake.
print(next(iterable_a))
#print(next(iterable_a))
try:    
    print(next(iterable_a))
except StopIteration:
    print("Well, the iteration stopped")
else:
    print("the exception did not occur")
finally:
    print("Antha jarigindi")
# for i in a:
#     print (i)

