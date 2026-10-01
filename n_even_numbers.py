print("How many even numbers you want to print? ", end="")
count = int(input())
print("The first ", count, " even numbers are ", sep="", end="")
counter = 0
while ((counter / 2) < count - 1):
    print(counter, end=", ")
    counter = counter + 2
print(counter, end=".\n")
