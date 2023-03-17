# 1. Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.
print(type(7))          # Int
print(type(8.67))        # Float
print(type(1 + 1j))      # Complex number
print(type('Ryan'))  # String
print(type(True)) # Boolean
print(type([1, 2, 3]))   # List, ordered
print(type({'name':'Ryan'})) # Dictionary
print(type({9.8, "string?", 2.7}))    # Set, store only unique items
print(type((9.8, True, 2.7)))    # Tuple, immutable, ordered

# 2. Find an Euclidian distance between (2, 3) and (10, 8)
print(((2 - 10) ** 2 + (3 - 8) ** 2) ** 0.5)
