size = int(input("Enter the size of the pattern: "))

row = 0

while row < size:
    # Use a for loop for columns
    for col in range(size):
        print("*", end="")  # print asterisk without moving to next line
    print()  # move to the next line after each row
    row += 1