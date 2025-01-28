import pytest
import os


@pytest.fixture
def tests_path() -> str:
    file = os.path.abspath(__file__)
    parent = os.path.dirname(file)
    return parent


@pytest.fixture
def data_path(tests_path: str) -> str:
    return os.path.join(tests_path, "data")
