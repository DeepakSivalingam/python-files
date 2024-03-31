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
    #print(file.readline())     # this readline() function reads the data by single line 
    #print(file.readline(2))     # this readline(2) function reads the first two letter of the next line
    print(file.readlines())     # it converts the content of the file into list 
except FileNotFoundError:
    print("file not found error")
else:
    file.close()
    
    
    #looping the contents of the file 
    
    file=open("test file.txt","r") 
    for x in file:
        print(x)
        
    #write to an exixting file
    
file=open("test file.txt",'w')
file.write("this is the content for writing to an existing file ")   #here we overwrite the values
file=open("test file.txt","r")
print(file.read())

#appending to the file 

file=open("test file.txt",'a')
file.write("\nthis is the append operation ")   #here we overwrite the values
file=open("test file.txt","r")
print(file.read())

#deleting the file 

#to deleting the file to import the os

import os
if os.path.exists("test.txt"):
    os.remove("test.txt")
else:
    print("file not found !")

#for deleting the folder

import os
if os.path.exists("sample"):
    os.rmdir("sample")
else:
    print("folder not found !")