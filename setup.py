from setuptools import find_packages, setup

setup(
    name='carelib',
    packages=find_packages(include=['carelib']),
    version='0.1.0',
    description='Caresept: A library for AI-related tasks',
    author='Caresept',
#    author_email='', 
#    url='', 
#    license='', 
#    python_requires='>=3.6', 
    install_requires=[
        # Add dependencies
    ],
    tests_require=['unittest'],
    test_suite='tests',
)