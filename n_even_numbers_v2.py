print("How many even numbers you want to print? ", end="")
count = int(input())
print("The first ", count, " even numbers are ", sep="", end="")
counter = 0
even_number = 2 * counter
while (counter < count-1):
    counter = counter + 1
    print(even_number, end=", ")
    even_number = 2 * counter
print(even_number, end=".\n")
