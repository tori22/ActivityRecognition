# Import modules
import os


# Import scripts
import general_methods




if __name__ == "__main__":

    ##############################################################################
    # Create all one-time folders and files
    ##############################################################################

    # Create all the one-time folders and files in ActivityRecogn
    os.chdir("../")
    
    general_methods.create_folder("Base_files")
    
    general_methods.create_file("General_info.txt")

    general_methods.create_folder("Output_files")

    # Create all the one-time folders and files in Base_files
    os.chdir("Base_files")

    for i in range(1,16):
        general_methods.create_folder("P" + str(i))
        
    os.chdir("../")

    # Create all the one-time folders and files in Pp (for all p)
    os.chdir("Base_files")
    for p in range(1,16):
        os.chdir("P" + str(p))

        for a in range(1,8):
            general_methods.create_file("P" + str(p) + "A" + str(a) + ".csv")
        os.chdir("../")
    os.chdir("../")

        
    ##############################################################################
    # Add appropriate values to the one-time files
    ##############################################################################

    general_methods.makePpAa()


    general_methods.add_to_general_info()


        
    ##############################################################################
    # Create all folders and files which will be created during every execution
    # Add the appropiate values to these folders and files
    ##############################################################################





