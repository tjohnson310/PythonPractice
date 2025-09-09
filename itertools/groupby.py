# itertools.groupby function is a powerful tool for grouping consecutive elements of an iterable that share the same
# key. It is part of the itertools modules, which provides functions for creating efficient iterators.

# How it works:
# Consecutive grouping: 'groupby()' groups consecutive elements that have the same key. This is a crucial distinction
# from database-style "GROUP BY" operations, which group all elements with the same key regardless of their position.

# Key Function:
# It takes an iterable and an optional key function as arguments.
#   - If a key function is provided, it is applied to each element to determine the grouping key.
#   - If no key function is provided, the elements themselves are used as keys.

# Output: it returns an iterator that yields pairs of (key, group_iterator)
#   - key: the value of the key for the current group.
#   - group_iterator: An iterator yielding the elements belonging to that group. This iterator is consumed when you
#   iterate over it (e.g. by converting it to a list).


