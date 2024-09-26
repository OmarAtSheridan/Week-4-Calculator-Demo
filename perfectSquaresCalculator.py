
baseNumber = 1
perfectSquare = baseNumber**2

minimum = int(input("Minimum value:"))
maximum = int(input("Maximum value:"))

counter = 0

while perfectSquare <= maximum:

    if perfectSquare >= minimum:
        counter += 1
        print(perfectSquare)

    baseNumber += 1
    perfectSquare = baseNumber**2

else:
    print(f"Number of stuff: {counter}")

