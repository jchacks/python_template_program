# Default Python Project

If you know what you are doing delete this README and replace with your project else read on.
If you are building an application using a `src` folder then this is suitable for you. 
Otherwise there is a separate structure for building packages. (setup.py etc...) and you need a slightly different setup.

Inspiration is taken from the [Hitchhiker's Guide to Python - Structuring Your Project](https://docs.python-guide.org/writing/structure/).

## Getting started

### Installation

```zsh
➜ git clone https://github.com/jchacks/python_template_program.git project-name
➜ cd project-name
➜ git remote remove origin
```

### Environment

Use (mini)conda for managing python environments it combines the goodness of pyenv with pip and venv all in one.  If you are used to `requirements.txt` then [`environment.yml`](environment.yml) is your new friend.  Take a look at the snippet below:

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

This is `environment.yml` file that is included by default, you will need to edit it a little:
  1) Choose a name for your environment and replace it
  2) Edit it to contain your desired python version for example `python=3.8`
  3) Add any dependencies available on conda
  4) If the dependency is not available on conda you will need to add pip as a dependency and then the pip packages below 


### Default Python code

Included is a default [`config.py`]() file that solves a lot of issues commonly encountered in python projects.

#### Environment Variables

Projects often contain "secret" variables or variables that need to be easily configurable during a project.  These are better stored in `.env` files than in python source code.
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

The other parts of the [`config.py`](src/config.py) file are to do with logging.  The `tqdm` package offers some great progress bars that are handy for monitoring longer running tasks.  However, normal logging and printing do not play nicely with tqdm.  To fix this it is required that logging output is redirected through the `tqdm.write` method.  The [`TqdmLoggingHandler`](src/config.py#L15)  logging handler is used by default in the `make_logger` function and solves these issues.

When using the python `logging` module inside your own module you should declare your logger using `logging.getLogger(__name__)`.  This automatically records the module name making it easier to track down errors.

```python
# some_module 
import logging

logger = logging.getLogger(__name__)

def useful_func(arg):
    logger.info(f"Hello {arg}!")

```

and then in the 'main' program that is expected to be invoked you would create the root logger using `make_logger` from `config`.
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


### Footnote

All of the statements above are my opinion on a good starting point for Python projects and is open to discussion.
