
from tkinter import *
from bot import startScrape

root = Tk()
root.resizable(width = False, height = False)
#county selection
frame = Frame(root)
frame.pack(fill = BOTH, pady = 10, padx = 50, side = 'left')

countyLabel = Label(frame,text = 'County', font = 12)
countyLabel.pack()

#all counties in Florida in order corresponding to the site
counties = ['ALACHUA','BAKER','BAY','BRADFORD','BREVARD','BROWARD','CALHOUN','CHARLOTTE','CITRUS','CLAY','COLLIER','COLUMBIA','DESOTO','DIXIE','DUVAL','ESCAMBIA','FLAGLER','FRANKLIN','GADSDEN','GILCHRIST','GLADES','GULF','HAMILTON','HARDEE','HENDRY','HERNANDO','HIGHLANDS','HILLSBOROUGH','HOLMES','INDIAN RIVER','JACKSON','JEFFERSON','LAFAYETTE','LAKE','LEE','LEON','LEVY','LIBERTY','MADISON','MANATEE','MARION','MARTIN','MIAMI-DADE','MONROE','NASSAU','OKALOOSA','OKEECHOBEE','ORANGE','OSCEOLA','PALM BEACH','PASCO','PINELLAS','POLK','PUTNAM','SANTA ROSA','SARASOTA','SEMINOLE','ST.JOHNS','ST.LUCIE','SUMTER','SUWANNEE','TAYLOR','UNION','VOLUSIA','WAKULLA','WALTON','WASHINGTON']
#option menu that will be in the window
countyMenu = Listbox(frame)
countyMenu.pack(side = 'left')
countyMenu.insert(END, *counties)

scroll = Scrollbar(frame, orient= VERTICAL)
scroll.config(command = countyMenu.yview)
scroll.pack(side = 'right', fill = 'y')

countyMenu.config(yscrollcommand = scroll.set, width = 20, height = 10)
#this frame area holds the rest of the widgets
quotaFrame = Frame(root)
quotaFrame.pack(fill = BOTH, pady = 10, padx = 30, side = 'right')
quotaLabel = Label(quotaFrame, text = 'number of pages', font = 12)
quotaLabel.grid(row = 0, column =0)
estimateLabel = Label(quotaFrame, text = 'Quota≈ 20 students', font = 12)
estimateLabel.grid(row = 1, column= 0)
def calculateQuota(quotaBox):
    estimateLabel.config(text = 'Quota≈ '+str(int(quotaBox.get())*20) + ' students')

quotaBox = Spinbox(quotaFrame, from_=1,to=500, state = 'readonly', command= lambda: calculateQuota(quotaBox))
quotaBox.config(width = 4, font = 12)
quotaBox.grid(row = 0, column = 1)


errorLabel = Label(quotaFrame, font = 12, fg = 'red')
errorLabel.grid(row=3,column = 0)

def start(startButton):

    if len(countyMenu.curselection())>0:
        startButton.config(state = DISABLED)
        countySelected = int(countyMenu.curselection()[0]+1)
        numberOfPages = int(quotaBox.get())
        print(numberOfPages)
        startScrape(countySelected,numberOfPages)

    else:
        errorLabel.config(text = "Please choose a county to pull from")

startButton = Button(quotaFrame, text = 'Start', command = lambda: start(startButton))
startButton.config(width = 20, font = 14)
startButton.grid(row=2, column = 0)

def init():
    root.title("CNA data web scraper")

    root.mainloop()

if __name__ == '__main__':
    init()