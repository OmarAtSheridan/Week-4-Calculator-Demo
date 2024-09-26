
baseNumber = 1
perfectSquare = baseNumber**2

minimum = int(input("Minimum value:"))
maximum = int(input("Maximum value:"))

while perfectSquare <= maximum:

    perfectSquare = baseNumber**2

    if perfectSquare >= minimum and perfectSquare <= maximum:
        print(perfectSquare)

    baseNumber += 1


