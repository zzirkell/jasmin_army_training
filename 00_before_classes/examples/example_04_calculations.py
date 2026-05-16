def main():
    ticket_price = 12.50
    number_of_tickets = 3
    snack_price = 4.00
    number_of_snacks = 2

    ticket_total = ticket_price * number_of_tickets
    snack_total = snack_price * number_of_snacks
    full_total = ticket_total + snack_total

    print("Ticket total:", ticket_total)
    print("Snack total:", snack_total)
    print("Full total:", full_total)


if __name__ == "__main__":
    main()
