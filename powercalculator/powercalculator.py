from Tkinter import * #This is the GUI that comes with python
import tkMessageBox as mbox #For our mssage box later

class TwoWay(Frame):
    def __init__(self,parent): #Initializes when run
        Frame.__init__(self, parent) #This initializes our top level frame
        self.parent = parent  #Sets self (TwoWay) as the parent
        self.initUI() #Runs initUI when a TwoWay class is initialized
        self.centerWindow() #Runs centerWindow when a TwoWay class is initialized
      
    def initUI(self): #Stuff relating to the GUI apperance goes here)
        self.parent.title("Balanced ANOVA") #Sets the window title
        self.grid(row=0, column = 0) #This is the largest grid
      
        inputframe = Frame(self) #This creates a sub-frame within "self" (see above)
        inputframe.grid(row=0,column=0,columnspan=2) #This starts at row 0, column 0 and spans 2 columns (to align with the buttons below)
     
        ninputframe = Frame(self) #Creates another sub-frame within "self" for our Ns input
        ninputframe.grid(row=1,column=0, sticky = N) #First row of the frame (below inputframe)
        ninputframe.columnconfigure(0,pad=3) #Padding for alignment
        
        buttonframe = Frame(self) #Creats another sub-frame within "self" for our Buttons
        buttonframe.grid(row=1,column=1) #Below inputframe and to the right of ninputframe
     
        Alabel1 = Label(inputframe, text="Mean A1B1") #Creats a new label
        Alabel1.grid(row = 1, column = 1) 
        self.Aentry1 = Entry(inputframe, width = 6) #We do this to make Aentry1 an attribute of self (the current class)
        self.Aentry1.grid(row = 1, column = 2) #This allows us to access it with other methods in the same class.
        
        #The following do the same thing for our other variables:
        Alabel2 = Label(inputframe, text="Mean A2B1")
        Alabel2.grid(row = 2, column = 1)
        self.Aentry2 = Entry(inputframe,width = 6)
        self.Aentry2.grid(row = 2, column = 2)
        
        Blabel1 = Label(inputframe, text="Mean A1B2")
        Blabel1.grid(row = 1, column = 3)
        self.Bentry1 = Entry(inputframe, width = 6)
        self.Bentry1.grid(row = 1, column = 4)
        
        Blabel2 = Label(inputframe, text="Mean A2B2")
        Blabel2.grid(row = 2, column = 3)
        self.Bentry2 = Entry(inputframe,width = 6)
        self.Bentry2.grid(row = 2, column = 4)
        
        SDAlabel1 = Label(inputframe, text="SD A1B1")
        SDAlabel1.grid(row = 4, column = 1)
        self.SDAentry1 = Entry(inputframe, width = 6)
        self.SDAentry1.grid(row = 4, column = 2)
        
        SDAlabel2 = Label(inputframe, text="SD A2B1")
        SDAlabel2.grid(row = 5, column = 1)
        self.SDAentry2 = Entry(inputframe,width = 6)
        self.SDAentry2.grid(row = 5, column = 2)
        
        SDBlabel1 = Label(inputframe, text="SD A1B2")
        SDBlabel1.grid(row = 4, column = 3)
        self.SDBentry1 = Entry(inputframe, width = 6)
        self.SDBentry1.grid(row = 4, column = 4)
        
        SDBlabel2 = Label(inputframe, text="SD A2B2")
        SDBlabel2.grid(row = 5, column = 3)
        self.SDBentry2 = Entry(inputframe,width = 6)
        self.SDBentry2.grid(row = 5, column = 4)
        
        subjectnumber = Label(ninputframe, text="Total N")
        subjectnumber.grid(row=0, column = 0, sticky = N)
        self.totalN = Entry(ninputframe, width = 6)
        self.totalN.grid(row=0, column = 1)
        
         #command tells us what to do when the button is pressed, specificall, call the quit() method on the self, or the analyze method
        #Creates a new Button object within buttonframe
        analyzeButton = Button(buttonframe, text = "Analyze", command = self.analyze) 
        #.grid tells us where it goes
        analyzeButton.grid(row=0, column=0, sticky = W)
        quitButton = Button(buttonframe, text="Quit", command = self.quit)
        quitButton.grid(row=1, column=0, sticky = W)       
        
    def analyze(self):
    
        #Let's get all the variables from the TwoWay class (referenced as "self", because this function is within the class)
        #This is why we had the self. prefix earlier
        #We get with the .get() function, and convert to float()
        meanA1 = float(self.Aentry1.get())
        meanA2 = float(self.Aentry2.get())
        meanB1 = float(self.Bentry1.get())
        meanB2 = float(self.Bentry2.get())
        sdA1 = float(self.SDAentry1.get())
        sdA2 = float(self.SDAentry2.get())
        sdB1 = float(self.SDBentry1.get())
        sdB2 = float(self.SDBentry2.get())
        totalN = float(self.totalN.get())
        
        #The following code calculates the results of a balanced two-way ANOVA
        #These are the marginal means for A
        marginalA1 = (meanA1 + meanB1)/2
        marginalA2 = (meanA2 + meanB2)/2
        #These are the marginal means for B
        marginalB1 = (meanA1 + meanA2)/2
        marginalB2 = (meanB1 + meanB2)/2
        
        #These are the column and row means
        rowmeans = (marginalA1 + marginalA2)/2
        colmeans = (marginalB1 + marginalB2)/2
         
        #These are the cell variances (used to calculate error)
        VarA1 = sdA1**2
        VarA2 = sdA2**2
        VarB1 = sdB1**2
        VarB2 = sdB2**2
        MSE = (VarA1 + VarA2 + VarB1 + VarB2)/4
        
        #Calculating sums of squares
        GrandMean =  (meanA1 + meanA2 + meanB1 + meanB2)/4
        SSTotal = (((meanA1 - GrandMean)**2 + (meanA2 - GrandMean)**2 + (meanB1 - GrandMean)**2 + \
         (meanB2 - GrandMean)**2) * totalN)/4
        SSRows = (((marginalA1 -  rowmeans)**2 + (marginalA2 - rowmeans)**2) * totalN)/2
        SSColumns = (((marginalB1-  colmeans)**2 + (marginalB2 - colmeans)**2) * totalN)/2
        SSInteraction = SSTotal - SSRows - SSColumns
        
        #Calculating F-ratios
        FRows = SSRows/MSE
        FColumns = SSColumns/MSE
        FInteraction = SSInteraction/MSE
         
        #Displays a message box with our results."
        mbox.showinfo( "Results", "FRows = %s \nFColumns = %s \nFInteraction %s" % (FRows, FColumns, FInteraction))
        
    def centerWindow(self):
        #We do this to center the window in the screen
        #Define height and width
        w = 210
        h = 140
        #Get screen width and height
        sw = self.parent.winfo_screenwidth() 
        sh = self.parent.winfo_screenheight()
        
        x = (sw - w)/2
        y = (sh -h)/2
        self.parent.geometry("%dx%d+%d+%d" % (w, h, x, y)) #Sets coordinates for the main window to appear

        
def main(): #This is our "main" function
    root = Tk() #Initialize tk
    app = TwoWay(root) #Run our power calculator program
    root.mainloop()

#The following checks to see if the current module is being interpreted directly, or being imported by another module.
#If run from the interpreter, __name__ is set to __main__ by the python interpreter.
#otherwise, __name__ is set to whatever is importing it
#The following check thus only executes when the code is being run from the interpreter.

if __name__ == '__main__': 
    main() #Run main()