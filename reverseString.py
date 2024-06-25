def reverseString(input):
    output = ""

    for char in input:
        output = char+output
    return output

input = input('Enter a string: ')
print(f'Reversed string: {reverseString(input)}')           