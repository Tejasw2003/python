print("Which multiplication table you want to print? ", end="")
table_num = int(input())
print("The multiplication table of ", table_num, " is:", sep="", end="\n")
counter = 1
multiple = table_num * counter
while (counter <= 10):
    # print(table_num, " x ", counter, " = ", multiple, sep = "", end = "\n")
    print("%2d x %2d = %3d" % (table_num, counter, multiple))
    counter = counter + 1
    multiple = table_num * counter
