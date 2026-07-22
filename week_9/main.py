from ticket import create_ticket
from display import display_ticket

def main():
    # Create the ticket by calling create_ticket()
    ticket_data = create_ticket()
    
    # Display the created ticket
    if ticket_data:
        display_ticket(ticket_data)

if __name__ == "__main__":
    main()