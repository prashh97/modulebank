#4a

# add() adds a new element to the set 
set_a = {1, 2, 3}
set_a.add(4)  # {1, 2, 3, 4}
#intersection() returns a new set with elements that are common to between sets 
set_a = {1, 2, 3}
set_b = {2, 3, 4}
set_a.intersection(set_b)  # {2, 3}
#difference() returns a new set with elements in set_a but not in set_b
set_a = {1, 2, 3}
set_b = {2, 3, 4}
print(set_a.difference(set_b))  # {1}
#isdisjoin() checks if sets have no common elements, returns true if they are different
set_a = {1, 2, 3}
set_b = {4, 5, 6}
print(set_a.isdisjoint(set_b))  # True (No common elements)

# when we tried to add an element that already exists in a set
# nothin happens as sets do not allow duplicates

# when sets have no common elements
# intersection() returns an empty set
# difference() returns the original set

# #when sets are completely identical
# intersection() returns the original set
# difference() returns an empty set


#4b i 
set1 = {"abcdefgh", "mycountryindia", "lmnopqrst", "abc"}
set2 = {"ijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz", "defghijklmnopqrstuvwxyz"}

count = 0  # Start with zero valid pairs

for word1 in set1:  # Pick each word from set1
    for word2 in set2:  # Pick each word from set2
        combined = word1 + word2  # Combine both words
        unique_letters = set(combined)  # Get unique letters
        if unique_letters == set("abcdefghijklmnopqrstuvwxyz"):  # Check if all 26 letters are present
            count += 1  # Increase count if the pair is valid
print("Total complete pairs:", count)   

#4b ii
a = [1, 2, 3, 4] 
b = [5, 6, 3, 8] 
common = set(a).intersection(set(b))
print("Common elements:", common)

#4b iii
a = {1, 2, 3, 4, 5, 6}
b = {3, 4, 5, 6, 7, 8} 
diff_1 = a.difference(b)
diff_2 = b.difference(a)
print("missing numbers in 2nd set compared to 1st :", diff_1)
print("missing numbers in 1sr set compared to 2nd", diff_2)


#4c
# intersection() 
# faster becaue pythons built in set operation uses hashing
# it is more effecient for large databases as it performs direct set operations internally
    
# manual iteration
# slower because it checks each element one by one , time complexity 
# not effecient for large databases as it requires multiple comparisons
    
# intersection is  recommended for large datasets because it is
# optimized, faster and reduces unnecessary comparisons







