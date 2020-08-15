#!/bin/bash

export PYTHONPATH="${PWD}/app"

# # Clean the old versions
# rm -r migrations/versions/*
# docker-compose exec postgres psql -U postgres -c "DROP TABLE IF EXISTS alembic_version;"

# Run the migration
poetry run alembic revision --autogenerate --head head
poetry run alembic upgrade head