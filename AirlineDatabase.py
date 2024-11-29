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


def get_avaliable_flights(departure_country, arrival_country):
    command = (""" SELECT Flight_Code,a1.Airport_Name, a1.Location,Departure_Time, a2.Airport_Name,a2.Location, Arrival_Time
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
    Where Flight_ID = '%s' AND ((Seat_Row = '%s' AND Seat_Column = '%s') OR Passenger_ID = '%s') """ % (flight_id, seat_row, seat_col, passenger_id))
    booking_available = len(executeCommand(command)) == 0

    #ikisi de boş kümeyse TRUE dönecek
    return booking_available


def remove_booked_flight(flight_id, passport_num):
    command = ("""DELETE FROM bookings 
    WHERE bookings.Flight_ID = '%s' 
    AND bookings.Passenger_ID IN (SELECT unique(Passenger_ID) from passengers WHERE Passport_Number = '%s')"""
               % (flight_id, passport_num))
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


def get_flight_id(flight_code):
    command = (""" SELECT flights.Flight_ID from flights where flights.Flight_Code = '%s' """ % (flight_code))
    return executeCommand(command)[0][0]  # id'yi int olarak döner


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

    #     command = ("""Delete FROM bookings
    # WHERE bookings.Flight_ID = '%s'
    # AND bookings.Passenger_ID IN (Select Distinct(Passenger_ID) from passengers WHERE passengers.Passport_Number = '%s')"""
    #                % (30, 123))
        # command = """ (SELECT unique(Passenger_ID) from passengers WHERE Passport_Number = '%s') """ % (123)
        # print(executeCommand(command))

        print(check_booking_availability(30, 1000, 'Z', 104))
        # print(remove_booked_flight(30, 123))
        # mysql.connection.commit()  # Ensure changes are saved to the database for INSERT/UPDATE/DELETE
