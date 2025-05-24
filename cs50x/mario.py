height = int(input("how high you want this thing? "))

for i in range(height):
    for j in range(height - i - 1):
        print(" ", end="")
    for k in range(0, i + 1):
        print("#", end="")
    print("  ", end="")
    for l in range(0, i + 1):
        print("#", end="")
    print("")
