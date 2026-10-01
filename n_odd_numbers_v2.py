print("How many odd numbers you want to print? ", end="")
count = int(input())
print("The first ", count, " odd numbers are ", sep="", end="")
counter = 1
odd_number = 2 * counter - 1
while (counter < count):
    print(odd_number, end=", ")
    counter = counter + 1
    odd_number = 2 * counter - 1
print(odd_number, end=".\n")
