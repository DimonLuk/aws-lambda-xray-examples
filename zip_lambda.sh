#!/usr/bin/bash

cd venv/lib/python3.7/site-packages
zip -r ../../../../lambda.zip .
cd ../../../../
zip -g lambda.zip lambda_function.py