name = 'josh'
print(name)

def nice():
    global name 
    
    new_list = ['joe', 'josgh', 'josh']

    for i in new_list:
        if i == name:
            print("found it")
            name = "boss man"
            

        else:
            print("nothing here")

    print(name)
    return name


nice()

print(name)