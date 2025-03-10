#5a
d = {"name": "Alice", "age": 25, "city": "New York"}

# get() method
print("Age:", d.get("age"))  # 25

# keys() method
print("Keys:", d.keys())  # ['name', 'age', 'city']

# values() method
print("Values:", d.values())  # ['Alice', 25, 'New York']

# update() method
d.update({"age": 26})
print("Updated Dictionary:", d)

# pop() method
d.pop("city")
print("After pop:", d)  # {'name': 'Alice', 'age': 26}



#5b i 
d = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15}

# Sort by key
sorted_dict_by_key = dict(sorted(d.items()))
print("Sorted Dictionary by Key:", sorted_dict_by_key)

#5b ii
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

result = {}
for key in d1:
    if key in d2:
        result[key] = d1[key] + d2[key]  # Add values for common keys
    else:
        result[key] = d1[key]  # Keep the value from d1 if not in d2

for key in d2:
    if key not in d1:
        result[key] = d2[key]  # Add new key from d2 if not in d1

print("Combined Dictionary:", result)

#5b iii
d = {'c1': 'Red', 'c2': 'Green', 'c3': None}

for key in list(d.keys()):
    if d[key] is None:
        del d[key]

print("Updated Dictionary:", d)

#5b iv
d1 = {'x': 1, 'y': 2}
d2 = {'y': 3, 'z': 4}

merged_dict = d1.copy()  # Copy d1
merged_dict.update(d2)  # Merge d2 into it

print("Merged Dictionary:", merged_dict)


#5c

#case 1 , using get() method
d = {'name': 'Alice', 'age': 25}

age = d.get('age', 'Not Found')  # If 'age' exists, return value, else return 'Not Found'
print("Age:", age)

height = d.get('height', 'Not Found')  # 'height' key does not exist
print("Height:", height)
#no error if key is not found

#case 2, using [] operator
d = {'name': 'Alice', 'age': 25}
print("Age:", d['age'])  # Works fine
print("Height:", d['height'])  # ❌ ERROR: KeyError: 'height'
#throws error if key is not found

#in a nutshell , using get() is better as we can handle cases if the key is not found


