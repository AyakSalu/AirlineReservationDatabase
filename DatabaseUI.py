import tkinter as tk
from tkinter import Label, Tk, Text, Button, Toplevel, Checkbutton, ttk, Frame
from AirlineDatabase import executeCommand, app, get_avaliable_flights,update_flight_crew, remove_booked_flight, get_flight_id,check_booking_availability,remove_crew,add_crew,update_crew,remove_flight,add_flight,update_flight,add_flight_crew,remove_flight_crew,add_airport,remove_airport
from datetime import datetime
import tkinter.messagebox


def bilet_iptal_et(flight_id, Passport_ID):
    return remove_booked_flight(flight_id, Passport_ID)

def deleteCrew():
    def apply():
        fname = crewFnameText.get("1.0", 'end-1c')
        lname = crewLnameText.get("1.0", 'end-1c')
        phone_num = crewPhoneNumText.get("1.0", 'end-1c')
        if remove_crew(fname, lname, phone_num) != -1:
            newWindow.destroy()
        else:
            tkinter.messagebox.showinfo("Hata.",  "Girdiğiniz Bilgi Hatalı")
    newWindow = Toplevel(root)
    crewFnameLabel = Label(newWindow, text="İsim ")
    crewFnameLabel.grid(sticky='W', row=0, column=0)
    crewFnameText = Text(newWindow, height=1, width=20)
    crewFnameText.grid(sticky='W', row=0, column=1)
    crewLnameLabel = Label(newWindow, text="Soyisim ")
    crewLnameLabel.grid(sticky='W', row=1, column=0)
    crewLnameText = Text(newWindow, height=1, width=20)
    crewLnameText.grid(sticky='W', row=1, column=1)
    crewPhoneNumLabel = Label(newWindow, text="Telefon Numarası")
    crewPhoneNumLabel.grid(sticky='W', row=2, column=0)
    crewPhoneNumText = Text(newWindow, height=1, width=20)
    crewPhoneNumText.grid(sticky='W', row=2, column=1)
    applyButton =  Button(newWindow, text='Uygula', height=1, command=apply, relief='solid')
    applyButton.grid(row=0, column=2)
    
    return 0
def updateCrew():
    def apply():
        fname = crewFnameText.get("1.0", 'end-1c')
        lname = crewLnameText.get("1.0", 'end-1c')
        phone_num = crewPhoneNumText.get("1.0", 'end-1c')
        new_phone_num = crewNewPhoneNumText.get("1.0", 'end-1c')
        if update_crew(fname, lname, phone_num, new_phone_num) != -1:
            newWindow.destroy()
        else:
            tkinter.messagebox.showinfo("Hata.",  "Girdiğiniz Bilgi Hatalı")
        
    newWindow = Toplevel(root)
    crewFnameLabel = Label(newWindow, text="İsim ")
    crewFnameLabel.grid(sticky='W', row=0, column=0)
    crewFnameText = Text(newWindow, height=1, width=20)
    crewFnameText.grid(sticky='W', row=0, column=1)
    crewLnameLabel = Label(newWindow, text="Soyisim ")
    crewLnameLabel.grid(sticky='W', row=1, column=0)
    crewLnameText = Text(newWindow, height=1, width=20)
    crewLnameText.grid(sticky='W', row=1, column=1)
    crewPhoneNumLabel = Label(newWindow, text="Eski Telefon Numarası")
    crewPhoneNumLabel.grid(sticky='W', row=2, column=0)
    crewPhoneNumText = Text(newWindow, height=1, width=20)
    crewPhoneNumText.grid(sticky='W', row=2, column=1)
    crewNewPhoneNumLabel = Label(newWindow, text="Yeni Telefon Numarası")
    crewNewPhoneNumLabel.grid(sticky='W', row=3, column=0)
    crewNewPhoneNumText = Text(newWindow, height=1, width=20)
    crewNewPhoneNumText.grid(sticky='W', row=3, column=1)
    applyButton =  Button(newWindow, text='Uygula', height=1, command=apply, relief='solid')
    applyButton.grid(row=0, column=2)
    return 0
def addCrew():
    def apply():
        fname = crewFnameText.get("1.0", 'end-1c')
        lname = crewLnameText.get("1.0", 'end-1c')
        phone_num = crewPhoneNumText.get("1.0", 'end-1c')
        crew_role = personPurchaseType.get()
        if add_crew(fname, lname, phone_num,crew_role) != -1:
            newWindow.destroy()
        else:
            tkinter.messagebox.showinfo("Hata.",  "Girdiğiniz Bilgi Hatalı")
        
    newWindow = Toplevel(root)
    crewFnameLabel = Label(newWindow, text="İsim ")
    crewFnameLabel.grid(sticky='W', row=0, column=0)
    crewFnameText = Text(newWindow, height=1, width=20)
    crewFnameText.grid(sticky='W', row=0, column=1)
    crewLnameLabel = Label(newWindow, text="Soyisim ")
    crewLnameLabel.grid(sticky='W', row=1, column=0)
    crewLnameText = Text(newWindow, height=1, width=20)
    crewLnameText.grid(sticky='W', row=1, column=1)
    crewPhoneNumLabel = Label(newWindow, text="Telefon Numarası")
    crewPhoneNumLabel.grid(sticky='W', row=2, column=0)
    crewPhoneNumText = Text(newWindow, height=1, width=20)
    crewPhoneNumText.grid(sticky='W', row=2, column=1)
    crewRoleLabel = Label(newWindow, text="Rol ")
    crewRoleLabel.grid(sticky='W', row=3, column=0)
    personPurchaseType = ttk.Combobox(newWindow, height=3, width=15)
    personPurchaseType['values'] = ('Cook', 'Pilot', 'Co-Pilot', 'Flight Attendant')
    personPurchaseType.grid(sticky='W', row=3, column=1)
    applyButton =  Button(newWindow, text='Uygula', height=1, command=apply, relief='solid')
    applyButton.grid(row=0, column=2)
    return 0

def deleteFlight():
    def apply():
        flight_code = flightCodeText.get("1.0", 'end-1c')

        if remove_flight(flight_code) != -1:
            newWindow.destroy()
        else:
            tkinter.messagebox.showinfo("Hata.",  "Girdiğiniz Bilgi Hatalı")
        
    newWindow = Toplevel(root)
    flightCodeLabel = Label(newWindow, text="Flight Code")
    flightCodeLabel.grid(sticky='W', row=0, column=0)
    flightCodeText = Text(newWindow, height=1, width=20)
    flightCodeText.grid(sticky='W', row=0, column=1)
    applyButton =  Button(newWindow, text='Uygula', height=1, command=apply, relief='solid')
    applyButton.grid(row=0, column=2)
    return 0

def updateFlight():
    def apply():
        flight_code = crewFnameText.get("1.0", 'end-1c')
        new_status = flightType.get()
        new_departure_time = crewPhoneNumText.get("1.0", 'end-1c')
        new_arrival_time = crewRoleText.get("1.0", 'end-1c')
        if update_flight(flight_code, new_status, new_departure_time,new_arrival_time) != -1:
            newWindow.destroy()
        else:
            tkinter.messagebox.showinfo("Hata.",  "Girdiğiniz Bilgi Hatalı")
        
    newWindow = Toplevel(root)
    crewFnameLabel = Label(newWindow, text="Flight Code")
    crewFnameLabel.grid(sticky='W', row=0, column=0)
    crewFnameText = Text(newWindow, height=1, width=20)
    crewFnameText.grid(sticky='W', row=0, column=1)
    crewLnameLabel = Label(newWindow, text="Yeni Durum")
    crewLnameLabel.grid(sticky='W', row=1, column=0)
    flightType = ttk.Combobox(newWindow, height=3, width=24)
    flightType['values'] = ('Cancelled', 'Delayed', 'On-Time')
    flightType.grid(sticky='W', row=1, column=1)
    crewPhoneNumLabel = Label(newWindow, text="Yeni Kalkış Zamanı(YYYY-MM-DD HH:MM:SS)")
    crewPhoneNumLabel.grid(sticky='W', row=2, column=0)
    crewPhoneNumText = Text(newWindow, height=1, width=20)
    crewPhoneNumText.grid(sticky='W', row=2, column=1)
    crewRoleLabel = Label(newWindow, text="Yeni Varış Zamanı(YYYY-MM-DD HH:MM:SS)")
    crewRoleLabel.grid(sticky='W', row=3, column=0)
    crewRoleText = Text(newWindow, height=1, width=20)
    crewRoleText.grid(sticky='W', row=3, column=1)
    applyButton =  Button(newWindow, text='Uygula', height=1, command=apply, relief='solid')
    applyButton.grid(row=0, column=2)
    return 0
def addFlight():
    def apply():
        plane_id = planeIDText.get("1.0", 'end-1c')
        departure_airport_name = departureAirportText.get("1.0", 'end-1c')
        arrival_airport_name = arrivalAirportText.get("1.0", 'end-1c')
        departure_time = crewPhoneNumText.get("1.0", 'end-1c')
        arrival_time = crewRoleText.get("1.0", 'end-1c')
        flight_code = fligtCodeText.get("1.0", 'end-1c')
        brand = brandText.get("1.0", 'end-1c')
        if add_flight(plane_id, departure_airport_name,arrival_airport_name, departure_time,arrival_time,flight_code,brand) != -1:
            newWindow.destroy()
        else:
            tkinter.messagebox.showinfo("Hata.",  "Girdiğiniz Bilgi Hatalı")
        
    newWindow = Toplevel(root)
    crewFnameLabel = Label(newWindow, text="Plane ID")
    crewFnameLabel.grid(sticky='W', row=0, column=0)
    planeIDText = Text(newWindow, height=1, width=20)
    planeIDText.grid(sticky='W', row=0, column=1)
    departureAirportLabel = Label(newWindow, text="Kalkış Havalimanı Adı")
    departureAirportLabel.grid(sticky='W', row=1, column=0)
    departureAirportText = Text(newWindow, height=1, width=20)
    departureAirportText.grid(sticky='W', row=1, column=1)
    arrivalAirportLabel = Label(newWindow, text="Varış Havalimanı Adı")
    arrivalAirportLabel.grid(sticky='W', row=2, column=0)
    arrivalAirportText = Text(newWindow, height=1, width=20)
    arrivalAirportText.grid(sticky='W', row=2, column=1)
    crewPhoneNumLabel = Label(newWindow, text="Kalkış Zamanı(YYYY-MM-DD HH:MM:SS)")
    crewPhoneNumLabel.grid(sticky='W', row=3, column=0)
    crewPhoneNumText = Text(newWindow, height=1, width=20)
    crewPhoneNumText.grid(sticky='W', row=3, column=1)
    crewRoleLabel = Label(newWindow, text="Varış Zamanı(YYYY-MM-DD HH:MM:SS)")
    crewRoleLabel.grid(sticky='W', row=4, column=0)
    crewRoleText = Text(newWindow, height=1, width=20)
    crewRoleText.grid(sticky='W', row=4, column=1)
    fligtCodeLabel = Label(newWindow, text="Flight Code")
    fligtCodeLabel.grid(sticky='W', row=5, column=0)
    fligtCodeText = Text(newWindow, height=1, width=20)
    fligtCodeText.grid(sticky='W', row=5, column=1)
    brandLabel = Label(newWindow, text="Plane Brand")
    brandLabel.grid(sticky='W', row=6, column=0)
    brandText = Text(newWindow, height=1, width=20)
    brandText.grid(sticky='W', row=6, column=1)
    applyButton =  Button(newWindow, text='Uygula', height=1, command=apply, relief='solid')
    applyButton.grid(row=0, column=2)
    return 0
def deleteAirport():
    def apply():
        airport_name = planeIDText.get("1.0", 'end-1c')
        if remove_airport(airport_name) != -1:
            newWindow.destroy()
        else:
            tkinter.messagebox.showinfo("Hata.",  "Girdiğiniz Bilgi Hatalı")
        
    newWindow = Toplevel(root)
    crewFnameLabel = Label(newWindow, text="Havalimanı Adı")
    crewFnameLabel.grid(sticky='W', row=0, column=0)
    planeIDText = Text(newWindow, height=1, width=20)
    planeIDText.grid(sticky='W', row=0, column=1)
    
    applyButton =  Button(newWindow, text='Uygula', height=1, command=apply, relief='solid')
    applyButton.grid(row=0, column=2)
    return 0

def addAirport():
    def apply():
        airport_name = planeIDText.get("1.0", 'end-1c')
        location = departureAirportText.get("1.0", 'end-1c')
        country = arrivalAirportText.get("1.0", 'end-1c')
        time_zone = crewPhoneNumText.get("1.0", 'end-1c')

        if add_airport(airport_name, location,country, time_zone) != -1:
            newWindow.destroy()
        else:
            tkinter.messagebox.showinfo("Hata.",  "Girdiğiniz Bilgi Hatalı")
        
    newWindow = Toplevel(root)
    crewFnameLabel = Label(newWindow, text="Havalimanı Adı")
    crewFnameLabel.grid(sticky='W', row=0, column=0)
    planeIDText = Text(newWindow, height=1, width=20)
    planeIDText.grid(sticky='W', row=0, column=1)
    departureAirportLabel = Label(newWindow, text="Konum")
    departureAirportLabel.grid(sticky='W', row=1, column=0)
    departureAirportText = Text(newWindow, height=1, width=20)
    departureAirportText.grid(sticky='W', row=1, column=1)
    arrivalAirportLabel = Label(newWindow, text="Ülke")
    arrivalAirportLabel.grid(sticky='W', row=2, column=0)
    arrivalAirportText = Text(newWindow, height=1, width=20)
    arrivalAirportText.grid(sticky='W', row=2, column=1)
    crewPhoneNumLabel = Label(newWindow, text="Zaman Dilimi")
    crewPhoneNumLabel.grid(sticky='W', row=3, column=0)
    crewPhoneNumText = Text(newWindow, height=1, width=20)
    crewPhoneNumText.grid(sticky='W', row=3, column=1)
    applyButton =  Button(newWindow, text='Uygula', height=1, command=apply, relief='solid')
    applyButton.grid(row=0, column=2)
    return 0
def deletePlane():
    return 0
def updatePlane():
    return 0
def addPlane():
    return 0
def deleteFlightCrew():
    def apply():
        flight_code = planeIDText.get("1.0", 'end-1c')
        fname = departureAirportText.get("1.0", 'end-1c')
        lname = arrivalAirportText.get("1.0", 'end-1c')
        phone_num = crewPhoneNumText.get("1.0", 'end-1c')

        if remove_flight_crew(flight_code ,fname, lname, phone_num) != -1:
            newWindow.destroy()
        else:
            tkinter.messagebox.showinfo("Hata.",  "Girdiğiniz Bilgi Hatalı")
        
    newWindow = Toplevel(root)
    crewFnameLabel = Label(newWindow, text="Flight Code")
    crewFnameLabel.grid(sticky='W', row=0, column=0)
    planeIDText = Text(newWindow, height=1, width=20)
    planeIDText.grid(sticky='W', row=0, column=1)
    departureAirportLabel = Label(newWindow, text="İsim")
    departureAirportLabel.grid(sticky='W', row=1, column=0)
    departureAirportText = Text(newWindow, height=1, width=20)
    departureAirportText.grid(sticky='W', row=1, column=1)
    arrivalAirportLabel = Label(newWindow, text="Soyisim")
    arrivalAirportLabel.grid(sticky='W', row=2, column=0)
    arrivalAirportText = Text(newWindow, height=1, width=20)
    arrivalAirportText.grid(sticky='W', row=2, column=1)
    crewPhoneNumLabel = Label(newWindow, text="Telefon Numarası")
    crewPhoneNumLabel.grid(sticky='W', row=3, column=0)
    crewPhoneNumText = Text(newWindow, height=1, width=20)
    crewPhoneNumText.grid(sticky='W', row=3, column=1)
    applyButton =  Button(newWindow, text='Uygula', height=1, command=apply, relief='solid')
    applyButton.grid(row=0, column=2)
    return 0
def updateFlightCrew():
    def apply():
        flight_code = planeIDText.get("1.0", 'end-1c')
        fname = departureAirportText.get("1.0", 'end-1c')
        lname = arrivalAirportText.get("1.0", 'end-1c')
        phone_num = crewPhoneNumText.get("1.0", 'end-1c')
        if update_flight_crew(fname, lname, phone_num,flight_code) != -1:
            newWindow.destroy()
        else:
            tkinter.messagebox.showinfo("Hata.",  "Girdiğiniz Bilgi Hatalı")
        
    newWindow = Toplevel(root)
    crewFnameLabel = Label(newWindow, text="New Flight Code")
    crewFnameLabel.grid(sticky='W', row=0, column=0)
    planeIDText = Text(newWindow, height=1, width=20)
    planeIDText.grid(sticky='W', row=0, column=1)
    departureAirportLabel = Label(newWindow, text="İsim")
    departureAirportLabel.grid(sticky='W', row=1, column=0)
    departureAirportText = Text(newWindow, height=1, width=20)
    departureAirportText.grid(sticky='W', row=1, column=1)
    arrivalAirportLabel = Label(newWindow, text="Soyisim")
    arrivalAirportLabel.grid(sticky='W', row=2, column=0)
    arrivalAirportText = Text(newWindow, height=1, width=20)
    arrivalAirportText.grid(sticky='W', row=2, column=1)
    crewPhoneNumLabel = Label(newWindow, text="Telefon Numarası")
    crewPhoneNumLabel.grid(sticky='W', row=3, column=0)
    crewPhoneNumText = Text(newWindow, height=1, width=20)
    crewPhoneNumText.grid(sticky='W', row=3, column=1)
    applyButton =  Button(newWindow, text='Uygula', height=1, command=apply, relief='solid')
    applyButton.grid(row=0, column=2)
    return 0
def addFlightCrew():
    def apply():
        flight_code = planeIDText.get("1.0", 'end-1c')
        fname = departureAirportText.get("1.0", 'end-1c')
        lname = arrivalAirportText.get("1.0", 'end-1c')
        phone_num = crewPhoneNumText.get("1.0", 'end-1c')

        if add_flight_crew(flight_code ,fname, lname, phone_num) != -1:
            newWindow.destroy()
        else:
            tkinter.messagebox.showinfo("Hata.",  "Girdiğiniz Bilgi Hatalı")
        
    newWindow = Toplevel(root)
    crewFnameLabel = Label(newWindow, text="Flight Code")
    crewFnameLabel.grid(sticky='W', row=0, column=0)
    planeIDText = Text(newWindow, height=1, width=20)
    planeIDText.grid(sticky='W', row=0, column=1)
    departureAirportLabel = Label(newWindow, text="İsim")
    departureAirportLabel.grid(sticky='W', row=1, column=0)
    departureAirportText = Text(newWindow, height=1, width=20)
    departureAirportText.grid(sticky='W', row=1, column=1)
    arrivalAirportLabel = Label(newWindow, text="Soyisim")
    arrivalAirportLabel.grid(sticky='W', row=2, column=0)
    arrivalAirportText = Text(newWindow, height=1, width=20)
    arrivalAirportText.grid(sticky='W', row=2, column=1)
    crewPhoneNumLabel = Label(newWindow, text="Telefon Numarası")
    crewPhoneNumLabel.grid(sticky='W', row=3, column=0)
    crewPhoneNumText = Text(newWindow, height=1, width=20)
    crewPhoneNumText.grid(sticky='W', row=3, column=1)
    applyButton =  Button(newWindow, text='Uygula', height=1, command=apply, relief='solid')
    applyButton.grid(row=0, column=2)
    return 0

def create_admin_controls(window):
    
    
    crewLabel = Label(window, text="Crew")
    deleteCrewButton = Button(window, text='Sil', height=1, command=deleteCrew, relief='solid')
    updateCrewButton = Button(window, text='Güncelle', height=1, command=updateCrew, relief='solid')
    addCrewButton = Button(window, text='Ekle', height=1, command=addCrew, relief='solid')
    crewLabel.grid(row=0, column=0)
    deleteCrewButton.grid(row=0, column=1)
    updateCrewButton.grid(row=0, column=2)
    addCrewButton.grid(row=0, column=3)
    crewLabel = Label(window, text="Flight")
    deleteCrewButton = Button(window, text='Sil', height=1, command=deleteFlight, relief='solid')
    updateCrewButton = Button(window, text='Güncelle', height=1, command=updateFlight, relief='solid')
    addCrewButton = Button(window, text='Ekle', height=1, command=addFlight, relief='solid')
    crewLabel.grid(row=1, column=0)
    deleteCrewButton.grid(row=1, column=1)
    updateCrewButton.grid(row=1, column=2)
    addCrewButton.grid(row=1, column=3)
    crewLabel = Label(window, text="Airport")
    deleteCrewButton = Button(window, text='Sil', height=1, command=deleteAirport, relief='solid')
    addCrewButton = Button(window, text='Ekle', height=1, command=addAirport, relief='solid')
    crewLabel.grid(row=2, column=0)
    deleteCrewButton.grid(row=2, column=1)
    addCrewButton.grid(row=2, column=3)
    """
    crewLabel = Label(window, text="Plane")
    deleteCrewButton = Button(window, text='Sil', height=1, command=deletePlane, relief='solid')
    updateCrewButton = Button(window, text='Güncelle', height=1, command=updatePlane, relief='solid')
    addCrewButton = Button(window, text='Ekle', height=1, command=addPlane, relief='solid')
    crewLabel.grid(row=3, column=0)
    deleteCrewButton.grid(row=3, column=1)
    updateCrewButton.grid(row=3, column=2)
    addCrewButton.grid(row=3, column=3)
    """
    crewLabel = Label(window, text="FlightCrew")
    deleteCrewButton = Button(window, text='Sil', height=1, command=deleteFlightCrew, relief='solid')
    updateCrewButton = Button(window, text='Güncelle', height=1, command=updateFlightCrew, relief='solid')
    addCrewButton = Button(window, text='Ekle', height=1, command=addFlightCrew, relief='solid')
    crewLabel.grid(row=4, column=0)
    deleteCrewButton.grid(row=4, column=1)
    updateCrewButton.grid(row=4, column=2)
    addCrewButton.grid(row=4, column=3)





def set_admin_access():

    
    

    global admin_access
    if admin_access == 0:
        admin_access = 1
        
        adminAccessFrame.grid(row=0, column=1000, columnspan=100,rowspan=100,sticky="n")
    else: 
        admin_access = 0
        adminAccessFrame.grid_forget()

    


def filtrele():
    Passport_ID = personIdTextBox.get("1.0", 'end-1c')
    arrivalCity = arrivalCityTextBox.get("1.0", 'end-1c')
    departureCity = departureCityTextBox.get("1.0", 'end-1c')
    global lst
    global total_columns
    global total_rows
    global table
    print(Passport_ID)
    if len(Passport_ID) != 0:
        command = """SELECT Flight_Code,departureAirport.Airport_Name, departureAirport.Location,Departure_Time, arrivalAirport.Airport_Name,arrivalAirport.Location, Arrival_Time , Airline  
            from flights join airports as arrivalAirport on arrivalAirport.Airport_ID = flights.arrival_Airport_ID 
                         join airports as departureAirport on departureAirport.Airport_ID = flights.Departure_Airport_ID
                         join planes on planes.Plane_ID = flights.Plane_ID
                         join bookings on flights.Flight_Id = bookings.Flight_Id
                         join passengers on passengers.Passenger_ID = bookings.Passenger_ID
            where passengers.Passport_Number = '%s'
            """ % Passport_ID
        with app.app_context():
            lst = executeCommand(command)
        print(lst)
        print(command)
        total_rows = len(lst)
        try :
            total_columns = len(lst[0])
        except IndexError:
            total_columns=0
        table = TableSearched(tablo, table, 1)
        tablo.grid(row=10, column=1, columnspan=100, rowspan=100)

        # table = TableSearched(root,table,1)

    elif len(arrivalCity) != 0 and len(departureCity) != 0:
        print(arrivalCity)
        print(departureCity)
        lst = get_avaliable_flights(departureCity, arrivalCity)
        print(lst)
        total_rows = len(lst)
        try :
            total_columns = len(lst[0])
        except IndexError:
            total_columns=0

        table = TableSearched(tablo, table, 0)
        tablo.grid(row=10, column=1, columnspan=100, rowspan=100)

        # table = TableSearched(root,table,0)
        # tablo.grid(row=10,column=1,columnspan=100,rowspan=100)
    else:
        command = """SELECT Flight_Code,departureAirport.Airport_Name, departureAirport.Location,Departure_Time, arrivalAirport.Airport_Name,arrivalAirport.Location, Arrival_Time , Airline
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
        table = TableInitial(tablo)
        tablo.grid(row=10, column=1, columnspan=100, rowspan=100)
        return 0


def biletSatinAl(biletNumarasi):
    def insertToTable():
        seat_col = personSeatColumnTextBox.get("1.0", 'end-1c')
        seat_row = personSeatRowTextBox.get("1.0", 'end-1c')
        seat_type = "Economy"
        passportNumber = personPassportText.get("1.0", 'end-1c')
        fname = personNameText.get("1.0", 'end-1c')
        lname = personLastNameText.get("1.0", 'end-1c')
        phoneNumber = personPhoneNumberText.get("1.0", 'end-1c')
        email = personEmailText.get("1.0", 'end-1c')
        amount = personPurchaseAmount.get("1.0", 'end-1c')
        paymentMethod = personPurchaseType.get()
        if check_booking_availability(biletNumarasi,seat_row,seat_col,passportNumber) and len(seat_col) != 0 and len(seat_row) != 0 and len(seat_type) != 0 and len(passportNumber) != 0 and len(fname) != 0 and len(lname) != 0 and len(phoneNumber) != 0 and len(email) != 0 and len(amount) != 0 and len(paymentMethod) != 0:
            print("%s %s %s %s %s %s %s " % (passportNumber, fname, lname, phoneNumber, email, amount, paymentMethod))
            time = datetime.now()
            # ilk önce passanger tablosuna sonra  booking tablosuna sonrada payment tablosuna ekleme yapılmalı
            # aynı pasaport numarasına sahip passanger varsa eklenmiyecek
            # burdan sonrası çok iyi çalışmıyor
            print(str(passportNumber) + " passport number")
            command = """
            Select Passenger_id from passengers 
            where Passport_number = '%s'
            """ % passportNumber
            with app.app_context():
                result = executeCommand(command)
                print("res1" + str(result))
            if len(result) == 0:
                print("girdik")
                command = """
                    INSERT INTO Passengers (Fname, Lname, Passport_Number, Phone_Number, Email) 
                    VALUES ('%s', '%s', '%s', '%s', '%s');
                """ % (fname, lname, passportNumber, phoneNumber, email)
                with app.app_context():
                    executeCommand(command)
            command = """
            Select Passenger_ID from Passengers 
            where Passport_Number = '%s'
            """ % passportNumber
            with app.app_context():
                personid = executeCommand(command)[0][0]
                print("res2 " + str(personid))
            command = """
            INSERT INTO Bookings(Flight_ID, Passenger_ID, Booking_Date, Seat_Column, Seat_Row, Booking_Status, Seat_Type) 
                VALUES (%s, %s, '%s', '%s', %s, '%s', '%s');
            """ % (biletNumarasi, personid, time, seat_col, seat_row, "Confirmed", seat_type)
            with app.app_context():
                print(command)
                executeCommand(command)
            command = """
            Select Booking_id from Bookings 
            where Flight_ID = %s and Passenger_ID= %s
            """ % (biletNumarasi, personid)
            with app.app_context():
                booking_id = executeCommand(command)[0][0]
                print("res3" + str(booking_id))
            command = """
            INSERT INTO Payments (Booking_ID, Amount, Payment_Date, Payment_Method) 
            VALUES (%s, %s, '%s', '%s');
            """ % (booking_id, amount, time, paymentMethod)
            with app.app_context():
                executeCommand(command)
            newWindow.destroy()
        else:
            tkinter.messagebox.showinfo("Hata.",  "Seçtiğiniz koltuk uygun değil ya da Girdiğiniz bilgiler hatalı")
    newWindow = Toplevel(root)
    newWindow.title("Purchase screen")
    personSeatRow = Label(newWindow, text="Satın Almak İstediğiniz Koltuğun Sırası")
    personSeatRow.grid(sticky='W', row=1, column=1)
    personSeatColumn = Label(newWindow, text="Satın Almak İstediğiniz Koltuğun Sütunu")
    personSeatColumn.grid(sticky='W', row=2, column=1)
    personPurchaseAmountLabel = Label(newWindow, text="Bilet Ücreti")
    personPurchaseAmountLabel.grid(sticky='W', row=3, column=1)
    personPurchaseAmount = Text(newWindow, height=1, width=20)
    personPurchaseAmount.grid(sticky='W', row=3, column=2)
    personPurchaseTypeLabel = Label(newWindow, text="Ödeme Türü ('Credit Card', 'PayPal' or 'Bank Transfer')")
    personPurchaseTypeLabel.grid(sticky='W', row=4, column=1)
    personPurchaseType = ttk.Combobox(newWindow, height=3, width=15)
    personPurchaseType['values'] = ('Credit Card', 'PayPal', 'Bank Transfer')
    personPurchaseType.grid(sticky='W', row=4, column=2, columnspan=2)
    personSeatRowTextBox = Text(newWindow, height=1, width=20)
    personSeatRowTextBox.grid(row=1, column=2)

    personSeatColumnTextBox = Text(newWindow, height=1, width=20)
    personSeatColumnTextBox.grid(row=2, column=2)

    personEmailLabel = Label(newWindow, text="Email")
    personEmailLabel.grid(sticky='W', row=5, column=1)
    personEmailText = Text(newWindow, height=1, width=20)
    personEmailText.grid(sticky='W', row=5, column=2)

    personNameLabel = Label(newWindow, text="İsim")
    personNameLabel.grid(sticky='W', row=6, column=1)
    personNameText = Text(newWindow, height=1, width=20)
    personNameText.grid(sticky='W', row=6, column=2)

    personLastNameLabel = Label(newWindow, text="Soyisim")
    personLastNameLabel.grid(sticky='W', row=7, column=1)
    personLastNameText = Text(newWindow, height=1, width=20)
    personLastNameText.grid(sticky='W', row=7, column=2)

    personPassportTypeLabel = Label(newWindow, text="Passaport")
    personPassportTypeLabel.grid(sticky='W', row=8, column=1)
    personPassportText = Text(newWindow, height=1, width=20)
    personPassportText.grid(sticky='W', row=8, column=2)

    personPhoneNumberLabel = Label(newWindow, text="Telefon Numarası")
    personPhoneNumberLabel.grid(sticky='W', row=9, column=1)
    personPhoneNumberText = Text(newWindow, height=1, width=20)
    personPhoneNumberText.grid(sticky='W', row=9, column=2)

    buyButton = Button(newWindow, text='Satın Al', height=4, command=insertToTable, relief='solid')
    buyButton.grid(row=1, column=4, rowspan=4)

    return 0


class TableInitial:
    Labels = list()

    def __init__(self, root):
        def resetTable(self):
            for label in self.Labels:
                label.grid_remove()

        resetTable(self)
        self.e = Label(root, text="Flight_Code", width=18, fg='black', borderwidth=1, relief='solid',
                       font=('Arial', 8))
        self.e.configure(background='white')
        self.e.grid(row=5, column=3)
        self.Labels.append(self.e)
        self.e = Label(root, text="Departure Airport", width=18, fg='black', borderwidth=1, relief='solid',
                       font=('Arial', 8))
        self.e.configure(background='white')
        self.e.grid(row=5, column=4)
        self.Labels.append(self.e)
        self.e = Label(root, text="Departure Location", width=18, fg='black', borderwidth=1, relief='solid',
                       font=('Arial', 8))
        self.e.configure(background='white')
        self.e.grid(row=5, column=5)
        self.Labels.append(self.e)
        self.e = Label(root, text="Departure Time", width=18, fg='black', borderwidth=1, relief='solid',
                       font=('Arial', 8))
        self.e.configure(background='white')
        self.e.grid(row=5, column=6)
        self.Labels.append(self.e)
        self.e = Label(root, text="Arrival Airport", width=18, fg='black', borderwidth=1, relief='solid',
                       font=('Arial', 8))
        self.e.grid(sticky='W', row=5, column=7)
        self.e.configure(background='white')
        self.Labels.append(self.e)
        self.e = Label(root, text="Arrival Location", width=18, fg='black', borderwidth=1, relief='solid',
                       font=('Arial', 8))
        self.e.grid(sticky='W', row=5, column=8)
        self.e.configure(background='white')
        self.Labels.append(self.e)
        self.e = Label(root, text="Arrival Time", width=18, fg='black', borderwidth=1, relief='solid',
                       font=('Arial', 8))
        self.e.grid(sticky='W', row=5, column=9)
        self.e.configure(background='white')
        self.Labels.append(self.e)
        self.e = Label(root, text="Airline", width=18, fg='black', borderwidth=1, relief='solid',
                       font=('Arial', 8))
        self.e.grid(sticky='W', row=5, column=10)
        self.e.configure(background='white')
        self.Labels.append(self.e)

        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                text = "Not Available"
                if lst[i][j] is not None:
                    text = lst[i][j]
                else:
                    text = "Not Available"
                self.e = Label(root, text=text, width=18, fg='black', borderwidth=1, relief='solid',
                               font=('Arial', 8))
                self.Labels.append(self.e)
                self.e.configure(background='white')
                self.e.grid(row=i + 6, column=j + 3)
            self.e = Button(root, text='Satın Al', command= lambda a = i: biletSatinAl(get_flight_id(lst[a][0])), padx=0, pady=0, width=40,
                            height=11, compound="center",
                            image=pixel)
            self.Labels.append(self.e)
            self.e.grid(row=i + 6, column=j + 4)
            self.e.configure(background='white')
class TableSearched:
    Labels = list()

    def __init__(self, root, table, flag):
        def resetTable(table):
            for label in table.Labels:
                label.grid_remove()

        resetTable(table)
        self.e = Label(root, text="Flight_Code", width=18, fg='black', borderwidth=1, relief='solid',
                       font=('Arial', 8))
        self.e.configure(background='white')
        self.e.grid(row=5, column=3)
        self.Labels.append(self.e)
        self.e = Label(root, text="Departure Airport", width=18, fg='black', borderwidth=1, relief='solid',
                       font=('Arial', 8))
        self.e.configure(background='white')
        self.e.grid(row=5, column=4)
        self.Labels.append(self.e)
        self.e = Label(root, text="Departure Location", width=18, fg='black', borderwidth=1, relief='solid',
                       font=('Arial', 8))
        self.e.configure(background='white')
        self.e.grid(row=5, column=5)
        self.Labels.append(self.e)
        self.e = Label(root, text="Departure Time", width=18, fg='black', borderwidth=1, relief='solid',
                       font=('Arial', 8))
        self.e.configure(background='white')
        self.e.grid(row=5, column=6)
        self.Labels.append(self.e)
        self.e = Label(root, text="Arrival Airport", width=18, fg='black', borderwidth=1, relief='solid',
                       font=('Arial', 8))
        self.e.grid(sticky='W', row=5, column=7)
        self.e.configure(background='white')
        self.Labels.append(self.e)
        self.e = Label(root, text="Arrival Location", width=18, fg='black', borderwidth=1, relief='solid',
                       font=('Arial', 8))
        self.e.grid(sticky='W', row=5, column=8)
        self.e.configure(background='white')
        self.Labels.append(self.e)
        self.e = Label(root, text="Arrival Time", width=18, fg='black', borderwidth=1, relief='solid',
                       font=('Arial', 8))
        self.e.grid(sticky='W', row=5, column=9)
        self.e.configure(background='white')
        self.Labels.append(self.e)
        self.e = Label(root, text="Airline", width=18, fg='black', borderwidth=1, relief='solid',
                       font=('Arial', 8))
        self.e.grid(sticky='W', row=5, column=10)
        self.e.configure(background='white')
        self.Labels.append(self.e)
        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                text = "Not Available"
                if lst[i][j] is not None:
                    text = lst[i][j]
                else:
                    text = "Not Available"
                self.e = Label(root, text=text, width=18, fg='black', borderwidth=1, relief='solid',
                               font=('Arial', 8))
                self.Labels.append(self.e)
                self.e.grid(sticky='W', row=i + 6, column=j + 3)
                self.e.configure(background='white')
            if flag == 1:
                self.e = Button(root, text='İptal Et',
                                command=lambda a = i: bilet_iptal_et(get_flight_id(lst[a][0]), personIdTextBox.get("1.0", 'end-1c')), padx=0,
                                pady=0, width=40, height=11, compound="center",
                                image=pixel)
                self.Labels.append(self.e)
                self.e.grid(row=i + 6, column=j + 4)
                self.e.configure(background='white')


# take the data

command = """ SELECT Flight_Code,a1.Airport_Name, a1.Location,Departure_Time, a2.Airport_Name,a2.Location, Arrival_Time,Airline
    FROM flights 
    natural join planes
    inner join airports as a1 on a1.Airport_ID = flights.Departure_Airport_ID
    inner join airports as a2 on a2.Airport_ID = flights.Arrival_Airport_ID
    Where capacity > 0
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
# window = ScrolledFrame(root)
# window.pack(side = 'left',expand=True, fill='both')


personIdTextBoxLabel = Label(root, text="Biletlerinizi görmek için Passaport Numaranızı giriniz")
personIdTextBoxLabel.configure(background='white', foreground='black')
personIdTextBoxLabel.grid(sticky='W', row=1, column=1, columnspan=6)
personIdTextBox = Text(root, height=1, width=20, borderwidth=1)
personIdTextBox.configure(background='white', foreground='black')
personIdTextBox.grid(row=1, column=7, columnspan=4)

arrivalCityLabel = Label(root, text="Varış Ülkesi")
arrivalCityLabel.configure(background='white', foreground='black')
arrivalCityLabel.grid(sticky='W', row=2, column=0, columnspan=5)
arrivalCityTextBox = Text(root, height=1, width=20, borderwidth=1)
arrivalCityTextBox.configure(background='white', foreground='black')
arrivalCityTextBox.grid(row=2, column=3, columnspan=3)

departureCityLabel = Label(root, text="Kalkış Ülkesi")
departureCityLabel.configure(background='white', foreground='black')
departureCityLabel.grid(sticky='W', row=2, column=7, columnspan=3)
departureCityTextBox = Text(root, height=1, width=15, borderwidth=1)
departureCityTextBox.configure(background='white', foreground='black')
departureCityTextBox.grid(sticky='E', row=2, column=10)

searchButton = Button(root, text='Search', command=filtrele)
searchButton.configure(background='white', foreground='black', )
searchButton.grid(row=1, column=11)

adminCheckBox = Checkbutton(root, text='Admin Access', command=set_admin_access)
adminCheckBox.configure(background='white', foreground='black')
adminCheckBox.grid(row=1, column=12)
tablo = Frame(root)
table = TableInitial(tablo)
tablo.grid(row=10, column=1, columnspan=100, rowspan=100)

adminAccessFrame = Frame(root)
create_admin_controls(adminAccessFrame)


root.mainloop()

# create root window