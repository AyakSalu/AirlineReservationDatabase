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
    

    command = """SELECT Flight_Id,arrivalAirport.Airport_Name,departureAirport.Airport_Name ,Airline  
            from flights join airports as arrivalAirport on arrivalAirport.Airport_ID = flights.arrival_Airport_ID 
                         join airports as departureAirport on departureAirport.Airport_ID = flights.Departure_Airport_ID
                         join planes on planes.Plane_ID = flights.Plane_ID
            where Airline IS NOT NULL"""
    values = executeCommand(command)
    print(values)

