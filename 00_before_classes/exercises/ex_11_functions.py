def calculate_total_price(price, quantity):
    return price * quantity
    pass


def is_passing_grade(grade):
    if grade >= 50:
        return True
    else:
        return False
    pass


def create_order_summary(customer_name, product_name, quantity, total_price):
    return f"{customer_name} ordered {quantity} x {product_name} for {total_price} euros."
    pass

def main():
    customer_name = "Sofia"
    product_name = "Notebook"
    quantity = 3
    price = 4.99
    grade = 76

    total_price = calculate_total_price(price, quantity)
    is_passing = is_passing_grade(grade)
    order_summary = create_order_summary(customer_name, product_name, quantity, total_price)

    print(order_summary)
    print(f"Passing grade: {is_passing}")
    pass


if __name__ == "__main__":
    main()
