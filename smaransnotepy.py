#Importing our GUI package
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

filename = None

def newFile():
    '''
    Function to create new file
    '''
    text.delete(0.0, END)


def openFile():
    '''
    Function for opening a file
    '''
    global filename
    filename = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("All Files","*.*"),("Text Files","*.txt")])
    if filename == " ":
        filename = None
    else:
        f = open(filename,"r")
        t = f.read()
        text.delete(0.0,END)
        text.insert(0.0,t)

def saveFile():
    '''
    Function to save a file
    '''
    global filename
    try:
        f = open(filename, "w")
        t = text.get(0.0, END)
        f.write(t)
        f.close()
    except:
        saveasFile()

def saveasFile():
    '''
    Function to save a file as decided by user
    '''
    f = filedialog.asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Files","*.txt")])
    t = text.get(0.0, END)
    try:
        fh = open(f,"w")
        fh.write(t.rstrip())
        fh.close()
    except:
        messagebox.showerror(title="Oh crap!", message="Failed to save the file.")


def exitEditor():
    '''
    Function to close the application
    '''
    exit()


def viewHelp():
    '''
    Function for help
    '''
    helpWindow=Toplevel()
    helpWindow.title("Help-Smaran's Notepy")
    helpWindow.geometry("600x100")
    helpWindow.config(background="orange")
    helpLabel = Label(helpWindow,text="Help", font=("Britannic Bold", 20), bg="orange").pack()
    details_help = Label(helpWindow,
        text="Use Smaran's Notepy to replace your hefty text editor with a Python powered cutie.\n Open,Edit and Save Files as you like!",
        font=("Helvetica",12),
        bg="orange",
    ).pack()

def viewAbout():
    '''
    Function for about
    '''
    aboutWindow=Toplevel()
    aboutWindow.title("About Smaran's Notepy")
    aboutWindow.geometry("500x150")
    aboutWindow.config(background="orange")
    aboutLabel = Label(aboutWindow,text="About", font=("Britannic Bold", 20), bg="orange").pack()
    details1_about = Label(aboutWindow,
        text="Smaran's Notepy v.0.0.1",
        font=("Helvetica",9),
        bg="orange"
    ).pack()
    details2_about = Label(aboutWindow,
        text="Smaran's Notepy is minimalistic notepad clone made using Python.\n For the source code behind it check out: \nwww.github.com/smaranjitghose/Smaransnotepy",
        font=("Helvetica",12),
        bg="orange"
    ).pack()



#Main Window
root = Tk()
root.title("Smaran's Notepy")
root.geometry("800x600")

#Menu Bar
menubar=Menu(root)
root.config(menu=menubar)

#File Menu
file_menu=Menu(menubar)
file_menu.add_command(label="New", command=newFile)
file_menu.add_command(label="Open", command=openFile)
file_menu.add_command(label="Save", command=saveFile)
file_menu.add_command(label="Save As", command=saveasFile)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exitEditor)
menubar.add_cascade(label="File",menu=file_menu)

#Help Menu
help_menu=Menu(menubar)
help_menu.add_command(label="View Help", command=viewHelp)
help_menu.add_separator()
help_menu.add_command(label="About", command=viewAbout)
menubar.add_cascade(label="Help", menu=help_menu)

text=Text(root)
text.pack(expand=True, fill=BOTH)

scrollbar_y = Scrollbar(text, orient='vertical')
text.configure(yscrollcommand=scrollbar_y.set)
scrollbar_y.config(command=text.yview)
scrollbar_y.pack(side=RIGHT, fill=Y)

root.mainloop()
