#!/bin/bash

# backend
cd backend
if [ -d "venv" ]; then
source ./venv/scripts/activate
python -m pip install -r requirements.txt
else
python -m pip install venv
python -m venv venv
source ./venv/scripts/activate
python -m pip install -r requirements.txt
fi
python run.py & pids+=" $!"

trap "kill $pids" SIGTERM SIGINT

wait $pids

