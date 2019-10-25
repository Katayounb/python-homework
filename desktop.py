# The library used to manipulate files in Python is called os
import os

# os can be used to validate whether a file really exists and if it is really a file
is_file = os.path.isfile('/Users/katy/desktop/test.txt')
print('text.txt is a file?', is_file)

# is this a directory
is_dir = os.path.isdir('/Users/katy/desktop/hi')
print('hi is a folder? ', is_dir)


# This command lists all files that exist inside a directory
my_desktop = os.listdir('/Users/katy/desktop')
print(my_desktop)

for x in my_desktop:
    #print(x)
    if os.path.isfile('/Users/katy/desktop/'+x) is True:
        print(x, "is a File")
    else:
        print(x, 'is a Dir')