print("Up to which number you want to print even numbers? ", end = "")
count = int(input())
counter = 0
print("The even numbers up to ", count, " are ", sep = "", end = "")
while(counter < count - 1):
    print(counter, end = ", ")
    counter = counter + 2
print(counter, ".", sep ="")
