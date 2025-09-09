def outer_function(x):

    # inner_function is a closure. When outer_function is called, it returns inner_function, but inner function
    # "remembers" the value of x (which is 10) from its creation in outer_function.
    def inner_function(y):
        return x + y
    return inner_function


# Create a closure where 'x' is set to 10
add_ten = outer_function(10)

print(f"Closure contents: {[cell.cell_contents for cell in add_ten.__closure__]}")
# Call the closure
result = add_ten(5)
print(result)  # Output: 15 (10 + 5)
