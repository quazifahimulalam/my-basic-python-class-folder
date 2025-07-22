set_a = {'apple','guava','potato','loqat'}
set_b = {'guava','loqat','mango','pepper'}

print("set a :" , set_a)
print("set b :" , set_b)

print(set_a.union(set_b))
print(set_a.intersection(set_b))
print(set_b.difference(set_a))
print(set_a.difference(set_b))
print(set_a.symmetric_difference(set_b))