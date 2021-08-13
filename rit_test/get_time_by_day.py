from get_hourcost_by_man import get_hourcost_by_man
from get_profitability import get_new_data_a


def getDayofWeek(date):
    return date.dayofweek

def get_dates():
    data_a = get_new_data_a()
    dates = data_a.drop(['Task', 'Cost'], axis=1)
    dates = dates.sort_values('Date')
    hours_list = []
    for worker, date in zip(dates['Worker'], dates['Date']):
        hours = dates[(dates['Worker'] == worker) & (dates['Date'] == date)]['Hours']
        hours_list.append(hours.sum())
    dates['Hours'] = hours_list
    dates = dates.drop_duplicates()
    dates = dates.reset_index(drop=True)
    dates['Day of week'] = dates['Date'].apply(getDayofWeek)
    return dates

def get_time_by_day():
    print('Получение данных о том, сколько отработал каждый сотрудник в каждый из дней:')
    dates = get_dates()
    print(dates)
    print('Получение данных об средней отработке каждого сотрудника в день:')
    average_worker_time_list = []
    hourcost_by_man = get_hourcost_by_man()
    for worker in hourcost_by_man['Worker']:
        average_worker_time = dates[dates['Worker'] == worker]['Hours'].sum() / len(
            dates[dates['Worker'] == worker]['Hours'])
        average_worker_time_list.append(average_worker_time)
    hourcost_by_man['Mean worktime'] = average_worker_time_list
    print(hourcost_by_man)

if __name__ == '__main__':
    get_time_by_day()