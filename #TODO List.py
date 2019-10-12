'''
Goal: Give the python code a location on my computer to look for #TODO.
If found, it copies/writes the line to a TODO.txt file.
Step 1: Write some python so I can give a specific location to look through.
Step 2: Loop through all the files/folders in that location.
Step 3: copy each line with a #TODO to a TODO.txt


'''

import os

rootdir = '/Users/chandlerkilpatrick/.julia/dev/SHERPA'
text_file_location = '/Users/chandlerkilpatrick/.julia/dev/SHERPA/TODO.txt'
TODO_file = open(text_file_location, 'w')

for subdir, dirs, files in os.walk(rootdir):
    
    for file in files:
        
        if str(file).endswith(".jl"):
            
            open_file = open(os.path.join(subdir, file), 'r')
            
            for line in open_file:
                
                if line.__contains__("#TODO"):
                    line = line.strip()
                    TODO_file.write(line + "\n")
            open_file.close()
            
        # print (os.path.join(subdir, file))


# end of all for loops
TODO_file.close()
