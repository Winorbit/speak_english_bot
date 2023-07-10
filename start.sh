#!/bin/bash

if [ "$1" == "stage" ]; then
    if [ "$(uname -s)" == "Darwin" ]; then
        export $(grep -v '^#' .env_stage | xargs)
    else
        while IFS='=' read -r key value; do
            set "$key" "$value"
            set "$1=$2"
        done < .env_stage
    fi
elif [ "$1" == "dev" ]; then
    if [ "$(uname -s)" == "Darwin" ]; then
        export $(grep -v '^#' .env_dev | xargs)
    else
        while IFS='=' read -r key value; do
            set "$key" "$value"
            set "$1=$2"
        done < .env_dev
    fi
elif [ "$1" == "prod" ]; then
    if [ "$(uname -s)" == "Darwin" ]; then
        export $(grep -v '^#' .env_prod | xargs)
    else
        while IFS='=' read -r key value; do
            set "$key" "$value"
            set "$1=$2"
        done < .env_prod
    fi
else
    echo "Invalid environment specified. Usage: ./start.sh <stage|dev|data> <action_type> <table_name>"
    exit 1
fi

# $2=input_message

python run.py "$2"

