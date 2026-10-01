print("Up to which number you want to print odd numbers? ", end="")
count = int(input())
counter = 1
print("The odd numbers up to ", count, " are ", sep="", end="")
while (counter < count - 1):
    print(counter, end=", ")
    counter = counter + 2
print(counter, end=".\n")
