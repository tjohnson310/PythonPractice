# Syntax: lambda arguments: expression

# Example:
double_fn = lambda x: x * 2

print(double_fn(5))

# Using a lambda with map() to double all numbers in a list
numbers = [1, 2, 3, 4]
doubled_numbers = list(map(lambda x: x * 2, numbers))
print(doubled_numbers)

# Using lambda with filter() to get even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# Using lambda as a key for sorting
data = [('apple', 3), ('banana', 1), ('cherry', 2)]
sorted_data = sorted(data, key=lambda item: item[1])
print(sorted_data)
