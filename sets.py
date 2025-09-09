# A Set in an inordered collection data type that stores unique, immutable, elements.
# Sets, themselves, are mutable, allowing for the addition, removal, and modification of their elements. But individual
# elements within a set must be immutable (e.g. numbers, strings, tuples). Mutable types like lists, dictionaries or
# other sets cannot be directly stored as elements within a set.

# Key characteristics of Python sets:
#   - Unordered: elements in a set do not maintain a specific order, and their position cannot be accessed by an index.
#   - Unique elements: sets automatically handle duplicate entries, ensuring that each element within a set is distinct.
#     If an attempt is made to add a duplicate elements, it will be ignored.
#   - Mutable (for the set itself): elements can be added to or removed from a set after its creation.
#   - Immutable elements: the individual elements stored within a set must be immutable data types.

# Creating sets: sets can be created using curly braces {} or the set() constructor
# using curly braces:
my_set = {1, 2, 3, 4}

# using the set() constructor with an iterable
another_set = set([1, 2, 3, 3, 4])
print(another_set)

# Set operations:
# Sets support various mathematical set operations, including:
#   - Union ( | or union()): Returns a new set containing all unique elements from both sets.
#   - Intersection (& or intersection()): Returns a new set containing only the common elements between two sets.
#   - Difference (- or difference()): Returns a new set containing elements present in the first set but not in the
#   second.
#   - Symmetric difference (^ or symmetric_difference()): Returns a new set containing elements that in either set
#   but not in both.
