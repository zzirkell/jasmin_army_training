def main():
    is_member = True
    order_total = 35
    is_birthday = False

    free_shipping = order_total >= 50 or is_member
    bonus_gift = is_member and is_birthday

    print("Free shipping:", free_shipping)
    print("Bonus gift:", bonus_gift)

    if free_shipping:
        print("The customer gets free shipping.")
    else:
        print("The customer pays for shipping.")


if __name__ == "__main__":
    main()
