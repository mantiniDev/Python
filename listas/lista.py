numbers = [10, 5, 7, 2, 1]
print("Original list content:", numbers)  # Printing original list content.

numbers[0] = 111
print("New list content: ", numbers)  # Current list content.

numbers[1] = numbers[4]
print("New list content: ", numbers)  # Current list content.

print("\nList length:", len(numbers))  # Printing the list's length.

del numbers[1]  # Removing the second element from the list.
print("\nNew list's length:", len(numbers))  # Printing new list length.
print("\nNew list content:", numbers)  # Printing current list content.

numbers = [111, 7, 2, 1]
print(numbers[-1])
print(numbers[-4])