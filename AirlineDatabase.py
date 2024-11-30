from flask_mysqldb import MySQL
from flask import Flask
from Sifreler import sifre
from datetime import datetime

def executeCommand(command):
    with app.app_context():
        cursor = mysql.connection.cursor()
        cursor.execute(command)
        data = cursor.fetchall()
        cursor.close()
        mysql.connection.commit()
        return data


def insert_passengers(Fname, Lname, Passport_Number, Phone_Number, Email):
    command = """
    Select Passenger_id from passengers 
    where Passport_number = '%s'
    """ % Passport_Number
    with app.app_context():
        result = executeCommand(command)
        print("new passanger" + str(result))
    if len(result) == 0:
        command = """
            INSERT INTO Passengers (Fname, Lname, Passport_Number, Phone_Number, Email) 
            VALUES ('%s', '%s', '%s', '%s', '%s');
        """ % (Fname, Lname, Passport_Number, Phone_Number, Email)
        with app.app_context():
            executeCommand(command)
            print("inserted new passenger")


def get_avaliable_flights(departure_country, arrival_country):
    command = (""" SELECT Flight_Code,a1.Airport_Name, a1.Location,Departure_Time, a2.Airport_Name,a2.Location, Arrival_Time,Airline
    FROM flights 
    natural join planes
    inner join airports as a1 on a1.Airport_ID = flights.Departure_Airport_ID
    inner join airports as a2 on a2.Airport_ID = flights.Arrival_Airport_ID
    Where a1.Country = '%s' AND a2.Country ='%s' AND capacity > 0"""
               % (departure_country, arrival_country))
    return executeCommand(command)


def check_booking_availability(flight_id, seat_row, seat_col, passenger_id):
    # seat biri tarafından alınmış mı? ya da vatandaş zaten bu uçuştan bilet almış mı?
    command = (""" Select * from bookings
    Where Flight_ID = '%s' AND ((Seat_Row = '%s' AND Seat_Column = '%s') OR Passenger_ID = '%s') """ % (
        flight_id, seat_row, seat_col, passenger_id))
    booking_available = len(executeCommand(command)) == 0

    # ikisi de boş kümeyse TRUE dönecek
    return booking_available


def remove_booked_flight(flight_id, passport_num):
    command = ("""DELETE FROM bookings
    WHERE bookings.Flight_ID = '%s'
    AND bookings.Passenger_ID IN (Select Distinct(Passenger_ID) from passengers WHERE passengers.Passport_Number = '%s')"""
               % (flight_id, passport_num))
    return executeCommand(command)


def get_next_bookid():
    maxBookingIdCommand = """SELECT max(Booking_ID)  
                from bookings 
                """
    return executeCommand(maxBookingIdCommand)[0][0] + 1


# bulamadıysa -1 dönüyo
def get_crew_id(fname, lname, phone_num):
    command = (""" SELECT c.Crew_ID FROM crew as c WHERE c.Fname = '%s' AND c.Lname = '%s' AND c.Phone_Number = '%s' """
               % (fname, lname, phone_num))
    result = executeCommand(command)
    return result[0][0] if len(result) > 0 else -1


def remove_crew(fname, lname, phone_num):
    crew_id = get_crew_id(fname, lname, phone_num)
    if crew_id != -1:
        command = """DELETE FROM crew WHERE crew.Crew_ID = '%s' """ % crew_id
        return executeCommand(command)
    print("olmayan birini silemezsin")
    return -1


# ekleyemediyse -1 dönüyor
def add_crew(fname, lname, phone_num, crew_role):
    if get_crew_id(fname, lname, phone_num) != -1:
        command = ("""INSERT INTO crew (Fname, Lname, Crew_Role, Phone_Number) VALUES ('%s', '%s', '%s', '%s') """ %
                   (fname, lname, crew_role, phone_num))
        return executeCommand(command)
    print("zaten öyle biri var")
    return -1


def update_crew(fname, lname, phone_num, new_phone_num):
    crew_id = get_crew_id(fname, lname, phone_num)
    if crew_id != -1:
        command = """UPDATE crew as c SET c.Phone_Number = '%s' WHERE c.Crew_ID = '%s' """ % (new_phone_num, crew_id)
        return executeCommand(command)
    print("olmayan birini güncelleyemezsin")
    return -1


def get_flight_id(flight_code):
    command = (""" SELECT flights.Flight_ID from flights where flights.Flight_Code = '%s' """ % (flight_code))
    return executeCommand(command)[0][0]  # id'yi int olarak döner


def remove_flight(flight_code):
    flight_id = get_flight_id(flight_code)
    if flight_id != -1:
        command = """DELETE FROM flight as f WHERE f.Flight_ID = '%s' """ % flight_id
        return executeCommand(command)
    print("olmayan bir flight'ı silemezsin")
    return -1


def get_airport(airport_name):
    command = (""" SELECT a.Airport_ID from airports as a where a.Airport_Name = '%s' """ % airport_name)
    result = executeCommand(command)
    return result[0][0] if len(result) > 0 else -1

def compare_dates(departure_date, arrival_date):

    # Parse the strings into datetime objects
    datetime1 = datetime.strptime(departure_date, '%Y-%m-%d %H:%M:%S')
    datetime2 = datetime.strptime(arrival_date, '%Y-%m-%d %H:%M:%S')

    # Extract the time portion
    time1 = datetime1.time()
    time2 = datetime2.time()

    #arrival_time > deprature olursa true döner
    return time2 > time1


def add_flight(plane_id, departure_airport_name, arrival_airport_name, departure_time, arrival_time, flight_code,
               brand=None):
    departure_airport = get_airport(departure_airport_name)
    arrival_airport = get_airport(arrival_airport_name)

    if(get_flight_id(flight_code) == -1):
        print("öyle bir flight zaten var")
        return -1
    if (departure_airport == -1 or arrival_airport == -1):
        print("öyle bir airportlar yok ya da yanlış yazıldı")
        return -1
    if(not compare_dates(departure_time,arrival_time)):
        print("varma zamanı, kalkma zamanından önce olamaz")
        return -1

    if brand != None:
        command = """ INSERT INTO airlinereservationsystem.flights (Plane_ID, Departure_Airport_ID, Arrival_Airport_ID, Departure_Time,
Arrival_Time, Fligth_Status, Airline_Brand, Flight_Code)
VALUES ('%s', '%s', '%s', '%s', '%s', 'On-Time', '%s', '%s')
    """ % (plane_id, departure_airport, arrival_airport, departure_time, arrival_time, brand, flight_code)

    else:
        command = """ INSERT INTO airlinereservationsystem.flights (Plane_ID, Departure_Airport_ID, Arrival_Airport_ID, Departure_Time,
                                                  Arrival_Time, Fligth_Status, Airline_Brand, Flight_Code)
VALUES ('%s', '%s', '%s', '%s', '%s', 'On-Time', NULL, '%s')
    """ % (plane_id, departure_airport, arrival_airport, departure_time, arrival_time, flight_code)

    return executeCommand(command)

#status cancelled ise zaman girmesine gerek yok ama status kesinlikle "Cancelled" olmalı yoksa patlar
def update_flight(flight_code, new_status, new_departure_time=None, new_arrival_time=None):
    flight_id = get_flight_id(flight_code)
    if flight_id == -1:
        print("olmayan bir flight'ı değiştiremezsin")
        return -1

    if new_status == "Delayed":
        command = """UPDATE flights as f
    SET f.Departure_Time = '%s',
        f.Arrival_Time   = '%s',
        f.Fligth_Status  = '%s'
    WHERE f.Flight_ID = '%s' """ % (new_departure_time, new_arrival_time, new_status, flight_id)
    else:
        command = """UPDATE flights as f
            SET f.Fligth_Status  = '%s'
            WHERE f.Flight_ID = '%s' """ % (new_status, flight_id)
    return executeCommand(command)

def add_flight_crew(flight_code ,fname, lname, phone_num):
    flight_id = get_flight_id(flight_code)
    crew_id = get_crew_id(fname, lname, phone_num)

    if (flight_id != -1 and crew_id != -1):
        print("öyle bir çalışan öyle bir flightta zaten çalışıyor.")
        return -1
    command = """INSERT INTO flight_crew (Flight_ID, Crew_ID) VALUES ('%s', '%s')""" % (flight_id, crew_id)
    return executeCommand(command)

def remove_flight_crew(flight_code ,fname, lname,phone_num):
    flight_id = get_flight_id(flight_code)
    crew_id = get_crew_id(fname, lname, phone_num)

    if (flight_id == -1 or crew_id == -1):
        print("çalışan veya flight bilgileri yanlış girildi.")
        return -1
    command = """DELETE FROM flight_crew where Flight_ID = '%s' and Crew_ID = '%s'""" % (flight_id, crew_id)
    return executeCommand(command)

def add_airport(airport_name, location, country, time_zone):
    if(get_airport(airport_name) != -1):
        print("öyle bir airport zaten eklendi")
        return -1

    command = ("""INSERT INTO airports (Airport_Name, Location, Country, Timezone) VALUES ('%s', '%s', '%s', '%s')"""
               % (airport_name, location, country, time_zone))
    return executeCommand(command)

def remove_airport(airport_name):
    airport_id = get_airport(airport_name)
    if(airport_id == -1):
        print("kayıylı böyle bir airport bulunmuyor")
        return -1

    command = """DELETE FROM airports as a where Airport_ID = '%s'""" % (airport_id)
    return executeCommand(command)

app = Flask(__name__)

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'  # Replace with your MySQL username
app.config['MYSQL_PASSWORD'] = sifre  # Replace with your MySQL password
app.config['MYSQL_DB'] = 'airlinereservationsystem'  # Your existing schema name

mysql = MySQL(app)

user_id = -1


# Helper: Admin check
def is_admin():
    return user_id == -1


if __name__ == '__main__':
    with app.app_context():
        # cursor = mysql.connection.cursor()

        command = """
            INSERT INTO bookings(Flight_ID, Passenger_ID, Booking_Date, Seat_Column, Seat_Row, Booking_Status, Seat_Type)
            VALUES (1,100, '2069-11-28 12:00:00', 'A' ,11 ,'Confirmed','Economy');
        """
        # Uncomment the next command for testing queries
        command = """
            Select Passenger_id from Passengers
            where Passport_Number = 'P8460896'
        """

        # values = executeCommand(command)
        # values = get_avaliable_flights("India", "Australia")
        # print(values)  # For INSERT, this will likely print 0 as no rows are returned

        # command = ("""SELECT * from bookings WHERE bookings.Flight_ID = '%s' AND
        # AND bookings.Passenger_ID IN  """ % (30, 123))
        # command = """ Select Distinct(Passenger_ID) from passengers WHERE passengers.Passport_Number = '%s' """ % (123)

#         print(executeCommand("""UPDATE airlinereservationsystem.flights t
# SET t.Departure_Time = '2024-11-20 21:08:11',
#     t.Arrival_Time   = '2024-11-13 21:08:12',
#     t.Fligth_Status  = 'Delayed'
# WHERE t.Flight_ID = '%s' """ % 33))
        # print(get_crew_id("FirstName_1", "LastName_1", 8628822263))

        print(executeCommand("""INSERT INTO airlinereservationsystem.airports (Airport_Name, Location, Country, Timezone)
VALUES ('Airport_11', 'City_1, Country_1', 'Brazil', 'PST');"""))
        # print(check_booking_availability(30, 1000, 'Z', 104))
        # print(remove_booked_flight(30, 123))
        # mysql.connection.commit()  # Ensure changes are saved to the database for INSERT/UPDATE/DELETE
