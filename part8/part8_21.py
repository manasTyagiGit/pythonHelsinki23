from datetime import date

def list_years (date_list: list) -> list :
    years = []

    for date in date_list:
        years.append(date.year)

    return sorted(years)


if __name__ == "__main__" :
    date1 = date(2019, 2, 3)
    date2 = date(2006, 10, 10)
    date3 = date(1993, 5, 9)

    years = list_years([date1, date2, date3])
    print(years)