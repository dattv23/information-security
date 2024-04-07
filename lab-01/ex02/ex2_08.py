# Function to check if a binary number is divisible by 5
def is_divisible_by_5(binary_number):
    # Convert the binary number to decimal
    decimal_number = int(binary_number, 2)
    # Check if the decimal number is divisible by 5
    if decimal_number % 5 == 0:
        return True
    else:
        return False


# Get a string of binary numbers from the user
binary_number_string = input("Enter a string of binary numbers (separated by commas): ")
# Split the string into individual binary numbers and check for divisibility by 5
binary_number_list = binary_number_string.split(",")
divisible_by_5 = [number for number in binary_number_list if is_divisible_by_5(number)]
# Print out the binary numbers that are divisible by 5
if len(divisible_by_5) > 0:
    result = ",".join(divisible_by_5)
    print("The binary numbers divisible by 5 are: ", result)
else:
    print("There are no binary numbers divisible by 5 in the entered string.")
