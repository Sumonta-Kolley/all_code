def star_pattern(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print("*", end="")
        print()

rows = int(input("Enter number of rows (e.g. 5): "))
star_pattern(rows)