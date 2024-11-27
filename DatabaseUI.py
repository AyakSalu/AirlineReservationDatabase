import tkinter as tk
from tkinter import Label,Tk,Text,Button
from AirlineDatabase import executeCommand
class Table:
     def __init__(self,root):
        self.e = Label(root, text="Flight_Id",width=15, fg='black',borderwidth=2,relief='solid',
                               font=('Arial',8,'bold'))
        
        self.e.grid(row=1, column=3)
        self.e = Label(root,text="Arrival Airport", width=15, fg='black',borderwidth=2,relief='solid',
                               font=('Arial',8,'bold'))
        self.e.grid(row=1, column=4)
        self.e = Label(root,text="Departure Airport", width=15, fg='black',borderwidth=2,relief='solid',
                               font=('Arial',8,'bold'))
        self.e.grid(row=1, column=5)
        self.e = Label(root,text="Airline", width=15, fg='black',borderwidth=2,relief='solid',
                               font=('Arial',8,'bold'))
        self.e.grid(row=1, column=6)
        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                text="Not Available"
                if lst[i][j] is not None:
                    text = lst[i][j]  
                else:
                    text = "Not Available"
                self.e = Label(root,text=text ,width=18, fg='black',borderwidth=1,relief='solid',
                               font=('Arial',8))                
                self.e.grid(row=i+2, column=j+3)   


class Example(tk.Frame):
    def __init__(self, parent):

        tk.Frame.__init__(self, parent)
        self.canvas = tk.Canvas(self, borderwidth=0, background="#ffffff")
        self.frame = tk.Frame(self.canvas, background="#ffffff")
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4,4), window=self.frame, anchor="nw",
                                  tags="self.frame")

        self.frame.bind("<Configure>", self.onFrameConfigure)

        self.populate()

    def populate(self):
        '''Put in some fake data'''
        for row in range(100):
            tk.Label(self.frame, text="%s" % row, width=3, borderwidth="1",
                     relief="solid").grid(row=row, column=0)
            t="this is the second column for row %s" %row
            tk.Label(self.frame, text=t).grid(row=row, column=1)

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

# take the data
command = """SELECT Flight_Id,arrivalAirport.Airport_Name,departureAirport.Airport_Name ,Airline  
            from flights join airports as arrivalAirport on arrivalAirport.Airport_ID = flights.arrival_Airport_ID 
                         join airports as departureAirport on departureAirport.Airport_ID = flights.Departure_Airport_ID
                         join planes on planes.Plane_ID = flights.Plane_ID
                         
            """
lst = executeCommand(command)
lst += executeCommand(command)
# find total number of rows and
# columns in list
total_rows = len(lst)
total_columns = len(lst[0])
def filtrele():
    return 0

window = Tk()

window.title("AirlineManagement")

window.geometry('1600x700+100+100')
personIdTextBoxLabel = Label(window, text = "Biletlerinizi görmek için id'nizi giriniz")
personIdTextBoxLabel.grid(row=0,column=0) 
personIdTextBox = Text(window,height=1,width=20)
personIdTextBox.grid(row=0,column=1) 

Example(window)
searchButton = Button(window,text='Search',command=filtrele)
searchButton.grid(row=0,column=2) 
Table(window)
window.mainloop()


  
# create root window

