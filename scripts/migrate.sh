#!/bin/bash

export PYTHONPATH="${PWD}/app"

# # Clean the old versions
# rm -r migrations/versions/*
# docker-compose exec postgres psql -U postgres -c "DROP TABLE IF EXISTS alembic_version;"

# Run the migration
docker-compose run alembic --rm revision --autogenerate --head head
docker-compose run alembic --rm upgrade head