# collections.defaultdict in Python is a specialized dictionary subclass that provides a default value for a key that
# does not exist when it is accessed. This differs from a standard dict, which would raise a KeyError if an attempt is
# made to access a non-existent key.

# Key Features:
# default_factory:
#   - The core of defaultdict is its default_factory argument during initialization. This argument takes a callable
#   (e.g., int, list, set, or a custom function) that will be called without arguments to provide a default value when
#   a missing key is accessed.

# Automatic Default Value Creation:
# When you try toa ccess a key that is not yet in the defaultdict, the default_factory is automatically invoked, and
# its return value is used as the value for the new key-value pair. This eliminates the need for explicity "if key not
# in dict:" check and initialization.

# Common Use Cases:
#   - Counting occurrences: Using defaultdict(int) is common for counting items, where the default value for a new key
#   is 0.
#   - Grouping elements: Using defaultdict(list) or defaultdict(set) allows for easy grouping of item sbased on a key, \
#   where the default value for a new key is an empty list or set, respectively.
#   - Nested dictionaries: defaultdict(lambda: defaultdict(int)) can be used to easily create mult-level nested
#   dictionaries without manual initialization.

from collections import defaultdict

# Counting occurrences of words
word_counts = defaultdict(int)
text = "apple banana apple cherry banana"
for word in text.split():
    word_counts[word] += 1
print(word_counts)

# Grouping items by their first letter
grouped_words = defaultdict(list)
words = ["apple", "ant", "banana", "bat"]
for word in words:
    grouped_words[word[0]].append(word)
print(grouped_words)

