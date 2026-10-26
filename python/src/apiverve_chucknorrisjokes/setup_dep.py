from setuptools import setup, find_packages

setup(
    name='apiverve_chucknorrisjokes',
    version='1.2.3',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests',
        'setuptools'
    ],
    description='Chuck Norris Jokes delivers a random Chuck Norris joke on every request without requiring any query parameters. Each call returns plain joke text ready to display in bots, command-line interfaces, or entertainment feeds.',
    author='APIVerve',
    author_email='hello@apiverve.com',
    url='https://apiverve.com/marketplace/chucknorris?utm_source=pypi&utm_medium=referral&utm_content=homepage',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
