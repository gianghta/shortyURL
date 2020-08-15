#!/bin/bash

set -e

poetry export -f requirements.txt --without-hashes > requirements/main.txt