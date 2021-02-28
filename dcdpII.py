# Module
import dmenu
import os
import getpass



def listall(location):
	files_in_dir = []
	# r=>root, d=>directories, f=>files
	for r, d, f in os.walk(location):
		for item in d:
			files_in_dir.append(os.path.join(r, item))
	return files_in_dir


# Global variable
enter="enter"
user = str(getpass.getuser())
default = ["..",enter]
path = "/home/"+user
terminalEmulator="xfce4-terminal"
entry = path

def list_files(path,default):
	grid=[]
	show_hidden = False
	files = os.listdir(path)
	for x in files:
		if x[:1]==".":
			if show_hidden is True:
				grid.append(x)
		else:
			grid.append(x)
	grid.sort(key=str.casefold)
	grid=default+grid
	grid.append("exit")
	return grid

def menu(user,path,default,terminalEmulator,entry):
	grid = list_files(path,default)
	entry = dmenu.show(grid, prompt=os.getcwd())
	if entry != enter:
		if entry == "exit":
			exit()
		path = os.chdir(entry)
		menu(user,path,default,terminalEmulator,entry)
	else:
		os.system(str(terminalEmulator)+" --working-directory="+os.getcwd())
		exit()

list_all=listall(path)
list_end=[]
for x in list_all:
	x=x.split("/")
	x = x[len(x)-1]
	list_end.append(x)

entry = dmenu.show(list_end)
index = list_end.index(entry)
path=list_all[index]

os.chdir(path)
os.system(str(terminalEmulator)+" --working-directory="+os.getcwd())




