def calculate_change(payment, cost):
    fifty_thousand = 50000
    ten_thousand = 10000
    five_thousand = 5000
    one_thousand = 1000

    change = payment - cost
    fifty_thousand_count = int(change / 50000)

    change = change % 50000
    ten_thousand_count = int(change / 10000)

    change = change % 10000
    five_thousand_count = int(change / 5000)

    change = change % 5000
    one_thousand_count = int(change / 1000)

    print("50000원 지폐: %d장" % (fifty_thousand_count))
    print("10000원 지폐: %d장" % (ten_thousand_count))
    print("5000원 지폐: %d장" % (five_thousand_count))
    print("1000원 지폐: %d장" % (one_thousand_count))


calculate_change(100000, 33000)

calculate_change(500000, 378000)
