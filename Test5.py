def removeNumNine(list):
    myNewList = []
    for num in list:
        if num != 9:
            myNewList.append(num)
    return myNewList

myArray =  [1,2,3,9,2,9,9,4]
result = removeNumNine(myArray)
print(result)