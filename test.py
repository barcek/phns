import os

print('\nRunning type check...\n')
os.system('mypy phns/')

print('\nRunning docstring interactive examples...\n')
os.system('python3 -m doctest phns/*.py')

print('\nRunning unit tests...\n')
os.system('python3 -m unittest discover test')
