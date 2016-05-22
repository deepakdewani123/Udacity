import os
def rename_files():
##    1. get all the files
	directory =   os.listdir(os.getcwd())
##    2. rename the files
	# print(directory)
	ep_name = "Narcos.S01E"
	for file_name in directory:
		# file = file_name
		if file_name.endswith("srt"):
			print(file_name)
			inc = 1
			print(inc)
			os.rename(file_name,ep_name+str(inc)+".srt")
			inc+=1

rename_files()
