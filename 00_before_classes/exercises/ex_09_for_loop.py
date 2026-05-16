#first do 9 basic!!
def main():
    expenses = [12.50, 8.99, 23.40, 5.00]
    total = 0
    for expense in expenses:
        total = total + expense
        print(f"Expense: {expense}")
    print(f"Total expenses: {total}\nAverage expense: {total/len(expenses)}")

    pass


if __name__ == "__main__":
    main()
