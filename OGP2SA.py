import os,sys
import re
import string
import datetime

#    _                                                              _ 
# __| |____________________________________________________________| |__
#(__   ____________________________________________________________   __)
#   | |#This reformats OGP non-contact CMM machine output format  #| |   
#   | |#  to Spatial Analyzer predefined ASCII formatted format.  #| |   
#   | |#                                                          #| |
__author__    =        "Jana Barker & Anthony Barker"             #| |
__copyright__ =         "Copyright (C) 2018 Barkers"              #| |
__version__   =                    "1.0"                          #| |
#   | |#                                                          #| |
#   | |#               Run from the command line:                 #| |   
#   | |#               $ python OGP2SA.py OGP.txt                 #| |   
# __| |#__________________________________________________________#| |__
#(__   ____________________________________________________________   __)
#   !_!                                                            !_!
#    

Input_file = ""
if len(sys.argv) == 1: #If no command line arguments are given, prompt the user for the input file name.
    Input_file = raw_input('OGP File name: ')
else: 
    #else some command line arguments are given, take the first argument as the input file name. 
    Input_file = sys.argv[1] #take in the file name.

Output_file = "SA_" + string.replace(Input_file, ".DAT", ".txt")

InFile = open(Input_file,'r')
OutFile = open(Output_file, 'w')

Line_Nos = []
Line_No = -1
Line_count = Line_No

In_Lines = InFile.readlines()

OutFile.write(string.replace(In_Lines[0], "\\", "/", 5) + "//_AXES_=_CARTESIAN:_X Y Z_(mm)" + "\n" 
    +"//Created: " + str(datetime.datetime.now()) + "\n"
    + "//Translated by: OGP2SA 1.0, Coded by: " + " J&A Barkers, 2018" + "\n")

for line in In_Lines:
    Line_No += 1
    Line_count = Line_No
    match = re.findall('.*[a-zA-Z]', line)
    if match:
        Line_Nos.append(Line_No)

for i in range(1,len(Line_Nos)):
    stop_line = 0
    if i == len(Line_Nos) - 1:
        stop_line = Line_count+1
    else:
        stop_line = Line_Nos[i+1]
    
    Group_name = string.replace(In_Lines[Line_Nos[i]].strip(), " ", "_")
        
    for j in range(1, stop_line - Line_Nos[i]):
        k = Line_Nos[i] + j# + 1
        Point_coordinates = string.replace(In_Lines[k], "+", "", 3)
        
        if len(Point_coordinates) < 2:
            continue
        elif len(Point_coordinates) < 10:
            print("Line %s has something stinky in it!" %k)
        else:
            data = Group_name + " " + str(j) + " " + Point_coordinates
            OutFile.write(data)

#close the files.
OutFile.close()
InFile.close()

print("The OGP file, %s, was succesfully translated to SA input file with name %s!" %(Input_file, Output_file))
