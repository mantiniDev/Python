numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)

###

numbers.append(4)

print(len(numbers))
print(numbers)

###

numbers.insert(0, 222)
print(len(numbers))
print(numbers)

#

my_list = []  # Creating an empty list.

for i in range(5):
    my_list.insert(0, i + 1)

print("\n",my_list)