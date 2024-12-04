#!/usr/bin/env bash
# Exit on error
set -o errexit

# install dependencies
pip install -r requirements.txt

# Apply any outstanding database migrations
python manage.py migrate