import os

import linecache # to make the random samples
import random 
import sys

##############################################################
# Create folders and files 
##############################################################

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

# Create Output folder 
def create_output_folder():
	create_folder("Output")

# Create Output_o folder 
def create_output_o_folder(output_numb):
	create_folder("Output_" + str(output_numb))

# Create Pp_Output folders
def create_Pp_output_folders(): 
	for p in range(1,16): 
		create_folder("P" + str(p) + "_Output")

# Create Pp_sample_folders 
def create_Pp_sample_folders(): 
	for p in range(1,16):
		os.chdir("P" + str(p) + "_Output")
		create_folder("P" + str(p) + "_Samples")
		os.chdir("../")

# Create Pp_Persistence_Diagram folders and it's sub-folders
def create_Pp_persist_diag_folders(): 
	for p in range(1,16):
		os.chdir("P" + str(p) + "_Output")
		create_folder("P" + str(p) + "_Persistence_Diagrams")
		os.chdir("P" + str(p) + "_Persistence_Diagrams")
		for a in range(1,8): 
			create_folder("P" + str(p) + "A" + str(a) + "_Persistence_Diagrams")
		os.chdir("../")
		os.chdir("../")

##############################################################
# Doing more important things 
##############################################################

# Make sure that numb_of_samples isn't bigger than the 
# file size from which we are taking the samples from 
def check_sample_sizes(size_of_samples): 
	for p in range(1,16): 
		for a in range(1,8): 
			os.chdir("P" + str(p))

			base_file = os.getcwd() + "/P" + str(p) + "A" + str(a) + ".csv"
			sample_size = size_of_samples[p - 1][a - 1]
			os.chdir("../")

			with open(base_file) as f: 
				lines_in_file = len(f.readlines())

			if sample_size > lines_in_file: 
				print("P" + str(p) + "A" + str(a))
				print("Sample size " + str(sample_size))
				print("Data size " + str(lines_in_file))
				print("You want a sample size that is bigger than the file size.") 
				sys.exit(1)

# Create the random sample files 
def create_samples(numb_of_samples, size_of_samples, output_numb):
	for p in range(1,16): 
		for a in range(1,8):
			# Change to the right directory 
			os.chdir("Output")
			os.chdir("Output_" + str(output_numb))

			sample_numb = numb_of_samples[p-1][a-1]


			for i in range(1, sample_numb + 1): 

				sample_size = size_of_samples[p-1][a-1]

				# Create the file 
				os.chdir("P" + str(p) + "_Output")
				os.chdir("P" + str(p) + "_Samples")
				fwrite = "P" + str(p) + "A" + str(a) + " Sample " + str(i) + ".csv"

				if(not os.path.exists(fwrite)): 
					open(fwrite,'w').close()
				else: 
					print("The file P" + str(p) + "A" + str(a) + " Sample " + str(i) + ".csv already exists.")

				output = open(fwrite,'w') # open the file we want to write to 

				# Change directories to where base_file is located
				os.chdir("../") # now in Pp_Output
				os.chdir("../") # now in Output_o
				os.chdir("../") # now in Output 
				os.chdir("../") # now in the main folder 
				os.chdir("Base_files")
				os.chdir("P" + str(p))
				base_file = "P" + str(p) + "A" + str(a) + ".csv"

				# Figure out how many lines are in the base_file
				with open(base_file) as f: 
					lines_in_file = len(f.readlines())

				# Choose a random line from the base_file and write it to  fwrite 
				for k in random.sample(range(1, lines_in_file + 1), sample_size): 
					output.write(linecache.getline(base_file, k))

				linecache.clearcache()
				output.close()
				f.close() # might not need this


				# Change the directory to Output_o 
				os.chdir("../") # now in Base_files
				os.chdir("../") # now in the main folder
				os.chdir("Output")
				os.chdir("Output_" + str(output_numb))

			os.chdir("../")
			os.chdir("../")
		