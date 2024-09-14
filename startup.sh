#!/bin/bash

# kill previous process of api_v2.py
ps aux | grep '[a]pi_v2.py' | awk '{print $2}' | xargs -r kill -9

# get and enter script directory
SCRIPT_PATH=$(realpath "$0")
SCRIPT_DIR=$(dirname "$SCRIPT_PATH")
cd $SCRIPT_DIR

# activate conda environment and run api_v2.py
source activate gpt_sovits
nohup python api_v2.py > app.log 2>&1 &
