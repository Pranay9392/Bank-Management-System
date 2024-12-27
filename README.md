# Bank Management System (Python Backend)

This project is a simple Python-based backend implementation for a **Bank Management System**. It allows customers to perform basic banking operations like balance inquiry, deposit, withdrawal, and fund transfer. The system uses a MySQL database for persistent storage of customer information and transaction history.

---

## Features

1. **Customer Account Management**
   - Create new customer accounts (`SignUp`).
   - Secure login functionality (`SignIn`).

2. **Banking Services**
   - Balance inquiry.
   - Deposit funds.
   - Withdraw funds.
   - Transfer funds to another account.

3. **Transaction History**
   - Records all transactions for each customer, stored in dedicated tables.

4. **MySQL Database Integration**
   - Manages customer details and banking transactions.

---

## Project Structure

### Files and Modules

1. **`main.py`**
   - Entry point for the application.
   - Manages the main menu for user registration and banking services.

2. **`register.py`**
   - Handles `SignUp` and `SignIn` functionality.
   - Verifies and manages user credentials.

3. **`customer.py`**
   - Manages customer details and account creation in the database.

4. **`bank.py`**
   - Implements core banking functionalities:
     - Balance inquiry
     - Deposit
     - Withdrawal
     - Fund transfer

5. **`database.py`**
   - Connects to a MySQL database.
   - Provides helper functions for querying the database.
   - Contains the `create_customer_table` function to initialize the database schema.

6. **Database Schema**
   - **`customers` table:** Stores customer details and balances.
   - **`<username>_transactions` table:** Stores transaction history for individual users.

---

## Concepts and Implementation

### Object-Oriented Programming (OOP)
- **Encapsulation:** 
  - Private attributes (e.g., `__username`, `__password`) ensure data security.
  - Access through methods only.
  
- **Classes:**
  - `Bank`: Handles banking operations.
  - `Customer`: Manages customer data and account creation.

### Database Management
- **MySQL Integration:**
  - Database queries are executed using `mysql-connector` Python library.
  - Tables:
    - `customers`: Stores user credentials, balances, and status.
    - Transaction tables (`<username>_transactions`): Dynamically created for each user to store their transaction history.
  
### Error Handling
- Input validation for user choices and operations.
- Checks for sufficient balance during withdrawals and fund transfers.

---

## Installation and Setup

### Prerequisites
1. Python 3.x installed on your system.
2. MySQL server installed and running.
3. Python packages:
   - `mysql-connector-python`

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/bank-management.git
   cd bank-management
