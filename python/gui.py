

from tkinter import *

root = Tk()
#county selection
frame = Frame(root)
frame.pack(fill = BOTH, pady = 10, padx = 50, side = 'left')
countyLabel = Label(frame,text = 'County')
countyLabel.pack()

#all counties in Florida in order corresponding to the site
counties = {'ALACHUA','BAKER','BAY','BRADFORD','BREVARD','BROWARD','CALHOUN','CHARLOTTE','CITRUS','CLAY','COLLIER','COLUMBIA','DESOTO','DIXIE','DUVAL','ESCAMBIA','FLAGLER','FRANKLIN','GADSDEN','GILCHRIST','GLADES','GULF','HAMILTON','HARDEE','HENDRY','HERNANDO','HIGHLANDS','HILLSBOROUGH','HOLMES','INDIAN RIVER','JACKSON','JEFFERSON','LAFAYETTE','LAKE','LEE','LEON','LEVY','LIBERTY','MADISON','MANATEE','MARION','MARTIN','MIAMI-DADE','MONROE','NASSAU','OKALOOSA','OKEECHOBEE','ORANGE','OSCEOLA','PALM BEACH','PASCO','PINELLAS','POLK','PUTNAM','SANTA ROSA','SARASOTA','SEMINOLE','ST.JOHNS','ST.LUCIE','SUMTER','SUWANNEE','TAYLOR','UNION','VOLUSIA','WAKULLA','WALTON','WASHINGTON'}
#variable that will hold the value of whats selected
countyChoice = StringVar(root)
countyChoice.set('--not selected--')
#option menu that will be in the window
countyMenu = Listbox(frame)
countyMenu.pack(side = 'left')
countyMenu.insert(END, *counties)

scroll = Scrollbar(frame, orient= VERTICAL)
scroll.config(command = countyMenu.yview)
scroll.pack(side = 'right', fill = 'y')

countyMenu.config(yscrollcommand = scroll.set ,width = 20, height = 10)
#this frame area holds the rest of the widgets
quotaFrame = Frame(root)
quotaFrame.pack(fill = BOTH, pady = 10, padx = 30, side = 'right')
quotaLabel = Label(quotaFrame,text = 'number of pages')
quotaLabel.grid(row = 0, column =0)
quotaBox = Spinbox(quotaFrame, from_=1,to=500)
quotaBox.config(width = 4)
quotaBox.grid(row = 0, column = 1)

def init():
    root.title("CNADOWS")

    root.mainloop()

if __name__ == '__main__':
    init()