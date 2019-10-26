from os.path import isfile
import numpy
file_path = 'housing.data'

if isfile(file_path):

    # To read a file using python we'll use the method `open`
    my_file = open(file_path)

    for line in my_file.readlines():
        # want to remove any extra chars before reading
        cleaned_line = line.split()
        print(cleaned_line)

    # Reach
    data = numpy.loadtxt(file_path)
    print(data)

    # It's important to close files after they've been used to avoid a `resources leak` on the os
    my_file.close()

else:
    print('Please provide a valid file!')