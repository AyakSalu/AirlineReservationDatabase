import tkinter as tk
from tkinter import Label,Tk,Text,Button,Frame
from AirlineDatabase import executeCommand

def filtrele():
    return 0
def biletSatinAl(biletNumarasi):
    return 0
class ScrolledFrame(tk.Frame):

    def __init__(self, parent, vertical=True, horizontal=False):
        super().__init__(parent)

        # canvas for inner frame
        self._canvas = tk.Canvas(self)
        self._canvas.grid(row=0, column=0, sticky='news') # changed

        # create right scrollbar and connect to canvas Y
        self._vertical_bar = tk.Scrollbar(self, orient='vertical', command=self._canvas.yview)
        if vertical:
            self._vertical_bar.grid(row=0, column=1, sticky='ns')
        self._canvas.configure(yscrollcommand=self._vertical_bar.set)

        # create bottom scrollbar and connect to canvas X
        self._horizontal_bar = tk.Scrollbar(self, orient='horizontal', command=self._canvas.xview)
        if horizontal:
            self._horizontal_bar.grid(row=1, column=0, sticky='we')
        self._canvas.configure(xscrollcommand=self._horizontal_bar.set)

        # inner frame for widgets
        self.inner = tk.Frame(self._canvas, bg='red')
        self._window = self._canvas.create_window((0, 0), window=self.inner, anchor='nw')

        # autoresize inner frame
        self.columnconfigure(0, weight=1) # changed
        self.rowconfigure(0, weight=1) # changed

        # resize when configure changed
        self.inner.bind('<Configure>', self.resize)
        self._canvas.bind('<Configure>', self.frame_width)

    def frame_width(self, event):
        # resize inner frame to canvas size
        canvas_width = event.width
        self._canvas.itemconfig(self._window, width = canvas_width)

    def resize(self, event=None): 
        self._canvas.configure(scrollregion=self._canvas.bbox('all'))
class Table:
     def __init__(self,root):
        self.e = Label(root, text="Flight_Id",width=18, fg='black',borderwidth=1,relief='solid',
                               font=('Arial',8))
        
        self.e.grid(row=2, column=3)
        self.e = Label(root,text="Arrival Airport", width=18, fg='black',borderwidth=1,relief='solid',
                               font=('Arial',8))
        self.e.grid(row=2, column=4)
        self.e = Label(root,text="Departure Airport", width=18, fg='black',borderwidth=1,relief='solid',
                               font=('Arial',8))
        self.e.grid(row=2, column=5)
        self.e = Label(root,text="Airline", width=18, fg='black',borderwidth=1,relief='solid',
                               font=('Arial',8))
        self.e.grid(row=2, column=6)
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
                self.e.grid(row=i+3, column=j+3)
            self.e = Button(root,text='Satın Al',command=biletSatinAl(lst[i][0]),padx=0, pady=0,width=40, height=11,compound="center",
                       image=pixel)
            self.e.grid(row=i+3, column=j+4)   



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

root  = Tk()
root .title("AirlineManagement")
root .geometry('1600x700+100+100')
pixel = tk.PhotoImage(width=1, height=1)
window = ScrolledFrame(root)
window.pack(side = 'left',expand=False, fill='both')


personIdTextBoxLabel = Label(window, text = "Biletlerinizi görmek ya da bilet almak için id'nizi giriniz")
personIdTextBoxLabel.grid(row=1,column=0) 
personIdTextBox = Text(window,height=1,width=20)
personIdTextBox.grid(row=1,column=1) 


searchButton = Button(window,text='Search',command=filtrele)
searchButton.grid(row=1,column=2) 
Table(window)



root.mainloop()


  
# create root window

