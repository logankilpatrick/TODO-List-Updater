'''
Goal: Give the python code a location on my computer to look for #TODO.
If found, it copies/writes the line to a TODO.txt file.
Step 1: Write some python so I can give a specific location to look through.
Step 2: Loop through all the files/folders in that location.
Step 3: copy each line with a #TODO to a TODO.txt


'''

import os
import datetime

# Pathway to folder I want to look through.
rootdir = '/Users/chandlerkilpatrick/.julia/dev/SHERPA'

# Pathway to file that is collecting the TODO list.
text_file_location = '/Users/chandlerkilpatrick/.julia/dev/SHERPA/TODO.txt'

# Opens and writes the TODO.txt file.
TODO_file = open(text_file_location, 'w')

# All the possible variations to look for.
possible_TODO = ["#TODO", "# TODO:", "# TODO", "TODO:"]


for subdir, dirs, files in os.walk(rootdir):
    
    for file in files:
        
        if str(file).endswith(".jl"): # All .jl files are opened
            
            open_file = open(os.path.join(subdir, file), 'r')
            line_counter = 0
            for line in open_file:
                
                for item in possible_TODO:
                    
                    if line.__contains__(item):
                        # If a line contains any of the possible variations.
                        # The line is stripped and pasted in the TODO.txt file.
                        line = line.strip()
                        
                        TODO_file.write("File Name: " + file + "\n")
                        TODO_file.write("Line Number: " + str(line_counter) + "\n")
                        TODO_file.write(line + "\n" + "\n")
                        break
                line_counter += 1
            # Closes open_file       
            open_file.close()
            

# end of all for loops

# Prints the last date modified for convenience. 
TODO_file.write("Last modified: " + str(datetime.datetime.now()))
# Closes the TODO_file
TODO_file.close()
