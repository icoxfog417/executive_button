#!/usr/bin/env bash

set -o errexit

echo "Making staticfiles"
python manage.py collectstatic --noinput

echo "Initializing database"
python manage.py migrate

if [[ -n "${ADMIN_USERNAME}" ]] && [[ -n "${ADMIN_PASSWORD}" ]] && [[ -n "${ADMIN_EMAIL}" ]]; then
  python manage.py create_admin \
    --username "${ADMIN_USERNAME}" \
    --password "${ADMIN_PASSWORD}" \
    --email "${ADMIN_EMAIL}" \
    --noinput \
  || true
fi

echo "Starting django"
gunicorn --bind 0.0.0.0:8000 backend.wsgi --timeout 300
