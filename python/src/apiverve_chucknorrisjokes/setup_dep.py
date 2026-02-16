from setuptools import setup, find_packages

setup(
    name='apiverve_chucknorrisjokes',
    version='1.1.14',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests',
        'setuptools'
    ],
    description='Chuck Norris Jokes is a simple tool for getting Chuck Norris jokes. It returns a random Chuck Norris joke.',
    author='APIVerve',
    author_email='hello@apiverve.com',
    url='https://apiverve.com/marketplace/chucknorris?utm_source=pypi&utm_medium=homepage',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
