#file operations
#to open the file in the read mode 

#two modes-read and write

try:
    file=open("test file.txt","r") 
    print(file.read())
except FileNotFoundError:
    print("file not found error")
else:
    file.close()
    
    
try:
    file=open("test file.txt","r") 
    print(file.readline())     # this readline() function reads the data by single line 
except FileNotFoundError:
    print("file not found error")
else:
    file.close()