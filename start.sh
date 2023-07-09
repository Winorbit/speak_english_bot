#!/bin/bash
if [ "$1" == "stage" ]; then
    export $(grep -v '^#' .env_stage | xargs)
elif [ "$1" == "dev" ]; then
    export $(grep -v '^#' .env_dev | xargs)
elif [ "$1" == "prod" ]; then
    export $(grep -v '^#' .env_prod | xargs)

else
    echo "Invalid environment specified. Usage: ./start.sh <stage|dev|data> <action_type> <table_name>"
    exit 1
fi

# $2=input_message

python3 run.py "$2"
