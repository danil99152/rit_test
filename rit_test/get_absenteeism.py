from get_time_by_day import get_dates


def get_absenteeism():
    dates = get_dates()
    days = dates['Date'].drop_duplicates()
    for employee in dates['Worker'].unique():
        print(f"Дни отсутствия исполнителя {employee}:")
        workdays = days.isin(dates[dates['Worker'] == employee]['Date'])
        if len(workdays) == len(workdays[workdays == True]):
            print("Не имеются")
        else:
            for i in workdays[workdays == False].index:
                print(dates[dates['Day of week'] < 5]['Date'].loc[i])

if __name__ == '__main__':
    get_absenteeism()