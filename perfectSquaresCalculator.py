
baseNumber = 1
perfectSquare = baseNumber**2

minimum = int(input("Minimum value:"))
maximum = int(input("Maximum value:"))

while perfectSquare <= maximum:

    if perfectSquare >= minimum:
        print(perfectSquare)

    baseNumber += 1
    perfectSquare = baseNumber**2


