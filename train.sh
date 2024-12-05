#!/bin/bash

# kill previous process of webui.py
ps aux | grep '[w]ebui.py' | awk '{print $2}' | xargs -r kill -9

# get and enter script directory
SCRIPT_PATH=$(realpath "$0")
SCRIPT_DIR=$(dirname "$SCRIPT_PATH")
cd $SCRIPT_DIR

# activate conda environment and run webui.py
source activate gpt_sovits
nohup python webui.py > app.log 2>&1 &
