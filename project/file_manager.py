''' 
file: any name with extensions
extensions: .py, .txt, .mp3 etc

file handling: creating, reading, updating, deleting 
(CRUD) operations that we can perform in files

r - read: reads a file & is default mode
w - write: creates or overwrites a file
a - append: write in file without overridding
x - create: Create an empty file

===========
a = open('abc.txt')
print(a.read())
a.close()

f = open('def.txt', 'w')
f.write('Hello this is second file\ncreated with the help of Python file handling.')
f.close()

b = open('def.txt', 'a')
b.write('\n\nAnd now we have appended this text in our file, without overridding')
b.close() 
===========
'''

from pathlib import Path
def existingFiles():
    path = Path('.') #Path.cwd & Path('.'): current working directory
    files = [f for f in path.iterdir() if f.is_file()]
    if not files:
        print("No files found.")
        return
    for i, f in enumerate(files, 1):
        print(f"{i}: {f.name}")

def createFile(file_name):
    if Path(file_name).exists():
        ch = int(input("Do you want to overwrite?(Yes- 1, No - 0): "))
        if ch == 0:
            return
    with open(file_name, 'w') as fc:
        data = input(f"Write in file {file_name}:\n")
        fc.write(data)
    print("File Created Successfully")

def readFile(file_name):
    if Path(file_name).exists():
        with open(file_name, 'r') as fr:
            print(fr.read())
        print("File Read Successfully.")
    else:
        print("File doesn't exist.")
        d = int(input("Do you want to create new file? (Yes-1, No-0): "))
        if d == 0:
            return
        else:
            createFile(file_name)

def updateFile(file_name):
    if Path(file_name).exists():
        print("Update:\n1. Rename the file\n2. Overwrite in file\n3. Append in file")
        ch = int(input("Updating action: "))
        if ch == 1:
            new_name = input("New Name: ")
            if Path(new_name).exists():
                print("File with this name already exists.")
                return
            
            Path(file_name).rename(new_name)
            print("File Renamed Successfully.")

        elif ch == 2:
            with open(file_name, 'w') as fw:
                data = input(f"Write in file {file_name}:\n")
                fw.write(data)
            print("File Overwritten Successfully.")

        elif ch == 3:
            with open(file_name, 'a') as fa:
                data = input(f"Write in file {file_name}:\n")
                fa.write("\n" + data)
            print("File Appended Successfully.")

        else:
            print("Invalid Selection")
            return

    else:
        print("Selected file doesn't exist.")
        d = int(input("Do you want to create new file? (Yes-1, No-0): "))
        if d == 0:
            return
        else:
            createFile(file_name)


def deleteFile(file_name):
    if Path(file_name).exists():
        confirm = input("Are you sure? (y/n): ")
        if confirm.lower() != 'y':
            return
        Path(file_name).unlink() 
        #import os
        #os.remove(Path(file_name))
        print("File Deleted Successfully.")
    else:
        print("File doesn't exist.")

while True:
    print("""
Operations:
1. Create a file
2. Read a file
3. Update a file
4. Delete a file
5. Exit
""")

    try:
        n = int(input("Select Operation: "))
    except Exception as err:
        print(f"{err} occured. Please enter a valid number")
        continue

    if n == 5: 
        break

    existingFiles()
    f_name = input("Name of the file: ")
    
    if n == 1:
        createFile(f_name)

    elif n == 2: 
        readFile(f_name)

    elif n == 3:
        updateFile(f_name)

    elif n == 4:
        deleteFile(f_name)

    else:
        print("Invalid Input")
