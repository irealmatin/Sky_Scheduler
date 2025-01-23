
"""
each flight have these objects :
- Pilot's name
- Flight number
- Flight time
- Number of passengers
- origin city
- destination city

our system have these feature :
- Display information about all flights in ascending order based on flight number
- Change the time of a flight with a given number
- Print information about all flights to a specific destination
- Get information about a flight from the input
- Print information about the flight with the highest number of passengers
- Delete a flight with a given number
"""

from AVL_Tree import AvlTree

class Flight:
    def __init__(self, flight_number, pilot_name, flight_time, passengers, origin, destination):
        self.flight_number = flight_number
        self.flight_time = flight_time
        self.pilot_name = pilot_name
        self.passengers = passengers
        self.origin = origin
        self.destination = destination

    def __str__(self):
        return (f"Flight Number: {self.flight_number}, Pilot's name: {self.pilot_name}, "
                f"Flight Time: {self.flight_time}, Passengers: {self.passengers}, "
                f"Origin: {self.origin}, Destination: {self.destination}")

class FlightManager:
    def __init__(self):
        self.flight_tree = AvlTree()

    def add_flight(self):
        flight_number = self.get_integer_input("Enter Flight Number: ")
        pilot_name = self.get_string_input("Enter Pilot's name: ")
        flight_time = self.get_flight_time_input()
        passengers = self.get_integer_input("Enter Number of Passengers: ")
        origin = self.get_string_input("Enter Origin City: ")
        destination = self.get_string_input("Enter Destination City: ")
        flight = Flight(flight_number, pilot_name, flight_time, passengers, origin, destination)
        self.flight_tree.insert(flight_number, flight)
        print("Flight added successfully.")

    @staticmethod    
    def get_integer_input(prompt):
        """Helper function to get valid integer input from the user."""
        while True:
            try:
                value = int(input(prompt))
                return value
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
    @staticmethod
    def get_string_input(prompt):
        while True:
            value = input(prompt).strip() 
            if all(char.isalpha() or char.isspace() for char in value): # handle space error  : matin '' mohamadi -> Done!
                return value
            print("Invalid input. Please enter only letters.")

            # elif value:  #  is empty or not
            #     return value
            # print("Invalid input. Please enter a non-empty string.")

    
    def get_flight_time_input(self):
        """
        Helper function to get valid flight time input in HH:MM format from the user.
        """
        while True:
            time_input = input("Enter Flight Time (HH:MM): ").strip()
            
            # Check if the input matches the HH:MM format
            if len(time_input) == 5 and time_input[2] == ':' and time_input[:2].isdigit() and time_input[3:].isdigit():
                hours = int(time_input[:2])
                minutes = int(time_input[3:])
                
                # Validate hours and minutes
                if 0 <= hours < 24 and 0 <= minutes < 60:
                    return time_input  # Return the valid time in HH:MM format
                else:
                    print("Invalid time. Hours must be between 00 and 23, and minutes between 00 and 59.")
            else:
                print("Invalid format. Please enter time in HH:MM format (e.g., 14:30).")

    def display_all_flights(self):
        print("\nAll Flights:")
        self.flight_tree.print_inorder()

    def change_flight_time(self): # hnale hh:mm format -> Done!
        flight_number = int(input("Enter Flight Number to Change Time: "))
        while True:
            new_time = input("Enter New Flight Time (HH:MM): ")
            if len(new_time) == 5 and new_time[2] == ':' and new_time[:2].isdigit() and new_time[3:].isdigit():
                break
            print("Invalid time format. Please use HH:MM.")
        node = self.flight_tree.search(self.flight_tree.root, flight_number)
        if node:
            node.value.flight_time = new_time
            print("Flight time updated successfully.")
        else:
            print("Flight not found.")

    def display_flights_to_same_destination(self): #handle no dest : Done!
        destination = input("Enter Destination City: ")
        print(f"\nFlights to {destination}:")
        found = False
        for key, value in self.flight_tree.inorder_traversal(self.flight_tree.root):
            if value.destination == destination:
                print(value)
                found = True
        if not found:
            print("No flights found to this destination.")

    def display_flight_with_most_passengers(self):
        max_passengers = -1
        flight_with_most_passengers = None
        for key, value in self.flight_tree.inorder_traversal(self.flight_tree.root):
            if value.passengers > max_passengers:
                max_passengers = value.passengers
                flight_with_most_passengers = value
        if flight_with_most_passengers:
            print("\nFlight with Most Passengers:")
            print(flight_with_most_passengers)
        else:
            print("No flights found.")

    def delete_flight(self):  # handle no exist : Done!
        flight_number = int(input("Enter Flight Number to Delete: "))
        node = self.flight_tree.search(self.flight_tree.root, flight_number)
        if node:
            self.flight_tree.delete(flight_number)
            print("Flight deleted successfully.")
        else:
            print("Flight not found.")

    def get_specific_flight_info(self):
        flight_number = int(input("Enter Flight Number to see the information:"))
        node = self.flight_tree.search(self.flight_tree.root , flight_number)

        if node :
            print("\nFlight Informations:")
            print(node.value)
        else:
            print("Flight Not Found")
        

def print_menu():
    print("\n--------------------------Flight Management System--------------------------")
    print("1. Add Flight")
    print("2. Display All Flights")
    print("3. Change Flight Time")
    print("4. Display Flights to same Destination")
    print("5. Display Flight with Most Passengers")
    print("6. Delete Flight")
    print("7. Display Specific Flight Information")
    print("8. Exit")

def main():
    flight_manager = FlightManager()
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            flight_manager.add_flight()
        elif choice == '2':
            flight_manager.display_all_flights()
        elif choice == '3':
            flight_manager.change_flight_time()
        elif choice == '4':
            flight_manager.display_flights_to_same_destination()
        elif choice == '5':
            flight_manager.display_flight_with_most_passengers()
        elif choice == '6':
            flight_manager.delete_flight()
        elif choice == '7':
            flight_manager.get_specific_flight_info()
        elif choice == '8':    
            print("Good Luck User!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
        