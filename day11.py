# Creating a set
my_set = {1, 2, 3, 4, 5, 5}  # Duplicate 5 will be removed
print("Original set:", my_set)

# Adding elements
my_set.add(6)
print("After add:", my_set)

# Update set with multiple values
my_set.update([7, 8])
print("After update:", my_set)

# Removing elements
my_set.remove(3)  # Raises error if element not found
print("After remove(3):", my_set)

# Discarding elements (no error if element not found)
my_set.discard(10)  # No error if 10 is not present
print("After discard(10):", my_set)

# Popping an element (removes a random item)
popped_item = my_set.pop()
print("Popped item:", popped_item)
print("After pop:", my_set)

# Clearing all elements
copy_set = my_set.copy()  # Making a copy before clearing
my_set.clear()
print("After clear:", my_set)

# Set Operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Difference (set1 - set2):", set1.difference(set2))
print("Symmetric Difference:", set1.symmetric_difference(set2))

# Checking subset and superset
print("Is subset:", {1, 2}.issubset(set1))
print("Is superset:", set1.issuperset({1, 2}))

# Checking disjoint
print("Is disjoint:", set1.isdisjoint({7, 8}))
