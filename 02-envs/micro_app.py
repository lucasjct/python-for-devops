import sys 
# sys.path has been manipulated before to run this script.
# this solution is not recommendedm te correct approach is use virtualenvs
sys.path.insert(0, "custom")

import custom 
print(custom.VERSION)


# Virtualenvs

# python -m venv .venv
# .venv is the name recommended by the python community.


# How to activate the virtualenv

# source .vevn/bin/activate  # Linux
# .venv\Scripts\activate    # Windows   


# When the venv is activated, the script activate changes the PATH variable.
# will set end export the PYTHONHOME


# How to ensure the you are install the packages in virtualenv (use -m)
# python -m pip install requests
# python -m pip list


# Hot to leave the virtualenv
# deactivate

# the common issues with virtualenvs
# 1. you forget to activate the virtualenv
# 2. Install the wrong package (global x virtual)
# 3. Manage multiple virtualenvs.
# 4. Ensure the correct python version is used in the virtualenv.




# THE SOLUTION IS USE TOOL LIKE UV 
# https://pypi.org/project/uv/

