dictionary = {
    "a" : 1,
    "b" : 1,
    "c" : 2,
    "d" : 4
}

unique_values = {}

for values , key in dictionary.items():
    if dictionary not in unique_values.values():
        unique_values[key] = values

print("original dictionary" , dictionary)

print("after removing duplicates:" , unique_values)