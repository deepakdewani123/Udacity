import os
def rename_files():
##    1. get all the files
	directory =   os.listdir(os.getcwd())
##    2. rename the files
	ep_name = "Narcos.S01E"
	file_inc = 1
	for file_name in directory:
		# file = file_name
		if file_name.endswith("mkv"):
			os.rename(file_name,ep_name+str(file_inc)+".mkv")
			file_inc += 1

rename_files()
