import os
import linecache
import random
import sys
import numpy as np 

# Creates file name in the current working directory
def create_file(name):
    if(not os.path.exists(name)):
        open(name, "w").close()
    else:
        print "The file " + name + " already exists."


# Creates folder name in the current working directory
def create_folder(name):
    if(not os.path.exists(name)):
        os.makedirs(name)
    else:
        print "The folder " + name + " already exists."


# Puts the appropriate values in all the files in all the folders of Base_files
# i.e. it creates PpAa.csv for every p and a depending on the raw files
# 1.csv, .., 15.csv
def makePpAa():
    for p in range(1,16):
        for a in range(1,8): 

            pathwrite = os.getcwd() + "/Base_files/P" + str(p) +"/P" + str(p) + "A" + str(a) + ".csv"
            pathread = os.getcwd() + "/Raw_files/" + str(p) + ".csv"

            fread = open(pathread, 'a')
            fread.write('\n')
            fread.close()

            fwrite = open(pathwrite, 'w')
            fread = open(pathread, 'r')


            for line in fread:
                
                if line[len(line) -2 : len(line) -1] == str(a):
                    fwrite.write(line) 

            fread.close()
            fwrite.close()





# Puts the appropriate values in General Info.txt
def add_to_general_info():

# These lists will be used later on
    listp = []
    lista = []


    # This adds the information sorted by the person
    f = open(os.getcwd() + "/General_info.txt", "a")
    f.write("THIS IS THE INFORMATION SORTED BY THE PERSON. \n")
    f.close()
        
    for p in range(1, 16):

        f = open(os.getcwd() + "/General_info.txt", "a")
        f.write("Person " + str(p) + '\n')
        f.close()
        
        for a in range(1,8):
            
            pwrite = os.getcwd() + "/General_info.txt"
            pread = os.getcwd() + "/Base_files/P" + str(p) + "/P" + str(p) + "A" + str(a) + ".csv"
            
            fwrite = open(pwrite, "a")

            numb_lines = sum(1 for line in open(pread))
            info = "The file P" + str(p) + "A" + str(a) + ".csv has " + str(numb_lines) + " lines. \n"
            fwrite.write(info)
            
            # This next line will add the values to listp
            listp.append(numb_lines)

            fwrite.close()
            
        fwrite = open(pwrite, "a")
        fwrite.write("\n")
        fwrite.close()
        
    # This adds the information sorted by the activity
    f = open(os.getcwd() + "/General_info.txt", "a")
    f.write("THIS IS THE INFORMATION SORTED BY THE ACTIVITY. \n")
    f.close()
    
    for a in range(1, 8):

        f = open(os.getcwd() + "/General_info.txt", "a")
        f.write("Activity " + str(a) + '\n')
        f.close()
        
        for p in range(1,16):
            
            pwrite = os.getcwd() + "/General_info.txt"
            pread = os.getcwd() + "/Base_files/P" + str(p) + "/P" + str(p) + "A" + str(a) + ".csv"
            
            fwrite = open(pwrite, "a")

            numb_lines = sum(1 for line in open(pread))
            info = "The file P" + str(p) + "A" + str(a) + ".csv has " + str(numb_lines) + " lines. \n"
            fwrite.write(info)

            # This next line will add the values to lista
            lista.append(numb_lines)

            fwrite.close()
        fwrite = open(pwrite, "a")
        fwrite.write("\n")
        fwrite.close()

    # Statistics sorted by the person.
    f = open(os.getcwd() + "/General_info.txt", "a")
    f.write("BASIC STATISTICS ON ALL THE ACTIVITIES SORTED BY THE PERSON. \n")
    
    for p in range(1,16):
        x = "Basic Statistics on all of the activities of P" + str(p) + "\n"
        f.write(x)

        listx = listp[(p-1)*7: p*7]
        x1 = "min: " + str(np.min(listx)) + "\n"
        x2 = "max: " + str(np.max(listx)) + "\n"
        x3 = "median: " + str(np.median(listx)) + "\n"
        x4 = "mean: " + str(np.mean(listx)) + "\n"
        x5 = "range: " + str(np.max(listx) - np.min(listx)) + "\n"
        f.write(x1 + x2 + x3 + x4 + x5)

        f.write("\n")
        
    f.close()


 

    # Statistics sorted by the activity. 
    f = open(os.getcwd() + "/General_info.txt", "a")
    f.write("BASIC STATISTICS ON ALL THE PEOPLE SORTED BY THE ACTIVITY. \n")
    
    for a in range(1,8):
        x = "Basic Statistics on all of the persons for activity A" + str(a) + "\n"
        f.write(x)

        listx = lista[(a-1)*15: a*15]


        x1 = "min: " + str(np.min(listx)) + "\n"
        x2 = "max: " + str(np.max(listx)) + "\n"
        x3 = "median: " + str(np.median(listx)) + "\n"
        x4 = "mean: " + str(np.mean(listx)) + "\n"
        x5 = "range: " + str(np.max(listx) - np.min(listx)) + "\n"
        f.write(x1 + x2 + x3 + x4 + x5)

        f.write("\n")
        
    f.close()



