def conversion(usd):
    inr_rate = 88.05
    gbp_rate = 0.73325
    cny_rate = 7.11507

    inr = usd * inr_rate
    gbp = usd * gbp_rate
    cny = usd * cny_rate

    return inr, gbp, cny


while True:
    user_input = input("Enter dollar ($) (* to exit): ")

    if user_input.strip() == "*":
        print("Bye")
        break

    dollar_list = user_input.split("@")
    print("Dollar($)   Indian Rupee(R)   British Pound(£)   China(Y)")

    for x in dollar_list:
        x = x.strip()
        try:
            usd = float(x)
            inr, gbp, cny = conversion(usd)
            print(usd, "        ", round(inr, 2), "           ", round(gbp, 2), "             ", round(cny, 2))
        except ValueError:
            print("Invalid input:", x)
