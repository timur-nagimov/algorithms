def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def generate_dates(year, start_day):
    days = ["Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"]
    month_lengths = [31, 29 if is_leap_year(
        year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_index = days.index(start_day)
    dates = []
    for month in range(1, 13):
        for day in range(1, month_lengths[month - 1] + 1):
            dates.append(
                (days[day_index % 7], f"{year}-{month:02d}-{day:02d}"))
            day_index += 1
    return dates


def parse_holidays(holiday_list, year):
    holidays = []
    for holiday in holiday_list:
        day, month_name = holiday.split()
        month = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6,
                 "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12}[month_name]
        holidays.append(f"{year}-{month:02d}-{int(day):02d}")
    return holidays


def calculate_optimal_day_for_holiday(dates, holidays):
    day_offs = {day: 0 for day in [
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]}

    for day, date_str in dates:
        day_offs[day] += 1 if date_str not in holidays else 0

    optimal_day_offs = {
        day: 365 + is_leap_year(year) - offs for day, offs in day_offs.items()}
    best_day = max(optimal_day_offs, key=optimal_day_offs.get)
    worst_day = min(optimal_day_offs, key=optimal_day_offs.get)

    return best_day, worst_day


n = int(input())
year = int(input())
holiday_list = [input() for i in range(n)]
start_day = input()

holidays = parse_holidays(holiday_list, year)
dates = generate_dates(year, start_day)
best_day, worst_day = calculate_optimal_day_for_holiday(dates, holidays)

print(worst_day, best_day)
