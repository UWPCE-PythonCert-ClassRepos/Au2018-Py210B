#!/usr/bin/env python3

def function1():
    """a program which prints the full path for all files in the current directory, one per line"""
    import pathlib
    pth = pathlib.Path("./")
    for f in pth.iterdir():
        print("The full path for {} is {}".format(f,f.absolute()))


def function2():
        """Write a program which copies a file from a source, to a destination (without using shutil, or the OS copy command).
        Advanced: make it work for any size file: i.e. don’t read the entire contents of the file into memory at once.
        This should work for any kind of file, so you need to open the files in binary mode: open(filename, 'rb') (or 'wb' for writing). Note that for binary files, you can’t use readline() – lines don’t have any meaning for binary files. Test it with both text and binary files (maybe jpeg or something of your choosing)."""
        with open ("students.txt","r") as f_input, open("students_copy.txt","w") as f_output:
                for line in f_input.readlines():
                        f_output.write(line)
 
# are we going to have example answer for lab?


"""keep track of how many students specified each language."""
with open("students_copy.txt","r") as f:
        from collections import defaultdict
        count = defaultdict(int)
        for line in f.readlines():
                lst = list(line.split(" "))
                #how to remove \n and , ??
                if "c++," in lst:
                        count["C++"] += 1
                elif "python," in lst:
                        count["Python"] += 1
                elif "sql," in lst:
                        count["SQL"] += 1
                elif "java," in lst:
                        count["Java"] += 1
                elif "r," in lst:
                        count["r"] += 1
                elif "c#," in lst:
                        count["C#"] += 1


print(count)


