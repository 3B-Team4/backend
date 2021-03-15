#!/bin/bash

if [ "$(uname)" == "Darwin" ]; then
   venvLoc="./venv/bin/activate"
elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
    venvLoc="./venv/bin/activate"
elif [ "$(expr substr $(uname -s) 1 10)" == "MINGW64_NT" ]; then
    venvLoc="./venv/Scripts/activate"
fi

if [ -d "venv" ]; then
source $venvLoc
python -m pip install -r requirements.txt
else
python -m pip install venv
python -m venv venv
source $venvLoc
python -m pip install -r requirements.txt
fi

python run.py & pids+=" $!"

trap "kill $pids" SIGTERM SIGINT

wait $pids

