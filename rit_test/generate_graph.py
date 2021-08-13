import os
import seaborn as sns

from data import get_data
from get_hourcost import get_hourcost
from get_profitability import get_projects

def generate_graph():
    projects = get_projects()
    _, data_b, _ = get_data()
    hourcost = get_hourcost()
    projects = projects.merge(data_b, on=['Task', 'Task'], how='left')
    projects = projects.merge(hourcost.filter(['Task', 'Hours'], axis=1), on=['Task', 'Task'], how='left')
    sns.set(rc={'figure.figsize': (30, 20)})
    g = sns.lineplot(x="Task", y='Hours', data=projects, marker='o', color='b')
    g = sns.lineplot(x="Task", y='Grade', data=projects, marker='o', color='r')
    g.set(title='Потраченное время на задачи', xlabel='Задача', ylabel='Фактическое (синие) и оцененное (красное)')
    g.figure.savefig(os.path.join('graph', 'get_hourcost.png'))
    print("График хранится в папке graph в корневой директории проекта")

if __name__ == '__main__':
    generate_graph()