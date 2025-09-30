# Q1
 tuple = (10, 20, 30, 40)
 print("tuple = ",tuple)

# Q2
 tuple = ("kamini", 10, False, [2,3], 3.14)
 print("tuple with different data types = ", tuple)

# Q3
 tuple = (10, 20, 30, 40)
 tuple_len = len(tuple)
 print("length of tuple = ",tuple_len)

# Q4
 tuple = (10, 20, 30, 40, 50)
 print("Elements from index 1 to 3 = ", tuple[1:4])
 print("Elements from the beginning to index 2 = ", tuple[ :3])
 print("Elements from index 3 to the end = ", tuple[3: ])

# Q5
# 1
 tuple = ("audi", "swift", "defender")
 print("first element of tuple = ",tuple[0])
 print("second element of tuple = ",tuple[1])
# 2
 tuple = ("audi", "swift", "defender")
 indexing_tuple = int(input("enter a index to show an element of tuple = "))
 print("Show Element of tuple = ",tuple[indexing_tuple])

# Q6
# Q7
# Q8
# Q9
# Q10
 n = 8
 tuple = ('PYTHON , ')
 repeated_tuple = tuple * n
 print("Tuple repeated", n, "times: ", repeated_tuple)

# Q11
 tuple = (10, 20, 30)
 tuple_list = list(tuple)
 print("Original Tuple = ", tuple)
 print("Tuple to list = ", tuple_list)

# Q12
# 1
 tuple = (10, 20, 30, 40, 50)
 tuple_string = str(tuple)
 print("Original Tuple = ", tuple)
 print("Tuple to string = ", tuple_string) 
# 2
 tuple = ("kamini", "kavita", "komal")
 tuple_string = str(tuple)
 print("Original Tuple = ", tuple)
 print("Tuple to string = ", tuple_string)

# Q13
 tuple = (6, 80, 10, 4, 9)
 max_value = max(tuple)
 min_value = min(tuple)
 print("Maximum value in the tuple: ,max_value)
 print("Minimum value in the tuple: ,min_value)

# Q14
 tuple = (5, 1, 9, 3, 7)
 sum_value = sum(tuple)
 print(f"Maximum value in the tuple: ",sum_value)
# Q15
 tuple = (10, 20, 5, 40, 15)
 sorted_tuple = sorted(tuple)
 print("Sorted tuple: ", sorted_tuple)

# Q16
 tuple = ("rose", "lily", "jasmine", "tulip")
 sorted_tuple = sorted(tuple)
 print("Sorted tuple: ", sorted_tuple)

# Q17
 tuple = (10, 20, 30, 40, 50)
 rev_tuple = tuple[::-1]
 print("Reversed tuple: ", rev_tuple)

# Q18
tuple1 = (input("enter a tuple1 : "))
 tuple2 = (input("enter a tuple2 : "))
 if tuple1 == tuple2:
     print("tuple1 and tuple2 are equal.")
 else:
     print("tuple1 and tuple2 are not equal.")
 tuple1 ('red', 'green', 'blue', 'yellow'), tuple2 (1, 2, 3, 4)

# Q19
 original_tuple = (1, 2, 2, 3, 4, 4, 5)
 remove_duplicate = set(original_tuple)
 new_tuple = tuple(remove_duplicate)
 print("Tuple with unique elements: ",new_tuple)


# Q20
 tuple = ("apple", "banana", "kiwi", "grapefruit", "orange")
 max_length = 0
 for word in tuple:
     current_length = len(word)
     if current_length > max_length:
         max_length = current_length
 print("The length of the longest word is: ",max_length)

# Q21
 nested_tuple = ("rose", "sunflower", ("lily", "jasmine"), "tulip")
 print("First element of the inner tuple: ",nested_tuple[2][0])
 print("Second element of the inner tuple: ",nested_tuple[2][1])
 print("First element of nested_tuple: ",nested_tuple[0])
 print("Third element of nested_tuple: ",nested_tuple[2])

# Q22
 nested_tuple = ((1, 2), (3, 4, 5), (6,))
 flattened_tuple = ()
 for sub_tuple in nested_tuple:
     flattened_tuple += sub_tuple
 print(flattened_tuple)

# Q23
 tuple1 = (10, 20, 30)
 tuple2 = ('x', 'y', 'z')
 print("Original tuples:")
 print("Tuple 1: ",tuple1)
 print("Tuple 2: ",tuple2)
 temp_tuple = tuple1
 tuple1 = tuple2
 tuple2 = temp_tuple
 print("Tuples after swapping:")
 print("Tuple 1: ",tuple1)
 print("Tuple 2: ",tuple2)

# Q24
 tuple1 = (1, 2, 3, 4, 5)
 tuple2 = (4, 5, 6, 7, 8)
 common_elements = set(tuple1) & set(tuple2)
 print("common between two tuples: ",common_elements)

# Q25
 tuple1 = (1, 2, 3, 4, 5)
 tuple2 = (4, 5, 6, 7, 8)
 diff_elements = set(tuple1) - set(tuple2)
 print("diffrence between two tuples: ",diff_elements)

# Q26
 tuple = (("name", "kamini"), ("city", "delhi"), ("age", "30"))
 dict_from_tuple = dict(tuple)
 print("tuple of tuples into dictionary: ",dict_from_tuple)

# Q27
 tuple = (("101", "kamini"), ("102", "anshika"), ("103", "kavita"))
 unzipped = zip(*tuple)
 id, name = unzipped
 print("IDs: ", list(id))
 print("Names: ", list(name))

# Q28
 tuple = (1, 2, 2, 2, 3, 3, 4, 5)
 counts = {}
 for item in tuple:
     counts[item] = counts.get(item, 0) + 1
 repeated_items = []
 for item, count in counts.items():
     if count > 1:
         repeated_items.append(item)
 print("Original tuple:", tuple)
 print("Repeated items:", repeated_items)

# Q29
 tuple = (10, 10, 10, 20, 20, 30, 40, 40, 50)
 if len(set(tuple)) == 1 :
     print(tuple,"\nAll elements in the tuple are same.")
 else:
     print(tuple,"\nAll elements in the tuple are not same.")

# Q30
 tuple1 = (1, 2, 3)
 tuple2 = (4, 5, 6)
 result_list = [] 
 for i in range(len(tuple1)):
     result_list.append(tuple1[i] + tuple2[i])
 result_tuple = tuple(result_list)
 print("tuple 1:", tuple1)
 print("tuple 2:", tuple2)
 print("element wise sum of two tuples :", result_tuple)
