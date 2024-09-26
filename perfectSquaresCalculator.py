
baseNumber = 1
perfectSquare = 1

minimum = int(input("Minimum value:"))
maximum = int(input("Maximum value:"))

while perfectSquare <= maximum:

    perfectSquare = baseNumber * baseNumber

    if perfectSquare >= minimum and perfectSquare <= maximum:
        print(perfectSquare)

    baseNumber = baseNumber + 1


