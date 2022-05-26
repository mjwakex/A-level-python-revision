#try something, except error, do something else
from logging import exception
from msilib.schema import Error


try:
    file = open("filename.txt","r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("File not found")

#try something, exceot error, do something else, finally always execute this
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Error!")
finally:
    print("Enjoy your day!")

#infinate try except until try is run
while True:
    try:
        value = int(input("enter a int value: "))
        break #break the loop if try block is executed
    except ValueError:
        pass #loop again until try is executed


