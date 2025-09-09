# The itertools.product() function in Python is a built-in tool that calculates the Cartesian product of input
# iterables. This means it generates all possible combinations of elements from the provided iterables, similar to the
# outcome of nested for-loopa.

# Syntax:
# itertools.product(*iterables, repeat=1)

# Parameters:
#   - *iterables: takes one or more iterable objects (e.g. lists, tuples, strings) as arguments.
#   - repeat (Optional): An integer specifying the number of times to repeat the iterable for self-product. The default
#   value is 1.

# Functionality:
# The product() function returns an iterator that yields tuples, where each tuple represents a unique combination of
# elements taken from the input iterables. The combinations are generated in an order that mirrors nested loops,
# processing from left to right.

from itertools import product

# Cartesian product with repeat parameter
list1 = [1, 2]
list2 = [3, 4]
result1 = list(product(list1, list2))
print(f"Product of {list1} amd {list2}: {result1}")

# Cartesian product with repeat parameter
list_single = ['A', 'B']
result2 = list(product(list_single, repeat=2))
print(f"Product of {list_single} repeated twice: {result2}")


# Use cases: itertools.product() is particularly useful for tasks such as:
#   - Generating all possible combinations of a set of values.
#   - Exploring every combination in combinatorial problems (e.g. generating test cases)
#   - Working with non-dimensional data structures
#   - Generating Cartesian products for simulations or parameter tuning in fields like machine learning.
