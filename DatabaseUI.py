import tkinter as tk
from tkinter import Label,Tk,Text,Button,END,Toplevel
from AirlineDatabase import executeCommand
from datetime import datetime
maxBookingIdCommand = """SELECT max(Booking_ID)  
            from bookings 
            """ 
next_booking_id = executeCommand(maxBookingIdCommand)[0][0]+1
def filtrele():
    text = personIdTextBox.get("1.0",END)
    global lst
    global total_columns
    global total_rows
    global table
    if text is not None:
        command = """SELECT flights.Flight_Id,arrivalAirport.Airport_Name,departureAirport.Airport_Name ,Airline  
            from flights join airports as arrivalAirport on arrivalAirport.Airport_ID = flights.arrival_Airport_ID 
                         join airports as departureAirport on departureAirport.Airport_ID = flights.Departure_Airport_ID
                         join planes on planes.Plane_ID = flights.Plane_ID
                         join bookings on flights.Flight_Id = bookings.Flight_Id
            where bookings.Passenger_ID = """ + text
        lst = executeCommand(command)
        total_rows = len(lst)
        total_columns = len(lst[0])
        table = TableSearched(root,table)
    return 0
def biletSatinAl(biletNumarasi):
    seat_col="C"
    seat_row=0
    seat_type = "Economy"
    def insertToTable():
        passportNumber = personPassportText.get("1.0",END)
        fname = personNameText.get("1.0",END)
        lname = personLastNameText.get("1.0",END)
        phoneNumber = personPhoneNumberText.get("1.0",END)
        email = personEmailText.get("1.0",END)
        amount = personPurchaseAmount.get("1.0",END)
        paymentMethod = personPurchaseType.get("1.0",END)
        time = datetime.now()



        #ilk önce passanger tablosuna sonra  booking tablosuna sonrada payment tablosuna ekleme yapılmalı
        #aynı pasaport numarasına sahip passanger varsa eklenmiyecek
        command = """
        Select Passanger_id from Passangers 
        where Passport_number = %s
        """,passportNumber
        result = executeCommand(command)
        if len(result) != 0 :
            command = """
                INSERT INTO Passengers (Fname, Lname, Passport_Number, Phone_Number, Email) 
                VALUES ('%s', '%s', '%s', '%s', '%s')
            """,fname,lname,passportNumber,phoneNumber,email
        
        command = """
        Select Passenger_id from Passengers 
        where Passport_Number = '%s'
        """,passportNumber
        personid = executeCommand(command)

        command = """
        INSERT INTO Bookings(Flight_ID, Passenger_ID, Booking_Date, Seat_Column, Seat_Row, Booking_Status, Seat_Type) 
            VALUES (%s, %s, '%s', '%s', %s, '%s', '%s');
        """,biletNumarasi,personid,time,seat_col,seat_row,"Confirmed",seat_type
        
        command = """
        Select Booking_id from Bookings 
        where Flight_ID = '%s'
        """,biletNumarasi
        booking_id = executeCommand(command)

        command = """
        INSERT INTO Payments (Booking_ID, Amount, Payment_Date, Payment_Method) VALUES 
        (%s, %s, '%s', '%s');
        """,booking_id,amount,time,paymentMethod
        executeCommand(command)
        
    newWindow = Toplevel(root)
    newWindow.title("Purchase screen")
    personSeatRow = Label(newWindow, text = "Satın Almak İstediğiniz Koltuğun Sırası")
    personSeatRow.grid(sticky='W',row=1,column=1)
    personSeatColumn = Label(newWindow, text = "Satın Almak İstediğiniz Koltuğun Sütunu")
    personSeatColumn.grid(sticky='W',row=2,column=1)
    personPurchaseAmountLabel = Label(newWindow, text = "Bilet Ücreti")
    personPurchaseAmountLabel.grid(sticky='W',row=3,column=1)
    personPurchaseAmount = Text(newWindow,height=1,width=20)
    personPurchaseAmount.grid(sticky='W',row=3,column=2)
    personPurchaseTypeLabel = Label(newWindow, text = "Ödeme Türü")
    personPurchaseTypeLabel.grid(sticky='W',row=4,column=1)
    personPurchaseType = Text(newWindow,height=1,width=20)
    personPurchaseType.grid(sticky='W',row=4,column=2)
    personSeatRowTextBox = Text(newWindow,height=1,width=20)
    personSeatRowTextBox.grid(row=1,column=2) 

    personSeatColumnTextBox = Text(newWindow,height=1,width=20)
    personSeatColumnTextBox.grid(row=2,column=2) 

    personEmailLabel = Label(newWindow, text = "Email")
    personEmailLabel.grid(sticky='W',row=5,column=1)
    personEmailText = Text(newWindow,height=1,width=20)
    personEmailText.grid(sticky='W',row=5,column=2)

    personNameLabel = Label(newWindow, text = "İsim")
    personNameLabel.grid(sticky='W',row=6,column=1)
    personNameText = Text(newWindow,height=1,width=20)
    personNameText.grid(sticky='W',row=6,column=2)

    personLastNameLabel = Label(newWindow, text = "Soyisim")
    personLastNameLabel.grid(sticky='W',row=7,column=1)
    personLastNameText = Text(newWindow,height=1,width=20)
    personLastNameText.grid(sticky='W',row=7,column=2)

    personPassportTypeLabel = Label(newWindow, text = "Passaport ya da TCKN")
    personPassportTypeLabel.grid(sticky='W',row=8,column=1)
    personPassportText = Text(newWindow,height=1,width=20)
    personPassportText.grid(sticky='W',row=8,column=2)

    personPhoneNumberLabel = Label(newWindow, text = "Telefon Numarası")
    personPhoneNumberLabel.grid(sticky='W',row=9,column=1)
    personPhoneNumberText = Text(newWindow,height=1,width=20)
    personPhoneNumberText.grid(sticky='W',row=9,column=2)

    buyButton = Button(newWindow,text='Satın Al',height=4,command=insertToTable,relief='solid') 
    buyButton.grid(row=1,column=3,rowspan=4)
    
    seat_col = personSeatColumnTextBox.get("1.0",END)
    seat_row = personSeatRowTextBox.get("1.0",END)
    seat_type = personPurchaseType.get("1.0",END)

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
class TableInitial:
    Labels = list()
    
    def __init__(self,root):
        def resetTable(self):
            for label in self.Labels:
                label.grid_remove()
        resetTable(self)
        self.e = Label(root, text="Flight_Id",width=18, fg='black',borderwidth=1,relief='solid',
                               font=('Arial',8))
        self.e.configure(background='white')
        self.e.grid(row=2, column=3)
        self.Labels.append(self.e)  
        self.e = Label(root,text="Arrival Airport", width=18, fg='black',borderwidth=1,relief='solid',
                               font=('Arial',8))
        self.e.configure(background='white')
        self.e.grid(row=2, column=4)
        self.Labels.append(self.e)  
        self.e = Label(root,text="Departure Airport", width=18, fg='black',borderwidth=1,relief='solid',
                               font=('Arial',8))
        self.e.configure(background='white')
        self.e.grid(row=2, column=5)
        self.Labels.append(self.e)  
        self.e = Label(root,text="Airline", width=18, fg='black',borderwidth=1,relief='solid',
                               font=('Arial',8))
        self.e.configure(background='white')
        self.e.grid(row=2, column=6)
        self.Labels.append(self.e)  
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
                self.Labels.append(self.e)    
                self.e.configure(background='white')        
                self.e.grid(row=i+3, column=j+3)
            self.e = Button(root,text='Satın Al',command=lambda : biletSatinAl(lst[i][0]),padx=0, pady=0,width=40, height=11,compound="center",
                       image=pixel)
            self.Labels.append(self.e)
            self.e.grid(row=i+3, column=j+4)
            self.e.configure(background='white')
class TableSearched:
    Labels = list()
    def __init__(self,root,table):
        def resetTable(table):
            for label in table.Labels:
                label.grid_remove()
        resetTable(table)
        self.e = Label(root, text="Flight_Id",width=18, fg='black',borderwidth=1,relief='solid',
                               font=('Arial',8))
        
        self.e.grid(sticky='W',row=2, column=3)
        self.e.configure(background='white')
        self.e = Label(root,text="Arrival Airport", width=18, fg='black',borderwidth=1,relief='solid',
                               font=('Arial',8))
        self.e.grid(sticky='W',row=2, column=4)
        self.e.configure(background='white')
        self.Labels.append(self.e)  
        self.e = Label(root,text="Departure Airport", width=18, fg='black',borderwidth=1,relief='solid',
                               font=('Arial',8))
        self.e.grid(sticky='W',row=2, column=5)
        self.e.configure(background='white')
        self.Labels.append(self.e)  
        self.e = Label(root,text="Airline", width=18, fg='black',borderwidth=1,relief='solid',
                               font=('Arial',8))
        self.e.grid(sticky='W',row=2, column=6)
        self.e.configure(background='white')
        self.Labels.append(self.e)  
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
                self.Labels.append(self.e)            
                self.e.grid(sticky='W',row=i+3, column=j+3)
                self.e.configure(background='white')
  
        



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
root.title("AirlineManagement")
root.geometry('1600x700+100+100')
root.configure(background='white')
pixel = tk.PhotoImage(width=1, height=1)
#window = ScrolledFrame(root)
#window.pack(side = 'left',expand=True, fill='both')


personIdTextBoxLabel = Label(root, text = "Biletlerinizi görmek ya da bilet almak için Passaport Numaranızı giriniz")
personIdTextBoxLabel.configure(background='white',foreground='black')
personIdTextBoxLabel.grid(sticky='W',row=1,column=1,columnspan=5) 
personIdTextBox = Text(root,height=1,width=20,borderwidth=1)
personIdTextBox.configure(background='white',foreground='black')
personIdTextBox.grid(row=1,column=6,columnspan=4) 


searchButton = Button(root,text='Search',command=filtrele)
searchButton.configure(background='white',foreground='black')
searchButton.grid(row=1,column=10) 
table = TableInitial(root)


root.mainloop()


  
# create root window

