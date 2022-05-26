#opening and closing files 

file = open("filename.txt", "r") #can be r, w, a
file.close()

#reading from files

file = open("filename.txt", "r")

#reading methods
print(file.read()) #ammount of chars wanting to read can be passed as parameter
print(file.readline()) #ammount of chars read of line can be passed as param
print(file.readlines()) #print array reading all lines in file including newline chars

#reading specific line
line_number, current_line = 3,1
for line in file:
    if current_line == line_number:
        print(line)
        break
    current_line += 1

file.close()

#writing to files - overwrites the file

file = open("filename.txt", "w")

#writng methods
file.write("text")#writes the string param into the file
file.writelines(["1\n","3\n","5\n"])#writes each index as new line in file

#writing multiple lines to file
file.write("This is the first line.\n")
file.write("This is the second line.")

file.close()

#appending to file - adds to the file
file = open("filename.txt", "a+")

#appending methods
file.write("text")#appends string param to last line of file
file.write("\ntext")#appends string param to end of file (new line)
file.writelines(["\n1","\n3","\n5"])#apends each index as a new line to the end of file
file.tell()#prints current location of pointer in file
file.seek(0)#data will be added to the beginning of the file
file.seek(1)#data will be added at location of pointer
file.seek(2)#data will be added to end of file


file.close()

