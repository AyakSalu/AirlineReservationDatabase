from flask_mysqldb import MySQL
from flask import Flask
from Sifreler import sifre


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

def remove_booked_flight(flight_id, passport_num):
    command = ("""DELETE FROM bookings 
    WHERE bookings.Flight_ID = '%s' 
    AND bookings.Passenger_ID IN (SELECT unique(Passenger_ID) from passengers WHERE Passport_Number = '%s')"""
               % (flight_id, passport_num))
    return executeCommand(command)
def get_avaliable_flights(departure_country, arrival_country):
    command = (""" SELECT Flight_Code,a1.Airport_Name, a1.Country,Departure_Time, a2.Airport_Name,a2.Country, Arrival_Time , Airline
    FROM flights 
    natural join planes
    inner join airports as a1 on a1.Airport_ID = flights.Departure_Airport_ID
    inner join airports as a2 on a2.Airport_ID = flights.Arrival_Airport_ID
    Where a1.Country = '%s' AND a2.Country ='%s' AND capacity > 0"""
               % (departure_country, arrival_country))
    print(command)
    return executeCommand(command)


def get_next_bookid():
    maxBookingIdCommand = """SELECT max(Booking_ID)  
                from bookings 
                """
    return executeCommand(maxBookingIdCommand)[0][0] + 1

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

def view_purchased_flights():
    command = """SELECT * FROM bookings WHERE Purchased_Flights"""


if __name__ == '_main_':
    with app.app_context():
        cursor = mysql.connection.cursor()

        command = """
             SELECT Flight_Code,a1.Airport_Name, a1.Country,Departure_Time, a2.Airport_Name,a2.Country, Arrival_Time , Airline
    FROM flights
    natural join planes
    inner join airports as a1 on a1.Airport_ID = flights.Departure_Airport_ID
    inner join airports as a2 on a2.Airport_ID = flights.Arrival_Airport_ID
    Where a1.Country = 'india' AND a2.Country ='australia' 
         """
        values = executeCommand(command)

        #values = executeCommand(command)
        print(values)  # For INSERT, this will likely print 0 as no rows are returned
        mysql.connection.commit()  # Ensure changes are saved to the database for INSERT/UPDATE/DELETE