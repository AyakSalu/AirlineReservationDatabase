from flask_mysqldb import MySQL
from flask import Flask
from Sifreler import sifre


def executeCommand(command):
    cursor = mysql.connection.cursor()
    cursor.execute(command)
    data = cursor.fetchall()
    cursor.close()
    mysql.connection.commit()
    return data

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
"""
# Helper: Admin check
def is_admin():
    return session.get("user_role") == "admin"


@app.route('/test_db', methods=['GET'])
def test_db():
    cursor = mysql.connection.cursor()
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    return jsonify({"tables": tables})


# Routes
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username, password = data['username'], data['password']

    # Hash password
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    # Insert into DB
    cursor = mysql.connection.cursor()
    try:
        cursor.execute("INSERT INTO Users (username, password, role) VALUES (%s, %s, %s)",
                       (username, hashed_password, 'user'))
        mysql.connection.commit()
        return jsonify({"message": "Registration successful"}), 201
    except:
        return jsonify({"message": "Registration failed, username may already exist"}), 400


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username, password = data['username'], data['password']

    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM Users WHERE username = %s", (username,))
    user = cursor.fetchone()

    if user and bcrypt.check_password_hash(user['password'], password):
        session['user_id'] = user['id']
        session['user_role'] = user['role']
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401

@app.route('/')
def home():
    return "Welcome to the Airline Reservation System API!", 200

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({"message": "Logged out"}), 200


@app.route('/book_ticket/<int:flight_id>', methods=['POST'])
def book_ticket(flight_id):
    if not session.get('user_id'):
        return jsonify({"message": "Unauthorized"}), 401

    user_id = session['user_id']

    # Check availability
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM Bookings WHERE flight_id = %s", (flight_id,))
    if cursor.fetchone():
        return jsonify({"message": "Ticket already booked"}), 400

    # Book ticket
    cursor.execute("INSERT INTO Bookings (user_id, flight_id) VALUES (%s, %s)", (user_id, flight_id))
    mysql.connection.commit()
    return jsonify({"message": "Ticket booked successfully"}), 201


def manage_flights():
    if not is_admin():
        return jsonify({"message": "Unauthorized"}), 403

    cursor = mysql.connection.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM Flights")
        flights = cursor.fetchall()
        return jsonify(flights), 200

    if request.method == 'POST':
        data = request.json
        # Add new flight
        cursor.execute(
            INSERT INTO Flights (plane_id, departure_airport_id, arrival_airport_id, departure_time, arrival_time)
            VALUES (%s, %s, %s, %s, %s)
        , (data['plane_id'], data['departure_airport_id'], data['arrival_airport_id'], data['departure_time'],
              data['arrival_time']))
        mysql.connection.commit()
        return print("Flight added successfully")


@app.route('/admin/users', methods=['GET'])
def manage_users():
    if not is_admin():
        return print("You are not authorized to manage users")

    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM Users")
    users = cursor.fetchall()
    return users
"""
if __name__ == '__main__':
    with app.app_context():
        cursor = mysql.connection.cursor()
        # command = """
        #     INSERT INTO bookings(Flight_ID, Passenger_ID, Booking_Date, Seat_Column, Seat_Row, Booking_Status, Seat_Type)
        #     VALUES (1,100, '2069-11-28 12:00:00', 'A' ,11 ,'Confirmed','Economy');
        # """
        # Uncomment the next command for testing queries
        fname = "a"
        lname = "b"
        passportNumber = "P1234"
        phoneNumber = "1"
        email = "d"
        command = """
                INSERT INTO Passengers (Fname, Lname, Passport_Number, Phone_Number, Email) 
                VALUES ('%s', '%s', '%s', '%s', '%s');
            """%(fname,lname,passportNumber,phoneNumber,email)
        command = """
        Select Passenger_ID from Passengers 
        where Passport_Number = '%s'
        """%("p2")
        text = "P2311557"
        command = """SELECT flights.Flight_Id,arrivalAirport.Airport_Name,departureAirport.Airport_Name ,Airline  
            from flights join airports as arrivalAirport on arrivalAirport.Airport_ID = flights.arrival_Airport_ID 
                         join airports as departureAirport on departureAirport.Airport_ID = flights.Departure_Airport_ID
                         join planes on planes.Plane_ID = flights.Plane_ID
                         join bookings on flights.Flight_Id = bookings.Flight_Id
                         join passengers on passengers.Passenger_ID = bookings.Passenger_ID
            where passengers.Passport_Number = '%s'"""%text
        print(command)
        values = executeCommand(command)
        print(values)  # For INSERT, this will likely print 0 as no rows are returned
        mysql.connection.commit()  # Ensure changes are saved to the database for INSERT/UPDATE/DELETE