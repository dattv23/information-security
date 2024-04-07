def delete_element(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        return True
    else:
        return False


# Use the function and print the result
my_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
key_to_delete = "b"
result = delete_element(my_dict, key_to_delete)
if result:
    print("The element has been deleted from the Dictionary:", my_dict)
else:
    print("Did not find the element to delete in the Dictionary.")
