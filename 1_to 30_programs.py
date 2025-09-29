# Q1
# tuple = (10, 20, 30, 40)
# print("tuple = ",tuple)

# Q2
# tuple = ("kamini", 10, False, [2,3], 3.14)
# print("tuple with different data types = ", tuple)

# Q3
# tuple = (10, 20, 30, 40)
# tuple_len = len(tuple)
# print("length of tuple = ",tuple_len)

my_tuple = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
slice_obj = slice(2, 7, 2) # Defines a slice from index 2 to 7 (exclusive), with a step of 2
sliced_result = my_tuple[slice_obj]
print(f"Sliced tuple: {sliced_result}") # Output: (30, 50, 70)
