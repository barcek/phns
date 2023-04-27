#!/usr/bin/sh

introduce() {
  echo "[$0] Running $1..."
}

introduce "static type check (via Mypy external library)"
mypy phns/

introduce "docstring interactive examples (via standard library doctest module)"
python3 -m doctest phns/*.py

introduce "test cases (via standard library unittest module)"
python3 -m unittest --quiet test/*.py
