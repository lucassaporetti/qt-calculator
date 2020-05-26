#!/usr/bin/env bash

CUR_DIR="$(pwd)"

export PYTHONPATH="${CUR_DIR}"

pushd src &> /dev/null || exit 1
python3 main.py
popd &> /dev/null || exit 1

exit 0
