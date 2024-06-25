def findcommonelement(listA, listB):
    common =[]
    for i in listA:
        for j in listB:
            if(i==j):
                common.append(i)
    
    return set(common)

input_str = input("Enter elements of 1st list separated by space: ")
listA = list(map(int, input_str.split()))

input_str = input("Enter elements of 2nd list separated by space: ")
listB = list(map(int, input_str.split()))

print("Common Elements: ", findcommonelement(listA, listB))