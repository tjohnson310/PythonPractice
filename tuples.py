# Tuples in Python are ordered, immutable, collections of elements. They are similar to lists but differ primarily in
# their immutability, meaning their contents cannot be changed after creation.

# Key characteristics:
#   - Ordered: Elements maintain their insertion order
#   - Immutable: once a tuple is created, its elements cannot be modified, added, or removed.
#   - HeterogeneousL Tuples can contain elements of different data types (e.g. integers, strings, floats)
# Syntax; Tuples are typically defined by enclosing elements in parentheses (), with elements separated by commas.

# Empty tuple:
empty_tuple = ()

# Tuple with elements
my_tuple = ("apple", 1, True)

# Tuple without parentheses (comma-separated values)
another_tuple = "hello", 42, 3.14

# Single-element typle (requires a trailing comma)
single_element_tuple = ("item", )


# Accessing elements: elements in a tuple can be accessed using zer-based indexing or slicing, similar to lists:
print(my_tuple[0])
print(my_tuple[1:3])

# While tuples are immutable, you can perform operations that return new tuples:
#   - Concatenation: combine two or more tuples using the "+" operator.
#   - Repetition: Repeat a tuple using the * operator
#   - Membership testing: Check if an element sexists ina tuple using the 'in' operator.
#   - Iteration: loop through elements in a tuple using a "for" loop.

# Use cases:
#   - Returning multiple values from fns: Functions can return tuples to efficiently return multiple pieces of data.
#   - Dictionary keys: Tuples containing only immutable elements can be used as keys in dictionaries.
#   - Representing fixed data: IDeal for data that should not be altered, such as coordinates, configuration settings,
#   or days of the week
#   - Data integrity: Their immutability ensures data consistency, preventing accidental modification.
