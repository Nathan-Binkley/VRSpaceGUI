# import io, sys, glob
#
# def discover():
#     for name in glob.glob('VR Projects/Shortcuts to Demos/*'):
#         if name[-4:] == ".lnk":
#             print(name)
#
#
# discover()
#

from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E
import io, sys, glob, os

def discover():
    count = 0
    global files
    global links
    links = []
    files = []
    for name in glob.glob('VR Projects/Shortcuts to Demos/*'):
        if name[-4:] == ".lnk":
            files.append(name)
            links.append(name[31:-4])
            count += 1
    print(str(links))
    print(str(files))

class ProjectGUI:
    def __init__(self, master):
        discover()
        self.master = master
        master.title("Project GUI")

        self.total = 0
        self.entered_number = 0

        #self.total_label_text = IntVar()
        #self.total_label_text.set(self.total)
        #self.total_label = Label(master, textvariable=self.total_label_text)

        #self.label = Label(master, text="Total:")

        ####
        #Instructions to add
        #
        # Come up with a special unique and descriptive name for your Project
        # count = last file count + 1
        # Name: <insert name here>
        #
        # Put your name in the line below in place of <name> (keep the quotes)
        # self.button_<name> = Button(master, text=links[count], command=lambda: self.update("<name>"))
        #
        # Under #LAYOUT section, put line below replaced with your project name in place of <name>
        # (The system works like a grid, please try and keep it somewhat visually pleasing)
        # self.button_<name>.grid(row=0,column=1,rowspan=1, padx=10, pady=10, sticky=W+E)
        #
        # under the "update(self,method)" function, copy this line while replacing <name> with your Project
        #
        #
        # elif method == "<name>":
        # Press Tab (Very important)
        #   os.startfile('C:\\Users\\VSpace2\\Desktop\\' + files[count])
        #
        ####






        vcmd = master.register(self.validate) # we have to wrap the command
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))


        #self.discover_button = Button(master, text="Discover", command=lambda: self.update("discover"))
        try:
            self.button_carpenter = Button(master, text=links[0], command=lambda: self.update("carpenter"))
            self.button_framing = Button(master, text=links[1], command=lambda: self.update("framing"))
            self.button_geology = Button(master, text=links[2], command=lambda: self.update("geology"))
            self.button_house1 = Button(master, text=links[3], command=lambda: self.update("house1"))
            self.button_house2 = Button(master, text=links[4], command=lambda: self.update("house2"))
            self.button_house3 = Button(master, text=links[5], command=lambda: self.update("house3"))
            self.button_littlejohn = Button(master, text=links[6], command=lambda: self.update("littlejohn"))
            self.button_safari = Button(master, text=links[7], command=lambda: self.update("safari"))
            self.button_sickness = Button(master, text=links[8], command=lambda: self.update("sickness"))
            # Chris' list code stuff
            # self.buttonsList = []
            # buttonTypes = ["carpetenter", "framing", "geology"]
            # for i, button in enumerate(self.buttonTypes):
            #     self.buttonList.append(Button(master, text=links[i], command=lambda: self.update(button)))
            #
            # for i, button in enumerate(self.buttonList):
            #     button.grid(row=0,column=1,rowspan=1, padx=10, pady=10, sticky=W+E)
            #
            #

            # LAYOUT

            #self.label.grid(row=0, column=0, sticky=W)

            #self.discover_button.grid(row=0, column=0, sticky=W+E)
            self.button_carpenter.grid(row=0,column=1,rowspan=1, padx=10, pady=10, sticky=W+E)
            self.button_framing.grid(row=0,column=3,rowspan=1, padx=10, pady=10, sticky=W+E)
            self.button_geology.grid(row=0,column=5,rowspan=1, padx=10, pady=10, sticky=W+E)
            self.button_house1.grid(row=2,column=1,rowspan=1, padx=10, pady=10, sticky=W+E)
            self.button_house2.grid(row=2,column=3,rowspan=1, padx=10, pady=10, sticky=W+E)
            self.button_house3.grid(row=2,column=5,rowspan=1, padx=10, pady=10, sticky=W+E)
            self.button_littlejohn.grid(row=4,column=1,rowspan=1, padx=10, pady=10, sticky=W+E)
            self.button_safari.grid(row=4,column=3,rowspan=1, padx=10, pady=10, sticky=W+E)
            self.button_sickness.grid(row=4,column=5,rowspan=1, padx=10, pady=10, sticky=W+E)
        except IndexError:
            print("Not enough files in src folder (VR Projects/Shortcuts to Demos)")
        except:
            pass




    def validate(self, new_text):
        if not new_text: # the field is being cleared
            self.entered_number = 0
            return True

        try:
            self.entered_number = int(new_text)
            return True
        except ValueError:
            return False

    def update(self, method):

        if method == "carpenter":
            os.startfile('C:\\Users\\VSpace2\\Desktop\\' + files[0])
        elif method == "framing":
            os.startfile('C:\\Users\\VSpace2\\Desktop\\' + files[1])
        elif method == "geology":
            os.startfile('C:\\Users\\VSpace2\\Desktop\\' + files[2])
        elif method == "house1":
            os.startfile('C:\\Users\\VSpace2\\Desktop\\' + files[3])
        elif method == "house2":
            os.startfile('C:\\Users\\VSpace2\\Desktop\\' + files[4])
        elif method == "house3":
            os.startfile('C:\\Users\\VSpace2\\Desktop\\' + files[5])
        elif method == "littlejohn":
            os.startfile('C:\\Users\\VSpace2\\Desktop\\' + files[6])
        elif method == "safari":
            os.startfile('C:\\Users\\VSpace2\\Desktop\\' + files[7])
        elif method == "sickness":
            os.startfile('C:\\Users\\VSpace2\\Desktop\\' + files[8]) #<-- Last file count.
        else: # reset
            pass #re-scan for items in future

        self.total_label_text.set(self.total)
        self.entry.delete(0, END)


root = Tk()
my_gui = ProjectGUI(root)
root.mainloop()
