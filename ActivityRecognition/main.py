import generate_samples
import os

# Hardcoded user input 
#numb_of_samples = [[500,500,500,500,500,500,500],[500,500,500,500,500,500,500],[500,500,500,500,500,500,500],[500,500,500,500,500,500,500],[500,500,500,500,500,500,500],[500,500,500,500,500,500,500],[500,500,500,500,500,500,500],[500,500,500,500,500,500,500],[500,500,300,500,500,500,500],[500,500,500,500,500,500,500],[500,500,500,500,500,500,500],[500,500,500,500,500,500,500]]
#size_of_samples = [[10,2,3,4,5,6,7],[1,2,3,4,5,6,7],[1,2,3,4,5,6,7],[1,2,3,4,5,6,7],[1,2,3,4,5,6,7],[1,2,3,4,5,6,7],[1,2,3,4,5,6,7],[1,2,3,4,5,6,7],[1,2,3,4,5,6,7],[1,2,3,4,5,6,7],[1,2,3,4,5,6,7],[1,2,3,4,5,6,7],[1,2,3,4,5,6,7],[1,2,3,4,5,6,7],[1,2,3,4,5,6,7]]
output_numb = 1


numb_of_samples = []
for p in range(1,16): 
	numb_of_samples.append([10,10,10,10,10,10,10])

size_of_samples = []
for p in range(1,16):
	size_of_samples.append([30,30,30,30,30,30,30])


# Create all one time folders 
generate_samples.create_output_folder()
#%%%%%%%%%%%%%%%%%%%%% ^ That should go in the other script.. we don't want it to be made every time 


# Create all folders which will be created after every execution 
os.chdir("Output") 

generate_samples.create_output_o_folder(output_numb)

os.chdir("Output_" + str(output_numb))

generate_samples.create_Pp_output_folders() 

generate_samples.create_Pp_sample_folders() 

generate_samples.create_Pp_persist_diag_folders()

# Make sure that we have inputted appropriate sample size requests
os.chdir("../")
os.chdir("../")
os.chdir("Base_files")
generate_samples.check_sample_sizes(numb_of_samples)

# Create the samples 
os.chdir("../") # Move into the main folder
generate_samples.create_samples(numb_of_samples, size_of_samples, output_numb)

