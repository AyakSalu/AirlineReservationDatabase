import tkinter as tk
from tkinter import Label,Tk,Text,Button,Toplevel,Checkbutton
from AirlineDatabase import executeCommand, app,get_avaliable_flights
from datetime import datetime
def bilet_iptal_et(flight_id,Passport_ID):
    return 0
def set_admin_access():
    global admin_access
    admin_access = 1 if admin_access == 0 else 0
def filtrele():
    Passport_ID = personIdTextBox.get("1.0",'end-1c')
    arrivalCity = arrivalCityTextBox.get("1.0",'end-1c')
    departureCity = departureCityTextBox.get("1.0",'end-1c')
    global lst
    global total_columns
    global total_rows
    global table
    print(Passport_ID)
    if len(Passport_ID) != 0:
        command = """SELECT Flight_Code,departureAirport.Airport_Name, departureAirport.Country,Departure_Time, arrivalAirport.Airport_Name,arrivalAirport.Country, Arrival_Time , Airline  
            from flights join airports as arrivalAirport on arrivalAirport.Airport_ID = flights.arrival_Airport_ID 
                         join airports as departureAirport on departureAirport.Airport_ID = flights.Departure_Airport_ID
                         join planes on planes.Plane_ID = flights.Plane_ID
                         join bookings on flights.Flight_Id = bookings.Flight_Id
                         join passengers on passengers.Passenger_ID = bookings.Passenger_ID
            where passengers.Passport_Number = '%s'
            """%Passport_ID
        with app.app_context():
            lst = executeCommand(command)
        print(lst)
        print(command)
        total_rows = len(lst)
        total_columns = len(lst[0])
        table = TableSearched(root,table,1)
        
    elif len(arrivalCity) and len(departureCity):
        print(arrivalCity)
        print(departureCity)
        lst = get_avaliable_flights(departureCity,arrivalCity)
        print(lst)
        total_rows = len(lst)
        total_columns = len(lst[0])
        table = TableSearched(root,table,0)
    return 0
def biletSatinAl(biletNumarasi):
    
    def insertToTable():
        seat_col=personSeatColumnTextBox.get("1.0",'end-1c')
        seat_row=personSeatRowTextBox.get("1.0",'end-1c')
        seat_type = "Economy"
        passportNumber = personPassportText.get("1.0",'end-1c')
        fname = personNameText.get("1.0",'end-1c')
        lname = personLastNameText.get("1.0",'end-1c')
        phoneNumber = personPhoneNumberText.get("1.0",'end-1c')
        email = personEmailText.get("1.0",'end-1c')
        amount = personPurchaseAmount.get("1.0",'end-1c')
        paymentMethod = personPurchaseType.get("1.0",'end-1c')
        print("%s %s %s %s %s %s %s "%(passportNumber,fname,lname,phoneNumber,email,amount,paymentMethod))
        time = datetime.now()


        #ilk önce passanger tablosuna sonra  booking tablosuna sonrada payment tablosuna ekleme yapılmalı
        #aynı pasaport numarasına sahip passanger varsa eklenmiyecek
        #burdan sonrası çok iyi çalışmıyor
        print(str(passportNumber) + " passport number")
        command = """
        Select Passenger_id from passengers 
        where Passport_number = '%s'
        """ % passportNumber
        with app.app_context():
            result = executeCommand(command)
            print("res1" + str(result))
        if len(result) == 0 :
            print("girdik")
            command = """
                INSERT INTO Passengers (Fname, Lname, Passport_Number, Phone_Number, Email) 
                VALUES ('%s', '%s', '%s', '%s', '%s');
            """%(fname,lname,passportNumber,phoneNumber,email)
            with app.app_context():
                executeCommand(command)
                
        
        command = """
        Select Passenger_ID from Passengers 
        where Passport_Number = '%s'
        """%passportNumber
        with app.app_context():
            personid = executeCommand(command)[0][0]
            print("res2 " + str(personid))

        command = """
        INSERT INTO Bookings(Flight_ID, Passenger_ID, Booking_Date, Seat_Column, Seat_Row, Booking_Status, Seat_Type) 
            VALUES (%s, %s, '%s', '%s', %s, '%s', '%s');
        """%(biletNumarasi,personid,time,seat_col,seat_row,"Confirmed",seat_type)
        with app.app_context():
            print(command)
            executeCommand(command)

        command = """
        Select Booking_id from Bookings 
        where Flight_ID = %s and Passenger_ID= %s
        """%(biletNumarasi,personid)

        with app.app_context():
            booking_id = executeCommand(command)[0][0]
            print("res3" + str(booking_id))

        command = """
        INSERT INTO Payments (Booking_ID, Amount, Payment_Date, Payment_Method) 
        VALUES (%s, %s, '%s', '%s');
        """%(booking_id,amount,time,paymentMethod)
        with app.app_context():
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
    personPurchaseTypeLabel = Label(newWindow, text = "Ödeme Türü ('Credit Card', 'PayPal' or 'Bank Transfer')")
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

    personPassportTypeLabel = Label(newWindow, text = "Passaport")
    personPassportTypeLabel.grid(sticky='W',row=8,column=1)
    personPassportText = Text(newWindow,height=1,width=20)
    personPassportText.grid(sticky='W',row=8,column=2)

    personPhoneNumberLabel = Label(newWindow, text = "Telefon Numarası")
    personPhoneNumberLabel.grid(sticky='W',row=9,column=1)
    personPhoneNumberText = Text(newWindow,height=1,width=20)
    personPhoneNumberText.grid(sticky='W',row=9,column=2)

    buyButton = Button(newWindow,text='Satın Al',height=4,command=insertToTable,relief='solid') 
    buyButton.grid(row=1,column=3,rowspan=4)
    

    return 0
class TableInitial:
    Labels = list()
    
    def __init__(self,root):
        def resetTable(self):
            for label in self.Labels:
                label.grid_remove()
        resetTable(self)
        self.e = Label(root, text="Flight_Code",width=18, fg='black',borderwidth=1,relief='solid',
                               font=('Arial',8))
        self.e.configure(background='white')
        self.e.grid(row=5, column=3)
        self.Labels.append(self.e)  
        self.e = Label(root,text="Departure Airport", width=18, fg='black',borderwidth=1,relief='solid',
                               font=('Arial',8))
        self.e.configure(background='white')
        self.e.grid(row=5, column=4)
        self.Labels.append(self.e)  
        self.e = Label(root,text="Departure City", width=18, fg='black',borderwidth=1,relief='solid',
                               font=('Arial',8))
        self.e.configure(background='white')
        self.e.grid(row=5, column=5)
        self.Labels.append(self.e)  
        self.e = Label(root,text="Departure Time", width=18, fg='black',borderwidth=1,relief='solid',
                               font=('Arial',8))
        self.e.configure(background='white')
        self.e.grid(row=5, column=6)
        self.Labels.append(self.e)  
        self.e = Label(root,text="Arrival Airport", width=18, fg='black',borderwidth=1,relief='solid',
                               font=('Arial',8))
        self.e.grid(sticky='W',row=5, column=7)
        self.e.configure(background='white')
        self.Labels.append(self.e) 
        self.e = Label(root,text="Arrival City", width=18, fg='black',borderwidth=1,relief='solid',
                               font=('Arial',8))
        self.e.grid(sticky='W',row=5, column=8)
        self.e.configure(background='white')
        self.Labels.append(self.e)
        self.e = Label(root,text="Arrival Time", width=18, fg='black',borderwidth=1,relief='solid',
                               font=('Arial',8))
        self.e.grid(sticky='W',row=5, column=9)
        self.e.configure(background='white')
        self.Labels.append(self.e)
        self.e = Label(root,text="Airline", width=18, fg='black',borderwidth=1,relief='solid',
                               font=('Arial',8))
        self.e.grid(sticky='W',row=5, column=10)
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
                self.e.configure(background='white')        
                self.e.grid(row=i+6, column=j+3)
            self.e = Button(root,text='Satın Al',command=lambda : biletSatinAl(lst[i][0]),padx=0, pady=0,width=40, height=11,compound="center",
                       image=pixel)
            self.Labels.append(self.e)
            self.e.grid(row=i+6, column=j+4)
            self.e.configure(background='white')
class TableSearched:
    Labels = list()
    def __init__(self,root,table,flag):
        def resetTable(table):
            for label in table.Labels:
                label.grid_remove()
        resetTable(table)
        self.e = Label(root, text="Flight_Code",width=18, fg='black',borderwidth=1,relief='solid',
                               font=('Arial',8))
        self.e.configure(background='white')
        self.e.grid(row=5, column=3)
        self.Labels.append(self.e)  
        self.e = Label(root,text="Departure Airport", width=18, fg='black',borderwidth=1,relief='solid',
                               font=('Arial',8))
        self.e.configure(background='white')
        self.e.grid(row=5, column=4)
        self.Labels.append(self.e)  
        self.e = Label(root,text="Departure City", width=18, fg='black',borderwidth=1,relief='solid',
                               font=('Arial',8))
        self.e.configure(background='white')
        self.e.grid(row=5, column=5)
        self.Labels.append(self.e)  
        self.e = Label(root,text="Departure Time", width=18, fg='black',borderwidth=1,relief='solid',
                               font=('Arial',8))
        self.e.configure(background='white')
        self.e.grid(row=5, column=6)
        self.Labels.append(self.e)  
        self.e = Label(root,text="Arrival Airport", width=18, fg='black',borderwidth=1,relief='solid',
                               font=('Arial',8))
        self.e.grid(sticky='W',row=5, column=7)
        self.e.configure(background='white')
        self.Labels.append(self.e) 
        self.e = Label(root,text="Arrival City", width=18, fg='black',borderwidth=1,relief='solid',
                               font=('Arial',8))
        self.e.grid(sticky='W',row=5, column=8)
        self.e.configure(background='white')
        self.Labels.append(self.e)
        self.e = Label(root,text="Arrival Time", width=18, fg='black',borderwidth=1,relief='solid',
                               font=('Arial',8))
        self.e.grid(sticky='W',row=5, column=9)
        self.e.configure(background='white')
        self.Labels.append(self.e)
        self.e = Label(root,text="Airline", width=18, fg='black',borderwidth=1,relief='solid',
                               font=('Arial',8))
        self.e.grid(sticky='W',row=5, column=10)
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
                self.e.grid(sticky='W',row=i+6, column=j+3)
                self.e.configure(background='white')
            if flag == 1: 
                self.e = Button(root,text='İptal Et',command=lambda : bilet_iptal_et(lst[i][0],personIdTextBox.get("1.0",'end-1c')),padx=0, pady=0,width=40, height=11,compound="center",
                           image=pixel)
                self.Labels.append(self.e)
                self.e.grid(row=i+6, column=j+4)
                self.e.configure(background='white')
  

# take the data

command = """SELECT Flight_Code,departureAirport.Airport_Name, departureAirport.Country,Departure_Time, arrivalAirport.Airport_Name,arrivalAirport.Country, Arrival_Time , Airline
            from flights join airports as arrivalAirport on arrivalAirport.Airport_ID = flights.arrival_Airport_ID 
                         join airports as departureAirport on departureAirport.Airport_ID = flights.Departure_Airport_ID
                         join planes on planes.Plane_ID = flights.Plane_ID
                         
            """

with app.app_context():
    lst = executeCommand(command)
# find total number of rows and
# columns in list
total_rows = len(lst)
total_columns = len(lst[0])
admin_access = 0
root = Tk()
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
personIdTextBox.grid(row=1,column=5,columnspan=4) 

arrivalCityLabel = Label(root, text = "Varmak istediğiniz şehri giriniz")
arrivalCityLabel.configure(background='white',foreground='black')
arrivalCityLabel.grid(sticky='W',row=2,column=0,columnspan=5) 
arrivalCityTextBox = Text(root,height=1,width=20,borderwidth=1)
arrivalCityTextBox.configure(background='white',foreground='black')
arrivalCityTextBox.grid(row=2,column=3,columnspan=4) 

departureCityLabel = Label(root, text = "Kalkışa geçmek istediğiniz şehri giriniz")
departureCityLabel.configure(background='white',foreground='black')
departureCityLabel.grid(sticky='W',row=2,column=5,columnspan=3) 
departureCityTextBox = Text(root,height=1,width=15,borderwidth=1)
departureCityTextBox.configure(background='white',foreground='black')
departureCityTextBox.grid(sticky='E',row=2,column=7) 

searchButton = Button(root,text='Search',command=filtrele)
searchButton.configure(background='white',foreground='black')
searchButton.grid(row=1,column=7) 

adminCheckBox = Checkbutton(root,text='Admin Access',command=set_admin_access)
adminCheckBox.configure(background='white',foreground='black')
adminCheckBox.grid(row=1,column=8) 
table = TableInitial(root)


root.mainloop()


  
# create root window

