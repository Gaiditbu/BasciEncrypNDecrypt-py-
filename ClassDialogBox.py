from tkinter import *
from tkinter import filedialog
from PIL import Image,ImageTk
from tkinter import font

class CPath():
    def __init__(self):
        self.root=''
        self.path=''
        
    def getPath(self):
        self.root = Tk()
        self.root.withdraw()
        self.path=filedialog.askopenfilename()
        return self.path

def run():
    win =Tk()
    path=CPath()
    a=path.getPath()
    print(a)

if __name__=='__main__':
    run()

