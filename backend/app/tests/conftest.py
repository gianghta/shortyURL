import os

import pytest
from starlette.testclient import TestClient

from app import main


@pytest.fixture(scope="module")
def test_app():
    # setup
    with TestClient(main.app) as test_client:

        # testing
        yield test_client

    # tear down
