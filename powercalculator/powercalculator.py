from Tkinter import *
import tkMessageBox as mbox

def calculator(n):
    return n

class PowerCalc(Frame):

    def __init__(self,parent): #Initializes when run
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
        self.centerWindow()
      
    def initUI(self): #Stuff relating to the GUI apperance goes here)
        self.parent.title("Balanced ANOVA")
        self.grid(row=0, column = 0)
        self.rowconfigure(0, pad=3)
      
        inputframe = Frame(self)
        inputframe.grid(row=0,column=0,columnspan=2)
     
        ninputframe = Frame(self)
        ninputframe.grid(row=1,column=0, sticky = N)
        ninputframe.columnconfigure(0,pad=3)
        
        buttonframe = Frame(self)
        buttonframe.grid(row=1,column=1)
        buttonframe.columnconfigure(0,pad=3)
     
        Alabel1 = Label(inputframe, text="Mean A1B1")
        Alabel1.grid(row = 1, column = 1)
        self.Aentry1 = Entry(inputframe, width = 6) #We do this to make Aentry1 an attribute of self (the current class)
        self.Aentry1.grid(row = 1, column = 2) #This allows us to access it with other methods in the same class.
        
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
        
        #command tells us what to do with it. specifically, call the quit() method on the self
        subjectnumber = Label(ninputframe, text="Total N")
        subjectnumber.grid(row=0, column = 0, sticky = N)
        self.totalN = Entry(ninputframe, width = 6)
        self.totalN.grid(row=0, column = 1)
        
        analyzeButton = Button(buttonframe, text = "Analyze", command = self.analyze)
        analyzeButton.grid(row=0, column=0, sticky = W)
        quitButton = Button(buttonframe, text="Quit", command = self.quit)
        quitButton.grid(row=1, column=0, sticky = W)       
        
    def analyze(self):
        meanA1 = float(self.Aentry1.get())
        meanA2 = float(self.Aentry2.get())
        meanB1 = float(self.Bentry1.get())
        meanB2 = float(self.Bentry2.get())
        sdA1 = float(self.SDAentry1.get())
        sdA2 = float(self.SDAentry2.get())
        sdB1 = float(self.SDBentry1.get())
        sdB2 = float(self.SDBentry2.get())
        totalN = float(self.totalN.get())
        
        marginalA1 = (meanA1 + meanB1)/2
        marginalA2 = (meanA2 + meanB2)/2

        marginalB1 = (meanA1 + meanA2)/2
        marginalB2 = (meanB1 + meanB2)/2
             
        rowmeans = (marginalA1 + marginalA2)/2
        colmeans = (marginalB1 + marginalB2)/2
         
        VarA1 = sdA1**2
        VarA2 = sdA2**2
        VarB1 = sdB1**2
        VarB2 = sdB2**2
        MSE = (VarA1 + VarA2 + VarB1 + VarB2)/4
        
        GrandMean =  (meanA1 + meanA2 + meanB1 + meanB2)/4
        SSTotal = (((meanA1 - GrandMean)**2 + (meanA2 - GrandMean)**2 + (meanB1 - GrandMean)**2 + \
         (meanB2 - GrandMean)**2) * totalN)/4
        SSRows = (((marginalA1 -  rowmeans)**2 + (marginalA2 - rowmeans)**2) * totalN)/2
        SSColumns = (((marginalB1-  colmeans)**2 + (marginalB2 - colmeans)**2) * totalN)/2
        SSInteraction = SSTotal - SSRows - SSColumns
        
        FRows = SSRows/MSE
        FColumns = SSColumns/MSE
        FInteraction = SSInteraction/MSE
        
        
        mbox.showinfo( "Results", "FRows = %s \nFColumns = %s \nFInteraction %s" % (FRows, FColumns, FInteraction))
        
    def centerWindow(self):
        w = 210
        h = 140
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        
        x = (sw - w)/2
        y = (sh -h)/2
        self.parent.geometry("%dx%d+%d+%d" % (w, h, x, y))

        
def main():
    root = Tk() #Initialize tk
    app = PowerCalc(root) #Run our power calculator program
    root.mainloop()

if __name__ == '__main__':
    main()