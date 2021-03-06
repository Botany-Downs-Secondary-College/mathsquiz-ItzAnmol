#Welcome.py
#MathsQuiz app
#A.Pandey, Feb 11

#importing all modules from tkinter
from tkinter import*

#Declare Parent class called MathsQuiz. All objects created from parent class
class MathsQuiz:
    #use init method for all widgets
    def __init__(self, parent):
        
        #Widgets for Welcome Frame
        
        self.Welcome = Frame(parent)
        self.Welcome.grid(row=0, column=0)
        
        self.TitleLabel = Label(self.Welcome, text = "Welcome to Maths Quiz",
                                bg = "black", fg = "white", width = 20, padx = 30, pady = 10,
                                font = ("Time", '14', "bold italic"))
        self.TitleLabel.grid(columnspan = 2)
        
        self.NextButton = Button(self.Welcome, text = 'Next')
        self.NextButton.grid(row = 8, column = 1)
        
#Main routine
if __name__ == "__main__":
    root =Tk()
    frames = MathsQuiz(root)
    root.title("Quiz")
    root.mainloop()