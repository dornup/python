import gspread

gs = gspread.service_account(filename='new-world-404713-3ea0feb6f959.json')
sh = gs.open_by_key('1zAUex3RlqXE4J3ew4bZXRCOI7roWoO3Oe-iXxfIYAlU')

sheet = sh.sheet1.get_all_values()
rates = [i.replace(',', '.') for i in sh.sheet1.col_values(12)[2:]]
ns = sh.sheet1.col_values(13)[2:]
ends = [i.replace(',', '.') for i in sh.sheet1.col_values(15)[2:]]
data = sh.sheet1.col_values(19)[2:]
output_rates = []
output_datas = []


for i in range(len(ns)):
    n = int(ns[i])
    end = float(ends[i])
    rate = float(rates[i])
    min_sum_rates = round((rate-0.05)*n, 1)
    max_sum_rates = round((rate+0.04)*n, 1)
    max_five, min_five = 0, 0

    while rate < end:
        if rate == 0.0:
            max_five = 1
            break
        if max_sum_rates/n < end:
            max_sum_rates += 5
            max_five += 1
        n += 1
        min_sum_rates += 5
        min_five += 1
        rate = round(min_sum_rates/n, 1)

    output_rates.append(max_five)

    days = max_five * 3
    data_start = data[i].split('.')
    day_start = int(data_start[0].lstrip('0'))
    day_end = day_start + days
    month_end = int(data_start[1].lstrip('0'))
    year_end = int(data_start[2].lstrip('0'))

    # thirty_one = ['01', '03', '05', '07', '08', '10', '12']
    # thirty = ['04', '06', '09', '11']
    # if month_end in thirty_one:
    #     while day_end > 31:
    #         day_end -= 31
    #         month_end += 1
    #
    # elif month_end in thirty:
    #     while day_end > 30:
    #         day_end -= 30
    #         month_end += 1
    # else:
    #     while day_end > 28:
    #         day_end -= 28
    #         month_end += 1
    while day_end > 30:
        day_end -= 30
        month_end += 1

    while month_end > 12:
        month_end -= 12
        year_end += 1

    while year_end > 99:
        year_end -= 99

    day_end, month_end, year_end = str(day_end), str(month_end), str(year_end)

    if len(day_end) == 1:
        day_end = '0' + day_end

    if len(month_end) == 1:
        month_end = '0' + month_end

    if len(year_end) == 1:
        year_end = '0' + year_end

    data_end = f'{day_end}.{month_end}.{year_end}'
    output_datas.append(data_end)

for i in range(len(ns)):
    sh.sheet1.update_acell(f'T{i+3}', output_datas[i])
    sh.sheet1.update_acell(f'P{i+3}', output_rates[i])


