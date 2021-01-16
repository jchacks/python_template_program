# Default Python Project

If you are building an application use the `src` folder.
There is a separate structure for building modules. (setup.py etc...) 

## Getting started

### Environment

Recently I converted to (mini)conda for managing my python environments.  The long and short of it is that it combines the goodness of pyenv with pip and venv all in one.  

```yaml
# environment.yml
name: myproject
channels:
  - conda-forge
dependencies:
  # conda dependencies
  - python=3.8
  - dotenv
  - numpy
  - pandas
  - requests
  - pip
  - pip:
    # pip dependencies
    - some-pip-dependency
```

Included in the project is this default `environment.yml` file.
* Edit it to contain your desired python version `python=3.8`
* Add any dependancies available on conda
* If the dependancy is not available on conda you will need to add pip as a dependancy and then the pip packages below 
```yaml
dependencies:
  ...
  - pip
  - pip:
    - some-pip-dependency
```


## VSCode

There are a few settings included for ease of development using VSCode.
The python extension is required.

```json
// .vscode/settings.json
{
    "python.pythonPath": "~/miniconda3/envs/base/bin/python",
    "terminal.integrated.env.linux": {
        "PYTHONPATH": "./src"
    }
}
```

The `"python.pythonPath"` setting should be set to the default python interpreter that you want to use for this project.  If you have a custom environment.yml for conda that defines an environment replace it with the path to that python. e.g. myproject below.

