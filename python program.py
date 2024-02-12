def create_event(event):
    event_name = input("Enter the name of the event: ")
    event_date = input("Enter the date of the event (YYYY-MM-DD): ")
    event_venue = input("Enter the venue of the event: ")
    event_seats = int(input("Enter the number of available seats: "))
    event[event_name] = {"date": event_date, "venue": event_venue, "seats": event_seats}
    print(f"Event '{event_name}' created successfully.")

def display_events(event):
    print("Upcoming Events:")
    for event_name, details in event.items():
        print(f"Name: {event_name}, Date: {details['date']}, Venue: {details['venue']}, Available Seats: {details['seats']}")

def book_ticket(event):
    event_name = input("Enter the name of the event you want to book tickets for: ")
    if event_name in event:
        num_tickets = int(input("Enter the number of tickets you want to book: "))
        if event[event_name]["seats"] >= num_tickets:
            event[event_name]["seats"] -= num_tickets
            print(f"{num_tickets} ticket(s) booked for '{event_name}'.")
        else:
            print("Insufficient seats available.")
    else:
        print("Event not found.")

def main():
    events = {}

    while True:
        print("\n1. Create Event\n2. Display Events\n3. Book Ticket\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            create_event(events)
        elif choice == "2":
            display_events(events)
        elif choice == "3":
            book_ticket(events)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
