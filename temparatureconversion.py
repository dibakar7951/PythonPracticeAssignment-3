def celsiustofahreheit(n):
    return ((9/5)*n)+32
n = float(input("Enter temparature in Celsius: "))
print(f"Temperature in Fahrenheit: {celsiustofahreheit(n)} F")