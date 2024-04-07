def access_elements(tuple_data):
    first_element = tuple_data[0]
    last_element = tuple_data[-1]
    return first_element, last_element


# Input a tuple from the user
input_tuple = eval(input("Enter a tuple, for example (1, 2, 3): "))

# Access the first and last elements of the tuple
first, last = access_elements(input_tuple)

# Print the result
print("First element:", first)
print("Last element:", last)
