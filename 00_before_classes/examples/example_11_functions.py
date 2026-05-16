def calculate_ticket_total(ticket_price, number_of_tickets):
    return ticket_price * number_of_tickets


def is_expensive(total_price):
    return total_price > 50


def create_ticket_summary(event_name, number_of_tickets, total_price):
    return f"{number_of_tickets} tickets for {event_name} cost {total_price} euros."


def main():
    event_name = "Python Workshop"
    number_of_tickets = 3
    ticket_price = 12.50

    total = calculate_ticket_total(ticket_price, number_of_tickets)
    summary = create_ticket_summary(event_name, number_of_tickets, total)
    expensive = is_expensive(total)

    print(summary)
    print("Expensive:", expensive)


if __name__ == "__main__":
    main()
