#!/bin/bash

export $(grep -v '^#' .env_dev| xargs)

python test_rec.py
