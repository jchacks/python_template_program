# Default Python Project

If you know what you are doing delete this README and replace with your project else read on.
If you are building an application using a `src` folder then this is suitable for you. Otherwise there is a separate structure for building modules. (setup.py etc...) and you need a slightly different setup.

## Getting started

### Installation

```zsh
➜ git clone https://github.com/jchacks/python_template_program.git project-name
➜ cd project-name
➜ git remote remove origin
```

### Environment

Recently I converted to (mini)conda for managing my python environments.  The long and short of it is that it combines the goodness of pyenv with pip and venv all in one.  If you are used to `requirements.txt` then `environment.yml` is your new friend.  Take a look at the snippet below:

```yaml
# environment.yml
name: myproject # <- 1) change this 
channels:
  - conda-forge
dependencies:
  # conda dependencies
  - python=3.8  # <- 2) change this 
  - dotenv      # <- 3) add dependencies here 
  - numpy
  - pandas
  - requests
  - pip
  - pip:         
    # pip dependencies
    - some-pip-dependency # <- 4) add pip only dependencies here
```

This is `environment.yml` file that is included by default, you wil need to edit it a little:
  1) Choose a name for your environment and replace it
  2) Edit it to contain your desired python version for example `python=3.8`
  3) Add any dependancies available on conda
  4) If the dependancy is not available on conda you will need to add pip as a dependancy and then the pip packages below 


### Default Python code

Included is a default `config.py` file that I find myself using on all my projects.

#### Environment Variables

In my projects I often have variables that are "secret" and those that are configurable during a project and are better stored in an `.env` file.
This code snippet shows how to load these variables and set them as global variables inside the python module.

```python
import os
...
from dotenv import load_dotenv

# Find the directory one up relative to this file
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Load .envs
load_dotenv(f"{PROJECT_ROOT}/.env", verbose=True)
load_dotenv(f"{PROJECT_ROOT}/secret.env", verbose=True)

#! Put any env vars loaded from dot env here e.g.

API_KEY = os.environ['API_KEY']
```

This would load the `API_KEY` variable from a `secret.env` file that looked like this.
```bash
export API_KEY=123supersecret
```
It would then be accessible in python by using:

```python
from config import API_KEY

# Show that the variable is accessible
print('Shhhh 🤫 this is my key', API_KEY)
```

#### Unimportant Logging Detour

The other parts of the `config.py` file are to do with logging.  For progress bars in python I use the `tqdm` package.  However normal logging/printing do not play nicely with tqdm.  In order to smooth out the kinks I redirect the logging output through the `tqdm.write` method and package it up nicely in a logging handler `TqdmLoggingHandler`.  Is used by default in the `make_logger` function.  All that you need to worry about is using the `make_logger` function.

When using logging in a module that should not be run it is good to define loggers like `logger = logging.getLogger(__name__)`.
```python
# some_module 
import logging

logger = logging.getLogger(__name__)

def useful_func(arg):
    logger.info(f"Hello {arg}!")

```

and then in a main program that is expected to be invoked `python3 some_program.py` you create the root logger using `make_logger`.
```python
# some_program
from config import make_logger
from some_module import useful_func

logger = make_logger()


if __name__ == '__main__':
    logger.info("This is from my logger")
    useful_func("world")

```



## VSCode

There are a few settings suggested for ease of development using VSCode.
* The python extension is suggested as it offers completion and linting.
* Creating/editing your `.vscode/settings.json` int the project root to contain theses two settings is suggested.

```json
// .vscode/settings.json
{
    "python.pythonPath": "~/miniconda3/envs/myproject/bin/python",
    "terminal.integrated.env.linux": {
        "PYTHONPATH": "./src"
    }
}
```

* The `"python.pythonPath"` setting should be set to the default python interpreter that you want to use for this project.  If you have a custom environment.yml for conda that defines an environment replace it with the path to that python. e.g. myproject above.
* Setting `terminal.integrated.env.linux` to be the `./src` directory enables linting and running of python code to find any modules stored in that directory.  Especially useful if you have any sibling modules that need importing.
