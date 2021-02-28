# Module
import dmenu
import os
import getpass

# Global variable
enter="enter"
user = str(getpass.getuser())
default = ["..",enter]
path = "/home/"+user
terminalEmulator="xfce4-terminal"
entry = path

def list_dir(location):
	files_in_dir = []
	# r=>root, d=>directories, f=>files
	for r, d, f in os.walk(location):
		for item in d:
			files_in_dir.append(os.path.join(r, item))
	return files_in_dir

list_all=list_dir(path)
entry = dmenu.show(list_all)
path=entry
os.chdir(path)
os.system(str(terminalEmulator)+" --working-directory="+os.getcwd())




