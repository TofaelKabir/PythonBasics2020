# "a" ---> append ---> add line after existing line "w" ---> Override
file = open("writeFile01.txt", "w")  # access to existing file/if not available create a new file
file.write("\nMohammad Orfat \nAge-42\nAddress: 69th st, woodside\nPhone:64646464646")  # "\n-->ensure new line
print("\n----- Writing is done in the writeFile01.txt file -----")

print("\n----- Is the file readable/writeable? ----- ")
print("Readable? ", file.readable())  # if mode is "w" returns false and "r" returns true, r+ returns true
print("Writable: ", file.writable())  # if mode is "w" returns ture and "r" returns false, r+ returns true

file = open("writeFile01.html", "w")
file.write("\n<h1>This is Header</h1>\n<p>Students name: Sharif</p>")
print("\n----- Writing is done in the writeFile01.html file -----")

print("\n----- Is the file readable/writeable? ----- ")
print("Readable? ", file.readable())  # if mode is "w" returns false and "r" returns true, r+ returns true
print("Writable: ", file.writable())  # if mode is "w" returns ture and "r" returns false, r+ returns true

file.close()
