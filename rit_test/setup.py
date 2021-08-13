from setuptools import setup

setup(
name='hourcost',
    entry_points={
        'console_scripts': [
            'hourcost = get_hourcost:print_hourcost',
        ],
    }
)
setup(
name='hourcostbyman',
    entry_points={
        'console_scripts': [
            'hourcostbyman = get_hourcost_by_man:print_hourcost_by_man',
        ],
    }
)

setup(
name='profitability',
    entry_points={
        'console_scripts': [
            'profitability = get_profitability:get_profitability',
        ],
    }
)
setup(
name='timebyday',
    entry_points={
        'console_scripts': [
            'timebyday = get_time_by_day:get_time_by_day',
        ],
    }
)
setup(
name='getlazy',
    entry_points={
        'console_scripts': [
            'getlazy = get_lazy_employee:get_lazy_employee',
        ],
    }
)
setup(
name='getabsenteeism',
    entry_points={
        'console_scripts': [
            'getabsenteeism = get_absenteeism:get_absenteeism',
        ],
    }
)
setup(
name='lates',
    entry_points={
        'console_scripts': [
            'lates = get_late:get_late',
        ],
    }
)
setup(
name='generategraph',
    entry_points={
        'console_scripts': [
            'generategraph = generate_graph:generate_graph',
        ],
    }
)
setup(
    name='pleasehelp',
    entry_points={
        'console_scripts': [
            'pleasehelp = help:help',
        ],
    }
)