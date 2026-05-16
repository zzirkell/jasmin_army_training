def main():
    prices = [10.0, 15.5, 4.5]

    total = 0
    for price in prices:
        print("Price:", price)
        total = total + price

    average = total / len(prices)

    print("Total price:", total)
    print("Average price:", average)


if __name__ == "__main__":
    main()
