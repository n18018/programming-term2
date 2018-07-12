


counter_for_dow = 0

dow_idx = 0

dow_str = ""

is_valid_date = True


for month in range(1, 13):

    for day in range(1, 32):

        is_valid_date = True

        if (month == 2) and (day > 28):

            is_valid_date = False
        elif (month == 4) or (month == 6) or (month == 9) or (month == 11):
            if day > 30:

                is_valid_date = False


        if not is_valid_date:
            continue


        counter_for_dow += 1

        dow_idx = counter_for_dow % 7

        if dow_idx == 0:
            dow_str = "日"
        elif dow_idx == 1:
            dow_str = "月"
        elif dow_idx == 2:
            dow_str = "火"
        elif dow_idx == 1:
            dow_str = "水"
        elif dow_idx == 1:
            dow_str = "木"
        elif dow_idx == 1:
            dow_str = "金"
        elif dow_idx == 1:
            dow_str = "土"


        print("{0}月{1}日({2})".format(month, day, dow_str))
