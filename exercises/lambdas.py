import pytest
import math

# Replace each ellipsis (...) with your code.

def test_lambdas():

    # Exercise 1
    # Use a lambda to find the square root of a number.
    # Assume you'll be given a positive number.
    # Hint: the math module is already imported for you :)
    # ================================

    # ...
    assert square_root(49) == 7


    # Exercise 2
    # Use a lambda to find the sum of three numbers
    # Assume you're given three valid numbers.
    # ================================

    # ...
    assert find_sum(5, 4, 3) == 12
    assert find_sum(49, 31, 20) == 100
    assert find_sum(5.5, 2.5, 3) == 11.0


    # Exercise 3
    # Use a lambda to concatenate a string to itself with a space in between
    # For example: "fun" becomes "fun fun"
    # ================================

    # ...
    assert double_string("python") == "python python"


    # Exercise 4
    # Use a lambda to remove extra spaces between words in a string.
    # For example, "Hello     there" becomes "Hello there"
    # Hint: join() and split() will be useful.
    # ================================

    # ...
    assert clean_up("Python    is     so much    fun!") == "Python is so much fun!"


    # Exercise 5
    # Use a lambda to convert a Fahrenheit temperature to Celsius
    # Hint: round your result to one decimal place using round().
    # ================================

    # ...
    assert convert_f_to_c(32) == 0
    assert convert_f_to_c(61) == 16.1


    # Exercise 6
    # Use a lambda to sort the characters of a given string in increasing order. 
    # The sorted list should be comprised of characters.
    # Hint 1: use a list comprehension to create a list of the individual characters.
    # Hint 2: sort() is useful, as is its "key" parameter.
    # ================================

    some_string = '0912542'
    # ...
    assert data == ['0', '1', '2', '2', '4', '5', '9']
