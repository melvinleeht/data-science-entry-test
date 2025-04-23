def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    if not isinstance(dct, dict):
        raise TypeError("First argument must be a dictionary")

    original = dct.get(key, None)
    if original is not None:
        print(f"Original value: {original}")
    dct[key] = value
    return dct


# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
# - {"age": 25}, "age", 26
print(update_dictionary({}, "name", "Alice"))
print(update_dictionary({"age": 25}, "age", 26))

