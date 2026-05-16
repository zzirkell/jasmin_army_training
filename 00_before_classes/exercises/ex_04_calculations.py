def main():
    coffee_price = 2.55
    number_of_coffees = 8
    cake_price = 5.30
    number_of_cakes = 3

    coffee_total = coffee_price * number_of_coffees
    cake_total = round(cake_price * number_of_cakes, 1)
    full_total = coffee_total + cake_total
    full_total_with_tax = full_total * 1.2

    print(f"Coffee total: {coffee_total}\nCake total: {cake_total}\nFull total: {full_total}")
    pass

if __name__ == "__main__":
    main()
