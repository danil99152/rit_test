from setuptools import setup

setup(
name='gethourcost',
    entry_points={
        'console_scripts': [
            'gethourcost = get_hourcost',
        ],
    }
)
setup(
name='gethourcostbyman',
    entry_points={
        'console_scripts': [
            'gethourcostbyman = get_hourcost_by_man',
        ],
    }
)

setup(
name='getprofability',
    entry_points={
        'console_scripts': [
            'getprofability = get_profability',
        ],
    }
)
setup(
name='gettimebyday',
    entry_points={
        'console_scripts': [
            'gettimebyday = get_time_by_day',
        ],
    }
)
setup(
name='getlazy',
    entry_points={
        'console_scripts': [
            'getlazy = get_lazy_employee',
        ],
    }
)
setup(
name='getabsenteeism',
    entry_points={
        'console_scripts': [
            'getabsenteeism = get_absenteeism',
        ],
    }
)
setup(
name='getlate',
    entry_points={
        'console_scripts': [
            'getlate = get_late',
        ],
    }
)
setup(
name='generategraph',
    entry_points={
        'console_scripts': [
            'generategraph = generate_graph',
        ],
    }
)
setup(
    name='help',
    entry_points={
        'console_scripts': [
            'help = help',
        ],
    }
)