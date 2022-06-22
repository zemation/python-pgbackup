from setuptools import find_packages, setup

with open('README', 'r') as f:
    long_description = f.read()


setup(
    name='pgbackup',
    version='0.1.0',
    author='R Rodgers',
    author_email='robert.rodgers@acloudengineer.com',
    description='A utility for backing up Postgres databasees.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/acloudengineer/python-pgbackup',
    packages=find__packages('src')
)