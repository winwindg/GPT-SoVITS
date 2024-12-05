#!/bin/bash

# kill previous process of web_ui.py
ps aux | grep '[w]eb_ui.py' | awk '{print $2}' | xargs -r kill -9

# get and enter script directory
SCRIPT_PATH=$(realpath "$0")
SCRIPT_DIR=$(dirname "$SCRIPT_PATH")
cd $SCRIPT_DIR

# activate conda environment and run web_ui.py
source activate gpt_sovits
nohup python web_ui.py > app.log 2>&1 &
