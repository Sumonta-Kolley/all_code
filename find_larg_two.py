def find_largest(a, b):
    if a > b:
        return a
    else:
        return b

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
print("The largest number is:", find_largest(a, b))