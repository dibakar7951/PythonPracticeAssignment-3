def greatestnumber(listofnumbers):
    max =listofnumbers[0]
    for num in listofnumbers:
        if(num>max):
            max = num
    return max
numbers = []

for i in range(5):
    num = int(input(f"Enter a number: "))
    numbers.append(num)

print(f"Greatest number in the list is: {greatestnumber(numbers)}")
