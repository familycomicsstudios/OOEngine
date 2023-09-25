#!/bin/bash
python3 -m black __main__.py
python3 -m black commands.py
python3 -m black main.py
python3 -m black usernamelib.py
# python3 -m pylint __main__.py
# python3 -m pylint commands.py
# python3 -m pylint main.py