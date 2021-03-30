# backend
## steps to run

On terminal/cmd
* Ensure python 3.9 64 bit and pip is installed
* Install virtualenv `pip install virtualenv`
* cd into __backend__ folder
* run `python -m venv venv`
* activate virtual environment
  * __Windows__
    If activating from bash(default vscode terminal), you'll first have to enter Command Prompt mode by entering: `cmd`,
    then type `venv\Scripts\activate`. Otherwise if you're already using Command Prompt, just directly type in `venv\Scripts\activate`.
  * __Linux__ - `source /venv/bin/activate`
* run backend `python run.py`

# Docker
If you want to use docker this is how.
* `docker build -t backend .`
* `docker run -p 5000:5000 --name backend backend`

# Bash
If you want to use bash script to launch project
* cd into root directory
* run `bash build.sh`