import pytest
from sqlalchemy import create_engine


@pytest.fixture
def engine():
    return create_engine('sqlite+pysqlite:///:memory:')
