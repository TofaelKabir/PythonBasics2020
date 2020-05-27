file = open("readFile.txt", "r+")  # mode --> r = read, w = write, r+ = read/write, a = append
# Need to separate read() method, because both can't work in same page
print("\n----- Read line by using readLines() -----")
line = file.readlines()
print(line)   # Print as a list
print("\n----- Line in Index n -----")
print(line[0])
print(line[1])
print(line[2])
print(line[3])
print(line[-1])
print(line[-2])
print(line[-3])

print("\n----- print by using for loop -----")
for i in line:
    print(i)

file.close()
