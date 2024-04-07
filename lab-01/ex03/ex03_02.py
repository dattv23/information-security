def reverse_list(lst):
    return lst[::-1]


# Input a list from the user and handle the string
input_list = input("Enter a list of numbers, separated by commas: ")
numbers = list(map(int, input_list.split(",")))

# Use the function and print the result
reversed_list = reverse_list(numbers)
print("The list after reversing:", reversed_list)
