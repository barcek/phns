#!/usr/bin/python3

import phns
import test

from pkgutil import iter_modules
from importlib import import_module

from mypy import api
from doctest import testmod
from unittest import main

# utility functions

def log(message):
  print(f'[{__file__}] {message}')

def introduce(task):
  log(f'Running {task}...')

def submodules_list(module):
  return [module.name for module in iter_modules(module.__path__)]

def submodule_yield(module):
  for module_name in submodules_list(module):
    yield import_module(f'{module.__name__}.{module_name}')

# verification

introduce('static type check (via Mypy external library)')
print(api.run(['phns/'])[0], end='')

introduce('docstring interactive examples (via standard library doctest module)')
for module in submodule_yield(phns):
  testmod(module)

introduce('test cases (via standard library unittest module)')
for module_name in submodules_list(test):
  log(f"... for '{module_name.split('_')[1]}'...")
  main(module=f'test.{module_name}', verbosity=0, exit=False)
