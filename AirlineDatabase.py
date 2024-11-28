from flaskext.mysql import MySQL
from flask import Flask
from Sifreler import sifre

def executeCommand(command):
    cursor.execute(command)
    data = cursor.fetchall()
    return data
app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = sifre #kendi sifresin gir
app.config['MYSQL_DATABASE_DB'] = 'airlinereservationsystem'  #database adı
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect()
cursor =conn.cursor()
if __name__ == '__main__':
    

    command = """
        INSERT INTO bookings(Flight_ID, Passenger_ID, Booking_Date, Seat_Column, Seat_Row, Booking_Status, Seat_Type)
        VALUES (1,200, '2069-11-28 12:00:00', 'A' ,11 ,'Confirmed','Economy');
        """ 
    command = """
        Select Passenger_id from Passengers 
        where Passport_Number = 'P8460896'
        """
    values = executeCommand(command)
    print(len(values))

