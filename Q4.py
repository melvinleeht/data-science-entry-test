def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    if not isinstance(s, str):
        raise TypeError("Argument must be a string")
    reversed_str = s[::-1]

    return reversed_str


# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"
print(string_reverse("Hello World"))
print(string_reverse("Python"))
