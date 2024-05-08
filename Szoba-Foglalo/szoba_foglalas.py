from abc import ABC, abstractmethod
from datetime import datetime

class Room(ABC):
    @abstractmethod
    def __init__(self, price, number_of_rooms):
        self.price = price
        self.number_of_rooms = number_of_rooms

class SingleRoom(Room):
    def __init__(self, price, number_of_rooms, single_bed):
        super().__init__(price, number_of_rooms)
        self.single_bed = single_bed

class DoubleRoom(Room):
    def __init__(self, price, number_of_rooms, double_bed):
        super().__init__(price, number_of_rooms)
        self.double_bed = double_bed

class Hotel:
    def __init__(self, name, rooms):
        self.name = name
        self.rooms = rooms

class Reservation:
    def __init__(self, id, hotel, room, date):
        self.id = id
        self.hotel = hotel
        self.room = room
        self.date = date

class BookingSystem:
    def __init__(self):
        self.reservations = []
        self.next_id = 1

    def book_room(self, hotel, room, date):
        if date < datetime.now():
            return "Invalid date. Please enter a future date."
        for reservation in self.reservations:
            if reservation.hotel == hotel and reservation.room == room and reservation.date == date:
                return "Room is not available on this date."
        new_reservation = Reservation(self.next_id, hotel, room, date)
        self.reservations.append(new_reservation)
        self.next_id += 1
        return f"Reservation ID: {new_reservation.id}, Hotel: {new_reservation.hotel.name}, Room: {type(new_reservation.room).__name__}, Date: {new_reservation.date}"

    def cancel_reservation(self, id):
        for reservation in self.reservations:
            if reservation.id == id:
                self.reservations.remove(reservation)
                return "Reservation cancelled."
        return "Reservation does not exist."

    def list_reservations(self):
        for reservation in self.reservations:
            print(f"Hotel: {reservation.hotel.name}, Room: {type(reservation.room).__name__}, Date: {reservation.date}")

def main():
    # Create rooms
    single_room = SingleRoom(100, 1, True)
    double_room = DoubleRoom(200, 2, True)

    # Create hotel
    hotel = Hotel("The Grand Budapest", [single_room, double_room])

    # Create booking system
    booking_system = BookingSystem()

    # Add initial reservations
    booking_system.book_room(hotel, single_room, datetime(2024, 5, 10))
    booking_system.book_room(hotel, double_room, datetime(2024, 5, 11))

    while True:
        print("1. Book a room")
        print("2. Cancel a reservation")
        print("3. List all reservations")
        print("4. Exit")
        choice = input("Select an option: ")

        try:
            if choice == "1":
                date_str = input("Enter date (yyyy-mm-dd): ")
                date = datetime.strptime(date_str, "%Y-%m-%d")
                room_type = input("Enter room type (single/double): ")
                room = single_room if room_type == "single" else double_room
                print(booking_system.book_room(hotel, room, date))
            elif choice == "2":
                reservation_id = int(input("Enter reservation id: "))
                print(booking_system.cancel_reservation(reservation_id))
            elif choice == "3":
                booking_system.list_reservations()
            elif choice == "4":
                break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()