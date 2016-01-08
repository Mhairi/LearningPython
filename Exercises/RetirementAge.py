try: #If python2
    from Tkinter import *
    import tkMessageBox as messagebox
except ImportError:
    from tkinter import *
    from tkinter import messagebox
    
class RetirementCalc(Frame):
    def __init__(self, parent): #Runs on initialization of the class
        Frame.__init__(self,parent) #This is the top level frame
        self.parent = parent  #Sets itself as parent?
        self.initUI()
        self.centerWindow() #Runs centerWindow on init
        
    def centerWindow(self):
     #Define height and width
     w = 250
     h = 150
     screenwidth = self.parent.winfo_screenwidth()
     screenheight = self.parent.winfo_screenheight()
     
     x = (screenwidth - w) / 2
     y = (screenheight - h) /2
     self.parent.geometry("%dx%d+%d+%d" % (w,h,x,y)) #Sets coordinates for main window to appear
     
    def initUI(self):
        self.parent.title("Retirement Calculator") #Title
        self.grid(row = 0, column = 0) 
        
        inputframe = Frame(self) #Creates a sub-frame within "self"
        inputframe.grid(row = 0, column = 0) #Grids frame at top left
        
        incomelabel = Label(inputframe, text = "Monthly Income") #Creates a new label handle for income
        incomelabel.grid(row = 0, column = 0) #Grids label top left
        self.incomeinput = Entry(inputframe, width = 10) #Creates a new handle that's part of self for the input textbox
        self.incomeinput.grid(row=0, column = 1) #Grids top right
        
        expenseslabel = Label(inputframe, text = "Monthly Expenses")
        expenseslabel.grid(row = 1, column = 0)
        self.expensesinput = Entry(inputframe, width = 10)
        self.expensesinput.grid(row=1, column = 1)
     
        buttonframe = Frame(self)
        buttonframe.grid(row = 1, column = 0)
        
        calculatebutton = Button(buttonframe, text = "Calculate", command = self.calculate)
        calculatebutton.grid(row = 0, column = 0)
     
    def calculate(self):
        income = float(self.incomeinput.get())
        expenses = float(self.expensesinput.get())
        
        messagebox.showinfo("Results", [income, expenses])
     
def main(): #This is our "main" function
    root = Tk() #initialize Tkinter
    app = RetirementCalc(root)
    root.mainloop()
    
if __name__ == '__main__': #if __name__ is itself (vs. a program that might be importing it, which would be main)
    main()
     