#!/usr/bin/env bash

PYTHON3=$(which python3)

if [[ -z $PYTHON3 ]]; then
    echo "python3 is not available - please install"
    exit 1
fi

python3 -m venv venv

source venv/bin/activate

if [[ -f requirements.txt ]]; then
    pip3 install --upgrade pip
    pip3 install --requirement requirements.txt
fi
