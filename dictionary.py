student = {
    "name": "yello",
    "age": 21,
    "grade" : "A",
    "courses" : ["math" , "physics"]
    ,"is active" : True
}

print("original dictionary" , student)

print("name" , student["name"])

student["email"] = "yellomarshmello@gmail.com"
print("after adding email:" , student)

student["grade"]  = "A+"
print("after updating date:" , student)

remove_age = student.pop("age")
print("remove age:" , remove_age)
print("after removing age:" , student)

print("phone:",student.get("phone" , "not found"))
print("email:",student.get("email" , "not found"))

print("keys:" , list(student.keys()))

print("values:" , list(student.values()))

print("items" , list(student.items()))

