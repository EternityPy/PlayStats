import os
from setuptools import find_packages, setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='playstats',
    version='0.2.1',
    packages=find_packages(),
    include_package_data=True,
    license='BSD License',
    description='A python package to fetch statistics of apps on Google Play such as ratings, downloads and much more.',
    long_description='A python package to fetch statistics of apps on Google Play such as ratings, downloads and much more.',
    url='https://github.com/EternityPy/PlayStats',
    author='Apoorva Pandey',
    author_email='apoorvaeternity@gmail.com',
    python_requires='>=3',
    install_requires=['lxml', 'cssselect'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
