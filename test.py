import os

print('\nRunning type check...\n')
os.system('mypy phns/')

print('\nRunning unit tests...\n')
os.system('python3 -m unittest discover test')
