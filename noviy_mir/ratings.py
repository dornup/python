import gspread

gs = gspread.service_account(filename='new-world-404713-3ea0feb6f959.json')
sh = gs.open_by_key('1zAUex3RlqXE4J3ew4bZXRCOI7roWoO3Oe-iXxfIYAlU')

sheet = sh.sheet1.get_all_values()
rates = [i.replace(',', '.') for i in sh.sheet1.col_values(12)[2:]]
ns = sh.sheet1.col_values(13)[2:]


for i in range(len(ns)):

    #n = int(sh.sheet1.acell(f'M{i+1}').value)
    n = int(ns[i])
    end = 4.8
    rate = float(rates[i])
    min_sum_rates = round((rate-0.05)*n, 1)
    max_sum_rates = round((rate+0.04)*n, 1)
    max_five, min_five = 0, 0
    print(i, rate, n)

    if rate == 0.0:
        sh.sheet1.update_acell(f'P{i+3}', '1')
        continue

    while rate < end:
        if max_sum_rates/n < end:
            max_sum_rates += 5
            max_five += 1
        n += 1
        min_sum_rates += 5
        min_five += 1
        rate = round(min_sum_rates/n, 1)

    sh.sheet1.update_acell(f'P{i+3}', str(max_five))