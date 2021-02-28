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

os.chdir(path)
menu(user,path,default,terminalEmulator,entry)

