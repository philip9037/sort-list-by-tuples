# Sample list of tuples
tuples_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# Sort the list in increasing order by the last element in each tuple
sorted_list = sorted(tuples_list, key=lambda x: x[-1])

# Print the sorted list
print(sorted_list)
