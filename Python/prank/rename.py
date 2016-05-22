import os
def rename_files():
##    1. get all the files
        directory =   os.listdir(os.getcwd())
##    2. rename the files
        for file_name in directory :
                file = file_name
                os.rename(file_name,file.encode('ASCII').translate(None,b'0123456789'))
                
rename_files()
