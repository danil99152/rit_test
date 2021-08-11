import os

from main import get_projects
import seaborn as sns

def generate_graph():
    projects = get_projects()
    timecost = projects.copy()
    timecost['Task'] = timecost['Task']
    g = sns.lineplot(x="Task", y='Hours', data=timecost, marker='o', color='b')
    g = sns.lineplot(x="Task", y='Grade', data=timecost, marker='o', color='r')
    g.set(title='Потраченное время на задачи', xlabel='Задача', ylabel='Фактическое (синие) и оцененное (красное)')
    sns.set(rc={'figure.figsize': (30, 20)})
    g.figure.savefig(os.path.join('graph','get_hourcost.png'))

if __name__ == '__main__':
    generate_graph()