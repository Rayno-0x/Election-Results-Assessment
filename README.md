Election Results Web Application (Bincom Assessment)

This is a Python-based web application developed as part of the Bincom Dev Center recruitment process. The application interacts with a database of the 2011 Nigerian election results to display and manage polling data.

Features
The application addresses the following technical requirements:

Question 1 (Polling Unit Results): Displays the results of individual polling units from the announced_pu_results table.

Question 2 (LGA Totals): Allows users to select a Local Government Area (LGA) from a dropdown to see the summed total of results for all polling units with**Election Results Web Application (Bincom Assessment)**

This is a Python-based web application developed as part of the Bincom Dev Center recruitment process. The application interacts with a database containing the 2011 Nigerian election results to display and manage polling data.

### Features

The application includes the following technical requirements:

1. **Polling Unit Results:** Displays the results of individual polling units from the `announced_pu_results` table.
   
2. **LGA Totals:** Allows users to select a Local Government Area (LGA) from a dropdown menu to view the summed total of results for all polling units within that area.

3. **New Data Entry:** Provides a user-friendly form for storing new election results for all parties within a specific polling unit.

### Tech Stack

- **Language:** Python 3.14
- **Framework:** Flask
- **ORM:** Flask-SQLAlchemy
- **Database:** MySQL (via XAMPP)
- **Frontend:** HTML/Jinja2

### Installation and Setup

To run this project locally, follow these steps:

1. **Clone the Repository:**

   ```bash
   git clone [Your-GitHub-Repository-Link]
   ```

2. **Install Dependencies:**
   
   Ensure you have Python installed, then run:

   ```bash
   pip install flask flask-sqlalchemy mysql-connector-python
   ```

3. **Database Configuration:**

   Import the provided `bincom_test.sql` file into your local MySQL server (e.g., using phpMyAdmin).

   Update the `SQLALCHEMY_DATABASE_URI` in `app.py` with your database credentials.

4. **Run the Application:**

   ```bash
   python app.py
   ```

   Access the app in your browser at [http://127.0.0.1:5000](http://127.0.0.1:5000).

### Project Structure

- **app.py:** Contains the main application logic, database models, and routes.
- **templates/:** Folder containing HTML files for rendering the web pages.
- **bincom_test.sql:** Contains the database schema and the dataset of the 2011 election results in that area.

Question 3 (New Data Entry): A user-friendly form to store new election results for all parties in a specific polling unit.

Tech Stack
Language: Python 3.14
Framework: Flask
ORM: Flask-SQLAlchemy
Database: MySQL (via XAMPP)
Frontend: HTML

Installation and Setup
To run this project locally, follow these steps:

Clone the Repository:

Bash
git clone [Your-GitHub-Repository-Link]
Install Dependencies:
Ensure you have Python installed, then run:

Bash
pip install flask flask-sqlalchemy mysql-connector-python
Database Configuration:

Import the provided bincom_test.sql file into your local MySQL server (e.g., via phpMyAdmin).

Update the SQLALCHEMY_DATABASE_URI in app.py with your database credentials.

Run the Application:

Bash
python app.py
Access the app in your browser at http://127.0.0.1:5000.

Project Structure
app.py: Main application logic, database models, and routes.

templates/: Folder containing HTML files for rendering the web pages.

bincom_test.sql: The database schema and 2011 election results dataset.
