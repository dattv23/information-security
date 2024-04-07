def create_tuple_from_list(lst):
    return tuple(lst)


# Input a list from the user and handle the string
input_list = input("Enter a list of numbers, separated by commas: ")
numbers = list(map(int, input_list.split(",")))

# Create a tuple and print the result
my_tuple = create_tuple_from_list(numbers)
print("List: ", numbers)
print("Tuple from List:", my_tuple)
