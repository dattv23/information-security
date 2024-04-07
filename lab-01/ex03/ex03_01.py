def sum_even_numbers(lst):
    total = 0
    for num in lst:
        if num % 2 == 0:
            total += num
    return total


# Get a list from the user and process the string
input_list = input("Enter a list of numbers, separated by commas: ")
numbers = list(map(int, input_list.split(",")))

# Use the function and print the result
sum_even = sum_even_numbers(numbers)
print("The sum of even numbers in the list is:", sum_even)
