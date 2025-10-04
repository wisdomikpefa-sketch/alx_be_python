size = int(input("f the user inputs 4, the output should be: "))
row = 0

while row < size:
    for col in range(size):
        print("*", end="")
    print()
    row += 1
