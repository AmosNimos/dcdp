# Module
import dmenu
import os
import getpass

# Global variable
user = str(getpass.getuser())
path = "/home/"+user
entry = path

# Here you can choose your default terminal emulator tested: xfce4-terminal,gnome-terminal
terminalEmulator="gnome-terminal"


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
