from setuptools import setup, find_packages

setup(
    name='events',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'kafka-python',
        'metrics @ git+https://github.com/BobryTeam/metrics.git@pip-deps',
        'trend_data @ git+https://github.com/BobryTeam/trend-data.git@pip-deps',
        'scale_data @ git+https://github.com/BobryTeam/scale-data.git@pip-deps',
    ],
    author='BobryTeam',
    author_email='sinntexxx@gmail.com',
    description='Events and KafkaEvent* classes',
    url='https://github.com/BobryTeam/scale-data',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)
