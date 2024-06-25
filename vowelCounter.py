def vowelCounter(input):
    vowels = "aeiouAEIOU"
    count = 0
    for char in input:
        if char in vowels:
            count+=1
    return count

input  = input('Enter a string: ')
print(f"Vowel count: {vowelCounter(input)}")
