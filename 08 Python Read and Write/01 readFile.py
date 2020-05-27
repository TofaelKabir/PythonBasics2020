file = open("readFile.txt", "r+")  # mode --> r = read, w = write, r+ = read/write, a = append
print("\n----- Is the file readable/writeable? ----- ")
print("Readable? ", file.readable())  # if mode is "w" returns false and "r" returns true, r+ returns true
print("Writable: ", file.writable())  # if mode is "w" returns ture and "r" returns false, r+ returns true

print("\n----- read the file by using read() -----")
text = file.read(10)  # Read character until 10
print(text)
print(len(text), "Characters is read")  # find the length of the readable part (How many char?)

print("\n")
text = file.read(140)  # What happen if there is not 130 characters in the file?
# And from where it start reading and why? Ans: It already read 10
print(text)
print(len(text), "Characters is read")  # There are 124 characters in the file, see the output for it

