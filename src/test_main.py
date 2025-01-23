import unittest
from unittest.mock import patch # we use this for handle hardcode and prevent user input 

from main import Flight, FlightManager 

class TestFlightManager(unittest.TestCase):
    def setUp(self):
        """Set up a FlightManager instance and
          pre-load some test flights."""
        self.manager = FlightManager()
        # Add some test flights
        self.manager.flight_tree.insert(101, Flight(101, "Matin Mohammadi", "12:00", 150, "kashan", "tehran"))
        self.manager.flight_tree.insert(102, Flight(102, "Alireza ashrafi", "14:00", 200, "kerman", "yazd"))
        self.manager.flight_tree.insert(103, Flight(103, "fateme rezai", "16:00", 180, "shomal", "bandar abbas"))

    def test_add_flight(self):
        new_flight = Flight(104, "matin matin", "18:00", 100, "tehran", "kish")
        self.manager.flight_tree.insert(104, new_flight)
        node = self.manager.flight_tree.search(self.manager.flight_tree.root, 104)
        self.assertIsNotNone(node)
        self.assertEqual(node.value, new_flight)

    def test_display_all_flights(self):
        flights = list(self.manager.flight_tree.inorder_traversal(self.manager.flight_tree.root))
        self.assertEqual(len(flights), 3)
        self.assertEqual(flights[0][0], 101)  # Flight numbers in sorted order
        self.assertEqual(flights[1][0], 102)
        self.assertEqual(flights[2][0], 103)

    def test_change_flight_time(self):
        """Test changing flight time."""
        with patch('builtins.input', side_effect=["101", "11:00"]):
            self.manager.change_flight_time()
            node = self.manager.flight_tree.search(self.manager.flight_tree.root, 101)
            self.assertEqual(node.value.flight_time, "11:00")

    def test_display_flights_to_same_destination(self):
        """Test displaying flights to the same destination."""
        destination = "tehran"
        flights_to_tehran = []
        for _, flight in self.manager.flight_tree.inorder_traversal(self.manager.flight_tree.root):
            if flight.destination == destination:
                flights_to_tehran.append(flight)
        self.assertEqual(len(flights_to_tehran), 1)
        self.assertEqual(flights_to_tehran[0].flight_number, 101)

    def test_display_flight_with_most_passengers(self):
        """Test finding the flight with the most passengers."""
        max_flight = None
        max_passengers = -1
        for _, flight in self.manager.flight_tree.inorder_traversal(self.manager.flight_tree.root):
            if flight.passengers > max_passengers:
                max_passengers = flight.passengers
                max_flight = flight
        self.assertIsNotNone(max_flight)
        self.assertEqual(max_flight.flight_number, 102)

    def test_delete_flight(self):
        self.manager.flight_tree.delete(102)
        node = self.manager.flight_tree.search(self.manager.flight_tree.root, 102)
        self.assertIsNone(node)

    def test_get_specific_flight_info(self):
        """Test retrieving specific flight information."""
        flight_number = 101
        node = self.manager.flight_tree.search(self.manager.flight_tree.root, flight_number)
        self.assertIsNotNone(node)
        self.assertEqual(node.value.flight_number, flight_number)

if __name__ == "__main__":
    unittest.main()

# i get output if u want see it now :
"""
.Flight time updated successfully.
......
----------------------------------------------------------------------
Ran 7 tests in 0.002s

OK
"""