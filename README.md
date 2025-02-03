# Railway Management System API

A powerful railway management system developed with Django. It allows users to register, log in, check seat availability, book seats, and view booking details. The system supports role-based access control (Admin and User) and ensures smooth seat booking with race condition handling.

---

## 🚀 Features

- 👥 **User Roles:** Distinct Admin and User roles with tailored functionalities.  
- 🔒 **Secure Bookings:** Advanced mechanisms to prevent double-booking and handle race conditions.  
- 🔑 **Effortless Authentication:** Secure login and registration for a seamless user experience.  
- 📖 **API Endpoints:** Well-documented APIs for easy frontend or system integration.  
- 🗄️ **Database Support:** Powered by PostgreSQL for efficient, reliable data storage.  
- ⏱️ **Real-time Updates:** Real-time seat availability updates during booking.
- 🛡️ **Role-based Access Control:** Admin APIs secured with API key authentication for extra security.  
- 🚆 **Customizable Trains:** Admins can add trains with source, destination, and seat capacity. 
- 💻 **Platform Independence:** Fully functional on Windows, macOS, and Linux systems.  
- 📈 **Scalability:** Designed to handle multiple users and concurrent booking requests efficiently.  
- 🔧 **Extensibility:** Built with Django’s modularity for easy feature and integration expansions.  


---

## 🛠️ Installation Steps

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/lakshay12793/workindia_assignment_irctc-main.git
    cd workindia_assignment_irctc-main/workindia_assignment_railway_management_system-main
    ```

2. **Create and Activate a Virtual Environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # For Windows: `venv\Scripts\activate`
    ```

3. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Install PostgreSQL** if not already installed. Refer to the [PostgreSQL Documentation](https://www.postgresql.org/docs/) for installation instructions.

5. **Set Up PostgreSQL Database:**

    ```bash
    psql -U postgres -c "CREATE DATABASE railway_management_test;"
    ```

6. **Update Database Settings:**

    Edit the `DATABASES` section in `settings.py` with your PostgreSQL credentials:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'railway_management_test',
            'USER': 'your_postgres_username',
            'PASSWORD': 'your_postgres_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```

---

## 🧑‍💻 Project Setup

1. **Apply Migrations:**

    ```bash
    python manage.py migrate
    ```

2. **Create a Superuser:**

    ```bash
    python manage.py createsuperuser
    ```

3. **Start the Development Server:**

    ```bash
    python manage.py runserver
    ```

---

## 🌐 API Endpoints

Below are the available API endpoints for the Railway Management System, along with example payloads and responses using the dummy user credentials.

---

### 🛂 Authentication Endpoints

1. **Register User**  
   - **Endpoint:** `/register/`  
   - **Method:** `POST`  
   - **Description:** Allows a user to register with a username, password, and role (Admin/User).  
   - **Request Payload:**
     ```json
     {
       "username": "lakshayahlawat",
       "password": "123456789",
       "is_admin": false
     }
     ```
   - **Response Example:**
     ```json
     {
       "message": "User registered successfully",
       "user_id": 1
     }
     ```

2. **Login User**  
   - **Endpoint:** `/login/`  
   - **Method:** `POST`  
   - **Description:** Authenticates a user and returns a session token for subsequent requests.  
   - **Request Payload:**
     ```json
     {
       "username": "lakshayahlawat",
       "password": "123456789"
     }
     ```
   - **Response Example:**
     ```json
     {
       "message": "Login successful",
       "token": "abcd1234efgh5678"
     }
     ```

---

### 🚆 Train Management Endpoints

1. **Add Train**  
   - **Endpoint:** `/add_train/`  
   - **Method:** `POST`  
   - **Description:** Enables an admin to add a new train with source, destination, and total seats.  
   - **Request Payload (Admin Credentials):**
     ```json
     {
       "source": "Bhopal",
       "destination": "Delhi",
       "total_seats": 100
     }
     ```
   - **Response Example:**
     ```json
     {
       "message": "Train added successfully",
       "train_id": 10
     }
     ```

2. **Check Seat Availability**  
   - **Endpoint:** `/check_availability/Bhopal/Delhi/`  
   - **Method:** `GET`  
   - **Description:** Checks the seat availability for a train between the specified source and destination.  
   - **Response Example:**
     ```json
     {
       "source": "Bhopal",
       "destination": "Delhi",
       "available_seats": 50
     }
     ```

---

### 🪑 Booking Endpoints

1. **Book Seat**  
   - **Endpoint:** `/book_seat/`  
   - **Method:** `POST`  
   - **Description:** Allows users to book a seat for a specific train.  
   - **Request Payload:**
     ```json
     {
       "train_id": 10,
       "seats_to_book": 2
     }
     ```
   - **Response Example:**
     ```json
     {
       "message": "Seats booked successfully",
       "booking_id": 201,
       "booked_seats": 2
     }
     ```

2. **View Booking Details**  
   - **Endpoint:** `/booking_details/`  
   - **Method:** `GET`  
   - **Description:** Retrieves the booking details for the authenticated user.  
   - **Response Example:**
     ```json
     {
       "user_id": 1,
       "bookings": [
         {
           "booking_id": 201,
           "train_id": 10,
           "source": "Bhopal",
           "destination": "Delhi",
           "seats_booked": 2,
           "date": "2024-12-01"
         }
       ]
     }
     ```


2. **Authorization Header:**  
   Include your API key in the header for admin-specific actions:
   ```bash
   Token: "Token <token_of_admin>"

