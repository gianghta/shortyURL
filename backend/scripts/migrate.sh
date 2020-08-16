#!/bin/bash

export PYTHONPATH=.

# Run the migration
docker-compose exec backend alembic revision --autogenerate --head head
docker-compose exec backend alembic upgrade head