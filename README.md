# Flight Management System


## Overview

The **Flight Management System** is a Python-based application designed to manage flight information using an AVL tree data structure. It allows users to perform various operations such as adding flights, deleting flights, searching for flights, and displaying flight details in a sorted order.

## Features

- **Add Flight**: Add a new flight with details such as flight number, pilot name, flight time, number of passengers, origin city, and destination city.
- **Display All Flights**: Display all flights in ascending order based on flight number.
- **Change Flight Time**: Update the flight time for a specific flight.
- **Display Flights to a Destination**: Display all flights heading to a specific destination city.
- **Display Flight with Most Passengers**: Display the flight with the highest number of passengers.
- **Delete Flight**: Delete a flight by its flight number.
- **Search Flight**: Retrieve detailed information about a specific flight.

## How To Run 

put all .py file together in a file and then write this in terminal(in related location) :

```bash
python main.py

```
## How To Test :

Unit tests are provided for the `AvlTree` and `FlightManager` classes. To run the tests, use the following commands:

```bash
python test_avltree.py
python test_main.py
```

or 

```bash
python -m unittest test_avltree.py
python -m unittest test_main.py
```
 
## Usage:

- Run the application using python main.py.

- Follow the screen menu to perform operations:

1: Add a new flight.

2: Display all flights.

3: Change flight time.

4: Display flights to a specific destination.

5: Display the flight with the most passengers.

6: Delete a flight.

7: Display specific flight information.

8: Exit the application.


## Dependencies :

- Python 3.8 or higher.