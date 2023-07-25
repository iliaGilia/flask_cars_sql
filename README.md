#MySQL "Cars" Flask App
The MySQL "Cars" Flask App is a simple web application that allows users to manage a collection of cars. It utilizes Flask, a Python web framework, and MySQL as the database to store car data.

#Features
View a list of all cars in the database.
Add a new car to the collection.
Edit the details of an existing car.
Delete a car from the database.
Getting Started
Prerequisites
#Before running the app, make sure you have the following installed:

Python (version 3.6 or higher)
MySQL database server
Pip (Python package manager)

Install the required packages:
```pip install -r requirements.txt```

Create a MySQL database:

Log in to your MySQL database server using a client like mysql or phpMyAdmin.
Create a new database named car_database:
```CREATE DATABASE car_database;```
Create a table named cars with columns: id (INT, primary key, auto-increment), make (VARCHAR), model (VARCHAR), and year (INT):
```CREATE TABLE cars (
    id INT AUTO_INCREMENT PRIMARY KEY,
    make VARCHAR(255) NOT NULL,
    model VARCHAR(255) NOT NULL,
    year INT NOT NULL
);
```

#Usage
View the list of cars by visiting the homepage (/ or /cars).
To add a new car, click the "Add Car" button on the homepage, fill in the car details in the form, and submit it.
To edit a car's details, click the "Edit" link next to the car you wish to modify, update the details in the form, and submit the changes.
To delete a car from the collection, click the "Delete" link next to the car you want to remove.
