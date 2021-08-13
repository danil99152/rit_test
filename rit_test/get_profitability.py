import pandas as pd
from data import get_data
from get_hourcost_by_man import get_hourcost_by_man

def get_new_data_a():
    data_a, _, _ = get_data()
    data_a = data_a.merge(get_hourcost_by_man().filter(['Worker', 'Rate'], axis=1), on=['Worker', 'Worker'], how='left')
    data_a['Cost'] = data_a['Hours'] * data_a['Rate']
    data_a = data_a.drop(['Rate'], axis=1)
    return data_a

def get_projects():
    data_a = get_new_data_a()
    projects = pd.DataFrame(data={'Task': [], 'Cost': []})
    for project in data_a['Task'].unique():
        task = data_a[data_a['Task'] == project]['Task']
        cost = data_a[data_a['Task'] == project]['Cost'].sum()
        projects = projects.append({'Task': task.values[0], 'Cost': cost}, ignore_index=True)
    return projects

def get_profitability():
    projects = get_projects()
    income = 24000
    profit = income - projects['Cost'].sum()
    profitability = (profit * 100) / income
    print("Рентабельность проекта =", profitability)

if __name__ == '__main__':
    get_profitability()