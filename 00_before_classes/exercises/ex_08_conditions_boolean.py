def main():
    is_student = True
    order_total = 25
    has_coupon = False

    discount_available = (is_student and order_total >= 20) or has_coupon
    print("Discount available:", discount_available)

    if discount_available == True:
        print("The customer receives a discount.")

    pass


if __name__ == "__main__":
    main()
