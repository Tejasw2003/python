print("How many multiples of 7 you want to print? ", end="")
count = int(input())
print("The first ", count, " multiples of 7 are ", sep="", end="")
counter = 1
multiple = counter * 7
while (counter < count):
    counter = counter + 1
    print(multiple, end=", ")
    multiple = counter * 7
print(multiple, end=".\n")
