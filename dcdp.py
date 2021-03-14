# Module
import dmenu
import os
import getpass

# Global variable
user = str(getpass.getuser())
path = "/home/"+user+"/Documents"
entry = path
data_file = '/var/tmp/dcdp.txt'
# Here you can choose your default terminal emulator tested: xfce4-terminal,gnome-terminal
terminalEmulator="gnome-terminal"
file_manager="nautilus"


def list_dir(location):
	files_in_dir = []
	# r=>root, d=>directories, f=>files
	for r, d, f in os.walk(location):
		for item in d:
			files_in_dir.append(os.path.join(r, item))
	return files_in_dir

if not os.path.exists(data_file):
	print("create")
	with open(data_file, 'w') as f: 
		list_all=list_dir(path)
		for element in list_all:
			if len(element) > 1 and element[0] != " ":
				f.write(element)
				f.write('\n')
		f.close()
		pass
else:
	file_size = os.path.getsize(data_file)
	print("show")
	if file_size < 1:
		print("write")
		list_all=list_dir(path)
		with open(data_file, 'w') as f: 
			for element in list_all:
				if len(element) > 1 and element[0] != " ":
					f.write(element)
					f.write('\n')
			f.close()
			pass	
	with open(data_file, 'r') as f: 
		print("show")
		list_all=f.readlines()
		f.close()
		pass

#select element
entry = dmenu.show(list_all)
#update list
if list_all[0] != entry:
	for element in list_all:
		if entry == element:
			tmp=element
			print(tmp)
			list_all.remove(tmp) 
			list_all.insert(0, tmp)
			print(list_all)
	with open(data_file, 'w') as f: 
		for element in list_all:
			if len(element) > 1 and element[0] != " ":
				f.write(element)
				f.write('\n')
		f.close()
		pass

path = entry
entry = dmenu.show([file_manager,terminalEmulator])
if entry == terminalEmulator:
	os.chdir(path)
	os.system(str(terminalEmulator)+" --working-directory="+os.getcwd())
	exit()
elif entry == file_manager:
	os.system(file_manager+" "+path)
	exit()
else:
	print("invalid option")
	exit()
