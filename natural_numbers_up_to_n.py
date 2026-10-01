print("Up to which number you want to print natural numbers? ", end="")
count = int(input())
counter = 1
print("The first ", count, " natural numbers are ", sep="", end="")
while (counter < count):
    print(counter, end=", ")
    counter = counter + 1
print(counter, ".", sep="")
