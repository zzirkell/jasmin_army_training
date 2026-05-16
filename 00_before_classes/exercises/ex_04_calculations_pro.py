"""
Exercise 13: Calculations Pro. SOLVE CALCULATIONS.py FIRST!

Goal:
Practice more useful math operators and built-in math-related functions.

You will practice:
- normal division /
- integer division //
- modulo %
- round()
- abs()
- min()
- max()
- sum()
- pow()

Run this file with:

    python ex_13_calculations_pro.py
"""


def main():
    print("Exercise 13: Calculations Pro")
    print("-----------------------------")

    total_items = 23
    box_size = 5

    exact_boxes = total_items / box_size

    full_boxes = total_items // box_size

    items_left = total_items % box_size

    print(f"Exact boxes: {exact_boxes}\nFull boxes: {full_boxes}\nItems left: {items_left}\n")

    tempertaure = -7
    print("Temperature distance from zero:", abs(tempertaure))

    prices = [12.99, 5.50, 3.25, 20.00]
    print("\nCheapest price:", min(prices))
    print("Most expensive price:", max(prices))
    print("Total price:", sum(prices))

    print("Rounded total price:", round(sum(prices), 1))

    result = pow(2, 3)
    print("\n", result)

    original_price = 80
    discount_percent = 15
    discount_amount = original_price * discount_percent / 100
    final_price = original_price - discount_amount
    print("\nDiscount amount:", discount_amount)
    print("Final price:", final_price)

    pass


if __name__ == "__main__":
    main()