#!/usr/bin/env bash

set -e

PROJECT_BASE_PATH='/home/ilias/triply_project'

git pull
$PROJECT_BASE_PATH/env/bin/python manage.py migrate
$PROJECT_BASE_PATH/env/bin/python manage.py collectstatic --noinput
supervisorctl restart trips_api

echo "DONE! :)"
