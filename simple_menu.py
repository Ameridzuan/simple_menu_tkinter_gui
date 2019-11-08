from Tkinter import *

class GUI_Menu:

    def __init__(self,master):
        
        #create pane
        self.master = master
        master.title("MENU")
        master.geometry('660x350+0+0')
        master.configure(background='#DADEEB')

        #create attribute
        self.getFilename = Button(master, text="SAY HELLO",bg="#30E7A1", font='Helvetica 12 bold', command = self.tellFilename)
        self.startInput = Button(master, text="WRITE SOMETHING",bg="#30E7A1", font='Helvetica 12 bold', command = self.inputSeq)
        self.quit = Button(master, text="QUIT",font='Helvetica 10 bold',bg="#FF3333", fg="black", command=master.destroy)
        self.desc = Button(master, text="DESCRIPTION",bg="#BEFDFC", command = self.desc)
        self.instruct = Button(master, text="INSTRUCTION",bg="#BEFDFC", command = self.inst)
        self.about = Button(master, text="ABOUT US",bg="#BEFDFC", command = self.about)

        #create function button
        self.fx1 = Button(master, text="OPTION 1", command = self.fx_1, bg="white", height = 5,width=30)
        self.fx2 = Button(master, text="OPTION 2", command = self.fx_2, bg="white", height = 5,width=30)
        self.fx3 = Button(master, text="OPTION 3", command = self.fx_3, bg="white", height = 5,width=30)
        self.fx4 = Button(master, text="OPTION 4", command = self.fx_4, bg="white", height = 5,width=30)
        self.fx5 = Button(master, text="OPTION 5", command = self.fx_5, bg="white", height = 5,width=30)
        self.fx6 = Button(master, text="OPTION 6", command = self.fx_6, bg="white", height = 5,width=30)

        #set layout
        self.about.grid(row=1, column=0, sticky=E+W, pady=5)
        self.getFilename.grid(row=2, column=1, sticky=E+W, pady=5)
        self.desc.grid(row=1, column=1, sticky=E+W, pady=5)
        self.instruct.grid(row=1, column=2, sticky=E+W, pady=5)
        self.startInput.grid(row=3, column=1,sticky=E+W, pady=5)
        self.quit.grid(row=6, column=2, sticky=E+W, pady=5)

        #set fx buttons layout
        self.fx1.grid(row=4,column=0,sticky=E+W)
        self.fx2.grid(row=4,column=1,sticky=E+W)
        self.fx3.grid(row=4,column=2,sticky=E+W)
        self.fx4.grid(row=5,column=0,sticky=E+W)
        self.fx5.grid(row=5,column=1,sticky=E+W)
        self.fx6.grid(row=5,column=2,sticky=E+W)

    def about(self):
        file = open("About.txt", "r") 
        print file.read()
        
    def desc(self):
        file = open("Description.txt", "r") 
        print file.read()

    def inst(self):
        file = open("Instruction.txt", "r") 
        print file.read()
        
    def tellFilename(self):
        print "Hello!"

    def inputSeq(self):
        filename = raw_input("Write something here: ")

    def fx_1(self):
        print "Option 1"
        
    def fx_2(self):
        print "Option 2"
    
    def fx_3(self):
        print "Option 3"
        
    def fx_4(self):
        print "Option 4"
        
    def fx_5(self):
        print "Option 5"
        
    def fx_6(self):
        print "Option 6"

root = Tk()
my_gui = GUI_Menu(root)
root.mainloop()
