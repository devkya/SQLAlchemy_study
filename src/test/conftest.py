import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session


@pytest.fixture
def engine():
    return create_engine('sqlite+pysqlite:///:memory:')


@pytest.fixture
def session(engine):
    with Session(engine) as session:
        yield session

@pytest.fixture
def create_xy_data(session) -> Session:
    session.execute(text("CREATE TABLE test01 (x int, y int)"))
    session.execute(text("INSERT INTO test01 (x, y) VALUES (:x, :y)"),
                    [{"x": 1, "y": 1}, {"x": 2, "y": 2}, {"x": 3, "y": 3}],
    )
