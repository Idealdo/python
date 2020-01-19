print("#################################################################################################################")
print("")
print("For loop:")
for i in range(0, 4):
    print("Number %d" % (i))

print("#################################################################################################################")

print("")

print("#################################################################################################################")
print("### Basic Python built-in Data Structures ###")

print("#################################################################################################################")
print("Python Lists: A list consists of a number of comma-separated values (items) between square brackets.")
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, "a", 9]]
for list in list_of_lists:
    for x in list:
        print(x)

list_of_letters = ["a", "b"]
print(list_of_letters)
print("#################################################################################################################")

print("")

print("#################################################################################################################")
print("Python Tuples: A tuple consists of a number of comma-separated values.")
t = 12345, 54321, list_of_lists, 'hello'
print(t[0])
print(t[2])
t[2].append('gatrico')
print(t[2])
print(t)

# Tuples are immutable
# t[2] = [1, 3] # This is not valid

# Lists are mutable
list_of_lists[0] = [999]
print(list_of_lists)

empty = ()
singleton = 4,
print(empty)
print(singleton)
print("#################################################################################################################")

print("")

print("#################################################################################################################")
print("Python Sets: A set is an unordered collection with no duplicate elements. Curly braces or set() function can be")
print("used to create sets.")
print("The empty set is created with set()")
gatos = {'Gatrico', 'Moreno', 'Amarello', 'Boni'}
print(gatos)
print('Paty' in gatos)

perros = set("Choco")  # it adds C, h, o, c. Not Choco, same for 'Choco'. It adds a list.
perros.add('Bruja')
print(perros)
print("#################################################################################################################")

print("")

print("#################################################################################################################")
print("Python Dictionaries: A pair of curly braces creates an empty dictionary: {}. Placing a comma-separated number of")
print("key:value pairs within curly braces sdds initial key:value pairs to the dictionary.")
d1 = {}
d1[1] = "Morenito"
print(d1)
d1["bb"] = 4
print(d1)
print("#################################################################################################################")
print("")


# Python built-in functions
print("Some Built-in functions")

print("#################################################################################################################")
print("")
print("abs(x) function: returns the absolute value of a number")
print("abs(%d) = %d" % (-4, abs(-4)))
print("abs(%.2f) = %f" % (-9.45, abs(-9.45)))
print("#################################################################################################################")
print("")

print("#################################################################################################################")
print("")
print("all(iterable) function: returns True if all elements of the iterable are True")
print(all([True, True]))
print(all([True, True, True, False]))
print(all((True, (False, (False, ("b", 4))))))
print("#################################################################################################################")
print("")

print("#################################################################################################################")
print("")
print("any(iterable) function: returns True if any element of the iterable is True.")
print(any([False, False, False, True]))
t2 = False, True
print(any(t2))
print(any(()))
print("#################################################################################################################")
print("")


print("#################################################################################################################")
print("")
print("len(s) function: returns the length (number of items) of an object. The argument may be a sequence such as a ")
print("string, bytes, list, tuple, or range; or a collection such as dictionary, set, or frozen set.")
print(len(set()))
print(len(range(2, 9)))
print(len((1, 2)))
print("#################################################################################################################")

print("")

print("#################################################################################################################")
print("dir([object] function: without arguments return the list of names in the current local scope. With an argument")
print("return, attempt to return a list of valid attributes for that object")

print(dir())
print(dir(__file__))
print(dir(__file__.isalpha))

import struct
print(dir(struct))
print("#################################################################################################################")

print("")

print("#################################################################################################################")
print("sum(iterable, l, start =0) function: sums start and the items of an iterable from left to right and return the")
print("total")
print(sum([1,2], -3))

print("#################################################################################################################")

print("")

print("#################################################################################################################")


def my_addition(n):
    return n+n


numbers = [1, 2, 3, 4, 5]
result = list(map(my_addition, numbers))
print(result)
