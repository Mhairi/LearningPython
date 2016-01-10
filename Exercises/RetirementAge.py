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
     
        agelabel = Label(inputframe, text = "Age")
        agelabel.grid(row = 2, column = 0)
        self.ageinput = Entry(inputframe, width = 10)
        self.ageinput.grid(row = 2, column = 1)
     
        lifeexpectancylabel = Label(inputframe, text = "Life Expectancy")
        lifeexpectancylabel.grid(row = 3, column = 0)
        self.lifeexpectancyinput = Entry(inputframe, width = 10)
        self.lifeexpectancyinput.grid(row = 3, column =1)
         
        buttonframe = Frame(self)
        buttonframe.grid(row = 1, column = 0)
        
        calculatebutton = Button(buttonframe, text = "Calculate", command = self.calculate)
        calculatebutton.grid(row = 0, column = 0)
     
    def calculate(self):
        income = float(self.incomeinput.get())
        expenses = float(self.expensesinput.get())
        age = float(self.ageinput.get()) * 12
        lifeexpectancy = float(self.lifeexpectancyinput.get()) * 12
        
        savings = income - expenses #Every month we save this much
        workingmonths = 0

        excess = 10
        bank = 9
        
        while excess > bank:
            workingmonths = workingmonths + 1
            age += 1 #we age by one more month
            monthstogo = (lifeexpectancy - age)
            excess = monthstogo * expenses  
            bank = savings * workingmonths #every month, we pay off some of that life debt
        
        workingyears = workingmonths/12
                
        messagebox.showinfo("Results", workingyears)
     
def main(): #This is our "main" function
    root = Tk() #initialize Tkinter
    app = RetirementCalc(root)
    root.mainloop()
    
if __name__ == '__main__': #if __name__ is itself (vs. a program that might be importing it, which would be main)
    main()
     