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
terminal_emulator="gnome-terminal"
file_manager="nautilus"
text_editor="subl"
list_all = []
z = [None,"",'\n%s','','\n',"\n"," ","  "]	

def list_dir(location):
	files_in_dir = []
	# r=>root, d=>directories, f=>files
	for r, d, f in os.walk(location):
		for item in d:
			files_in_dir.append(os.path.join(r, item))
	return files_in_dir

if not os.path.exists(data_file):
	print("write")
	with open(data_file, 'w') as f: 
		list_all=list_dir(path)
		for element in list_all:
			f.write(element)
			f.write("!|!")
				#f.write('\n')
		f.close()
		pass


#file_size = os.path.getsize(data_file)
print("read")
list_all=[]
with open(data_file, 'r') as f:
	full = f.read()
	paths = full.split("!|!")
	for line in paths: 
		if str(line) not in z:
			list_all.append(str(line))
			print(line)
			
#select element
entry = ''
while entry == '':
	entry = dmenu.show(list_all)
#update list

if str(list_all[0]) != str(entry) and entry != None:
	print("work")
	for element in list_all:
		if str(element).rstrip() == str(entry).rstrip():
			print("element: "+str(element))
			list_all.remove(element) 
			if len(element) > 1 and element[0] != " ":
				list_all.insert(0, str(element))
	print("write")
	with open(data_file, 'w') as f: 
		for element in list_all:
			f.write(element)
			f.write("!|!")
		f.close()
		pass

path = entry
#entry = dmenu.show([terminal_emulator,text_editor,file_manager])
entry = terminal_emulator
if entry == terminal_emulator:
	os.chdir(path)
	os.system(str(terminal_emulator)+" --working-directory="+os.getcwd())
	exit()
elif entry == file_manager:
	os.system(file_manager+" "+path)
	exit()
elif entry == text_editor:
	os.system(text_editor+" "+path)
	exit()
else:
	print("invalid option")
	exit()
