def exceptions():
    try:
        x = 1/0
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError: {e}")
        
    try:
       y = int("xyz")
    except ValueError as e :
         print(f"ValueError : {e}" )
         
    try:
        data = [12,45,33,45]
        z = data[5]
    except IndexError as e:
        print(f"index error: {e}")
        
    try:
        d = {"a":1}
        v = d["b"]
    except KeyError as e:
        print(f"key error : {e}")
    
    try:
        s = "abc" + 5
    except TypeError as e :
        print(f"type error : {e}")
        
    try:
        with open("data.txt") as f:
            f.read()
    except FileNotFoundError as e:
        print(f"file not found error : {e}")
        
    try:
        n = 5
        n.append(6)
    except AttributeError as e:
        print(f"attribute error: {e}")
        
    try:
        print(result)
    except NameError as e :
        print(f"name error : {e}")
        
    try:
        5 == 6
    except:
        print("unknown error.")
        
        
exceptions()