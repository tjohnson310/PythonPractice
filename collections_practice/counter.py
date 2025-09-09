# The collections.Counter tool in Pytohn is a specialized dictionary subclass designed for efficiently counting
# hashable objects. It is part of Python's collections module, which provides various container datatypes beyond the
# built-in ones.

# Key features and usage of collections.Counter:
#   - Counting occurrences: Its primary purpose is to count the frequency of elements within an iterable (such as a
#   list, string, or tuple). When initialized with an iterable, it creates a dictionary-like objext where elements are
#   keys and their counts are values.

from collections import Counter

data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
counts = Counter(data)
# print(counts)

# Dictionary-like behavior
# As a subclass of dict, Counter objects inherit all standard dictionary methods like keys(), values(), items(), and
# get(). Accessing a non-existent key returns a count of 0 by default, which is convenient for tallying.

# most_common() method:
# This method returns a list of the n most common elements and their counts, from most to least common.

text = "this is a test string for counting words"
words = text.split()
letters = [letter for letter in list(text) if letter != " "]
word_counts = Counter(words)
letter_counts = Counter(letters)
# print(word_counts.most_common(5))
# print(letter_counts.most_common(3))


# Arithmetic Operations: Counter objects support arithmetic operations like addition, subtraction, union, and
# intersection, allowing for combination or comparison of counts between different Counter instances.

c1 = Counter({'a': 3, 'b': 1})
c2 = Counter({'a': 1, 'b': 2})
print(c1 + c2)
