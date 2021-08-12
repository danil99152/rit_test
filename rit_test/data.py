import pandas as pd
import os

def get_data():
    path = 'C:/Users/danil99152/Downloads/Тестовое для РИТ/'
    data_a = pd.read_table(os.path.join(path, 'Приложение А')).rename(
        columns={"Дата": "Date", "Исполнитель": "Worker", "Задача": "Task", "Часы": "Hours"})
    data_a['Date'] = pd.to_datetime(data_a['Date'], infer_datetime_format=True, format="%Y-%m-%d", errors='coerce')
    data_b = pd.read_table(os.path.join(path, 'Приложение B')).rename(columns={"Задача": "Task", "Оценка": "Grade"})
    data_c = pd.read_table(os.path.join(path, 'Приложение C')).rename(columns={"Исполнитель": "Worker", "Ставка": "Rate"})
    return data_a, data_b, data_c


if __name__ == '__main__':
    get_data()
"""# Анализ

## Общие трудозатраты на проект в часах
"""
# def hourcost():
#     data_a,_,_ = get_data()
#     hourcost = pd.DataFrame(data={'Task': [], 'Hours': []})
#     for project in data_a['Task'].unique():
#         task = data_a[data_a['Task'] == project]['Task']
#         hours = data_a[data_a['Task'] == project]['Hours'].sum()
#         return hourcost.append({'Task': task.values[0], 'Hours': hours}, ignore_index=True)
#
# """## Среднее время, затраченное на решение задач каждым из исполнителей в часах"""
#
# def get_hourcost_by_man():
#     data_a,_,data_c = get_data()
#     hourcost_by_man = pd.DataFrame(data={'Worker': [], 'Hours': [], 'Mean time': []})
#     for project in data_a['Worker'].unique():
#         task = data_a[data_a['Worker'] == project]['Worker']
#         hours = data_a[data_a['Worker'] == project]['Hours'].sum()
#         mean_hours = hours / len(data_a[data_a['Worker'] == project]['Hours'])
#         hourcost_by_man = hourcost_by_man.append({'Worker': task.values[0], 'Hours': hours, 'Mean time': mean_hours},
#                                                  ignore_index=True)
#         hourcost_by_man = hourcost_by_man.merge(data_c, on=['Worker', 'Worker'], how='left')
#         hourcost_by_man['Salary'] = hourcost_by_man['Hours'] * hourcost_by_man['Rate']
#         return hourcost_by_man
#
# """## Рентабельность"""

def profitability():
    data_a,_,_ = get_data()
    data_a = data_a.merge(get_hourcost_by_man().filter(['Worker', 'Rate'], axis=1), on=['Worker', 'Worker'], how='left')
    data_a['Cost'] = data_a['Hours'] * data_a['Rate']
    data_a = data_a.drop(['Rate'], axis=1)
    projects = pd.DataFrame(data={'Task': [], 'Cost': []})
    for project in data_a['Task'].unique():
        task = data_a[data_a['Task'] == project]['Task']
        cost = data_a[data_a['Task'] == project]['Cost'].sum()
        projects = projects.append({'Task': task.values[0], 'Cost': cost}, ignore_index=True)
    income = 24000
    profit = income - projects['Cost'].sum()
    prof = (profit * 100) / income
    return prof, projects

def get_projects():
    _,data_b,_ = get_data()
    _, projects = profitability()
    projects = projects.merge(hourcost().filter(['Task', 'Hours'], axis=1), on=['Task', 'Task'], how='left')
    projects = projects.merge(data_b, on=['Task', 'Task'], how='left')
    return projects

"""## Рассчитать среднее количество часов, отрабатываемое каждым сотрудником за день"""


def getDayofWeek(date):
    return date.dayofweek

def get_dates():
    data_a,_,_ = get_data()
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

def mean_worktime():
    dates = get_dates()
    hourcost_by_man = get_hourcost_by_man()
    average_worker_time_list = []
    for worker in hourcost_by_man['Worker']:
        average_worker_time = dates[dates['Worker'] == worker]['Hours'].sum() / len(
            dates[dates['Worker'] == worker]['Hours'])
        average_worker_time_list.append(average_worker_time)
    hourcost_by_man['Mean worktime'] = average_worker_time_list

    return hourcost_by_man.filter(['Worker', 'Mean worktime'],axis=1)

"""## Рассчитать средний «вылет» специалиста из оценки в процентах

Как я понял задачу "Вылет": найти отношение разности времени от оценки к оценке
"""
def late():
    data_a,data_b,_ = get_data()
    hourcost_by_man = get_hourcost_by_man()
    grade = data_a.drop(['Date', 'Cost'], axis=1)
    hours_list = []
    for worker, task in zip(grade['Worker'], grade['Task']):
        hours = grade[(grade['Worker'] == worker) & (grade['Task'] == task)]['Hours']
        hours_list.append(hours.sum())
    grade['Hours'] = hours_list

    grade = grade.drop_duplicates()
    grade = grade.reset_index(drop=True)
    grade = grade.merge(data_b, how='left', on=['Task', 'Task'])
    grade['Mean late'] = (grade['Hours'] - grade['Grade']) / grade['Grade'] * 100  # Средний "вылет"

    mean_worker_late_list = []
    for worker in hourcost_by_man['Worker']:
        grades = grade[grade['Worker'] == worker]['Mean late']
        mean_worker_late_list.append(grades.sum() / len(grades))
    hourcost_by_man['Mean worker late'] = mean_worker_late_list

    return hourcost_by_man.filter(['Worker','Mean worker late'], axis=1)