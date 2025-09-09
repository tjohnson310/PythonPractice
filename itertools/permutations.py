# itertools.permutations is designed to generate all possible ordered arrangements (permutations) of elements from a
# given iterable (such as a list, string, or tuple).

# Key features:
#   - Generates ordered arrangements: considers the order of elements, meaning that (1, 2) and (2, 1) are treated as
#   distinct permutations.
#   - Returns an iterator: instead of returning a list directly, it returns an iterator, which is more memory-efficient,
#   especially for large inputs. You can convert this iterator to a list if needed (e.g. list(permutations(iterable))).
#   - Optional 'r' argument: You can specify the length of th epermutations you want to generate using the 'r' argument.
#   If 'r' is not provided or is None, it defaults to the length of the input iterable, generating all full-length
#   permutations.
#   - Elements treated as unique based on position: Even if an iterable contains duplicate values, permutations() treats
#   them as distinct if their positions differ.
#   - Lexicographical order: the permutations are generated in lexicographical (sorted) order.

from itertools import permutations

# Permutations of a list
my_list = [1, 2, 3]
for p in permutations(my_list):
    print(p)

# Permutations of a string
my_string = "ABC"
for p in permutations(my_string, 2):
    print(p)
