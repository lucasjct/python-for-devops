# UV helpful to manage virtualenvs 

# How to user it:
# pip install uv

# create a virtualenv 
# uv init . --bare -> will be created a file pyroject.toml
# uv will be responsible to activated and deactivate the virtualenv.


# when you run `uv init my-aap`
# will be created the directory my-app with: main.py, project.toml and readme.md

# to add packages
# uv add requests

# to run the app
# uv run python main.py

# to remove packages
# uv remove requests

# to list packages
# uv list   

# the uv is fast 
# the are cache strategies to be faster.  

# when we finsh the project
# we don't need run deactivate like in virtualenv 

# uv is compatible with any tool that use virtualenvs


# to create a package
# uv init --package my-app

