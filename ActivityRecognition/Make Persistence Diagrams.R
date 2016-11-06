# Given a list of files, this writes the persistence diagram corresponding to each file 
# Example: 
# p = 1 
# numb_of_samples = 5
# We are assuming that we have the files P1A1 - Sample 1.csv, ..., P1A7 - Sample 5.csv in the folder
#


# INITAILIZE THESE VARIABLES 
# numb_of_samples: the number of samples
# p: the p-th person 
# start_of_directory: the beginning on the path; You can move the folder "P1" but DO NOT RENAME IT
start_of_path = "~/Documents/ActivityRecognition/"
output_numb = 1
#numb_of_samples = c(c(1,2,3,4,5,6,7),c(1,2,3,4,5,6,7),c(1,2,3,4,5,6,7),c(1,2,3,4,5,6,7),c(1,2,3,4,5,6,7),c(1,2,3,4,5,6,7),c(1,2,3,4,5,6,7),c(1,2,3,4,5,6,7),c(1,2,3,4,5,6,7),c(1,2,3,4,5,6,7),c(1,2,3,4,5,6,7),c(1,2,3,4,5,6,7),c(1,2,3,4,5,6,7),c(1,2,3,4,5,6,7),c(1,2,3,4,5,6,7))

numb_of_samples <- c()
for (p in c(1:15)){
  numb_of_samples <- c(numb_of_samples, c(10,10,10,10,10,10,10))
}




library(TDA)


for (p in range(1:15))
{
  
  directory = paste(c("~/Documents/ActivityRecognition/Output/Output_", output_numb, "/P", p, "_Output/P", p, "_Samples"), collapse = '')
  setwd(directory)
  
  Pperson_samples = c(numb_of_samples[(p*7) - 6], numb_of_samples[(p*7) - 5], numb_of_samples[(p*7) - 4], numb_of_samples[(p*7) - 3], numb_of_samples[(p*7) - 2], numb_of_samples[(p*7) - 1], numb_of_samples[(p*7)]) 
  
  # Create the list of files 
  files <-c()
  for (a in c(1:7))
  {
    for (i in c(1:Pperson_samples[a]))
    {
      files <- c(files, paste(c(start_of_path,"Output/Output_", output_numb, "/P", p, "_Output/P", p, "_Samples/P", p, "A", a," Sample ", i, ".csv"), collapse = ''))
    }
  }
  
  
  
  
  # Compute the persistence diagram for every file and save it in persist_diag
  persist_diag <- c()
  
  for (file in files)
  {
    # Importing and prepping the data
    number.of.columns <- 5 # the number of columns in your data file
    delimiter <- "," # this is what separates the values in your data file
    lines <- readLines(file, -1L) 
    values <- unlist(lapply(lines, strsplit, delimiter, fixed=TRUE))
    data <- matrix(values, byrow=TRUE, ncol=number.of.columns)
    
    # gets rid of the first and fifth columns
    data <- data[,2:4] 
    
    # changes the values to numerics ones and creates a matrix
    data <- matrix(as.numeric(data), byrow = F, ncol = 3) 
    
    
    # Creating the persistence diagram
    maxscale <- 5
    maxdimension <- 1
    Diag <- ripsDiag(data, maxdimension, maxscale, library = "Dionysus",
                     location = TRUE, printProgress = TRUE)
    #plot(Diag[["diagram"]])
    persist_diag <-c(persist_diag, Diag)
  }
  
  setwd("../")
  setwd("../")
}


# Now, we will create the images of all our persistence diagrams in put them in their respective folders
for (p in c(1:15)){
  setwd(paste(c("P", p, "_Output"), collapse ='')) # now in Pp_Output
  setwd(paste(c("P", p, "_Persistence_Diagrams"), collapse=''))

  for (a in c(1:7))
  {
    for (i in c(1:Pperson_samples[a]))
    {
      jpeg(file = paste(c(start_of_path, "Output/Output_", output_numb, "/P", p, "_Output/P", p, "_Persistence_Diagrams/P", p, "A", a,"_Persistence_Diagrams/Sample ", i, ".jpeg"), collapse = ''))
      
      # jpeg(file = paste(c(start_of_path,"P",p,"/P", p, "A", a," - Persistence Diagrams/Sample ", i, ".jpeg"), collapse = ''))
      plot(persist_diag[1 + 4*i - 4][["diagram"]])
      dev.off()
    }
  }
  setwd("../")
  setwd("../")
}
