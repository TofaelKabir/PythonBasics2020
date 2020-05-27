# "a" ---> append ---> add line after existing line "w" ---> Override
file = open("writeFile02.txt", "a")  # access to existing file/if not available create a new file
file.write("\nMohammad Tofael \nAge-44\n625W 57th st, NY\nPhone:3476537214\n")  # "\n-->ensure new line
print("\n----- Append is done in the writeFile02.txt file -----")

print("\n----- Is the file readable/writeable? ----- ")
print("Readable? ", file.readable())  # if mode is "w" returns false and "r" returns true, r+ returns true
print("Writable: ", file.writable())  # if mode is "w" returns ture and "r" returns false, r+ returns true

file = open("writeFile02.html", "a")
file.write("\n<h1>This is Header</h1>\n<p>Students name: Sharif</p>")
print("\n----- Append is done in the writeFile02.html file -----")

print("\n----- Is the file readable/writeable? ----- ")
print("Readable? ", file.readable())  # if mode is "w" returns false and "r" returns true, r+ returns true
print("Writable: ", file.writable())  # if mode is "w" returns ture and "r" returns false, r+ returns true

file.close()
