from setuptools import setup

with open('README.md', 'r') as file:
    long_description = file.read()

setup(
    name='area_of_a_regular_polygon',
    version='1.1',
    description='To calculate the area of regular polygons either by using the length of one of its side or radius or apothem',
    long_description=long_description,
    long_description_content_type='text/markdown',
    py_modules=['validate_mail'],
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",

        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    url='https://github.com/Akshaya2411/area_of_a_regular_polygon.git',
    author='AKSHAYA G S',
    author_email='karthikgs1405@gmail.com'
)