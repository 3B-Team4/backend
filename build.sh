#!/bin/bash

if [ -d "venv" ]; then
source ./venv/bin/activate
python -m pip install -r requirements.txt
else
python -m pip install venv
python -m venv venv
source ./venv/bin/activate
python -m pip install -r requirements.txt
fi

python run.py & pids+=" $!"

trap "kill $pids" SIGTERM SIGINT

wait $pids

