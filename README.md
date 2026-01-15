# 🏨 Hotel Management System 🏨

Welcome to the **Hotel Management System** built using **Python** 🐍 and **Tkinter** for the user interface, along with a powerful **MySQL** database for data management 🗄️. This system is designed to help manage hotel operations seamlessly with **user authentication**, **room management**, **customer details**, **booking reports**, and **admin access**.

## 🚀 Features:
- **Admin Panel** with full control over customer data, bookings, and reports 🛠️.
- **User Authentication** with forgot password functionality and security questions 🔐.
- **Customer Management**: View, add, update, and delete customer records 🧳.
- **Room Management**: Check room availability, add new rooms, and assign bookings 🏠.
- **Booking & Reports**: Generate and view reports on customer bookings 📊. 

## 🛠️ Technologies Used:
- **Frontend**: Python with **Tkinter** (Graphical User Interface) 🖥️.
- **Backend**: **MySQL** (database) 💾.
- **Security**: High-level security features like **Forgot Password**, **Security Questions**, and **Admin Access** 🔒.

## 💡 How to Run:

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/your-username/hotel-management-system.git
    ```

2. **Install Dependencies:**
    - Install **Tkinter** (it usually comes with Python, but if not, you can install it via pip).
    - Install **MySQL** and configure the connection using your credentials.

3. **Database Setup:**
    - Open **MySQL Workbench**.
    - Create a new database: `hotel_management_system`.
    - Import the necessary tables for **customer data**, **rooms**, **bookings**, etc.

4. **Run the Application:**
    ```bash
    python main.py
    ```

## 📂 Files Description:
- **`customer.py`**: Handles customer-related functions such as adding and updating customer details 📇.
- **`details.py`**: Manages specific customer and booking details, and integrates with the database 🔍.
- **`hotel.py`**: Core logic for the hotel management system 🏨.
- **`login.py`**: Authentication module for **user login** and **forgot password** functionality 🔑.
- **`register.py`**: User registration and profile creation for customers and admins 📝.
- **`report.py`**: Generates and displays booking and customer reports 📑.
- **`room.py`**: Manages room assignments, availability, and booking statuses 🛏️.

## 🛡️ Security Features:
- **User Authentication**: Secure login system with username and password 🔑.
- **Forgot Password**: Users can reset their password via email or security question ❓.
- **Admin Access**: Admins have extra privileges like modifying rooms, booking details, and viewing all customer data 🔒.

## 📚 Screenshots:
1. **Login Screen**  
   ![Login Screen](https://github.com/Mohit-Kumawat2004/Hotel-Management-System/blob/main/Output%20Images/image%20login.png)

2. **Admin Dashboard**  
   ![Admin Dashboard](https://github.com/Mohit-Kumawat2004/Hotel-Management-System/blob/main/Output%20Images/admin.png)

3. **Room Management**  
   ![Room Management](https://github.com/Mohit-Kumawat2004/Hotel-Management-System/blob/main/Output%20Images/room.png)

4. **Booking Report**  
   ![Booking Report](https://github.com/Mohit-Kumawat2004/Hotel-Management-System/blob/main/Output%20Images/About.png)

5. **Registration User**
   ![Registration New User](https://github.com/Mohit-Kumawat2004/Hotel-Management-System/blob/main/Output%20Images/register.png)

## ⚙️ Installation Instructions:
1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/your-username/hotel-management-system.git
    ```

2. Install the required Python libraries:
    ```bash
    pip install -r requirements.txt
    ```

3. Make sure to have **MySQL** installed and configured on your machine for database operations.

## 📑 Contributing:
We welcome contributions! If you’d like to contribute, feel free to fork this repository and submit a **pull request**. Please make sure to follow these steps:
1. Fork the repository
2. Create a new branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -am 'Add feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Create a new Pull Request

## 📝 License:
This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.
