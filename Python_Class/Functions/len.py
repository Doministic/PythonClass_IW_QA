newList = [1, 2, 3]

def addToList(list):
    for item in list:
        list.append(item + 3)
    return list

def length(value):
    size = 0
    
    for item in value:
        if value == 0:
            return 0
        size += 1
    return size


old_len = len(newList)
new_len = length(newList)
print(old_len)
print(addToList(newList))



