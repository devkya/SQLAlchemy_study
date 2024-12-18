from loguru import logger
from sqlalchemy import text


def test_connect(engine):
    with engine.connect() as conn:
        result = conn.execute(text("select 'hello world!'"))
        assert result.all()[0][0] == "hello world!"


def test_commit(engine):
    with engine.begin() as conn:
        conn.execute(text("CREATE TABLE test01 (x int, y int)"))
        conn.execute(text("INSERT INTO test01 (x, y) VALUES (:x, :y)"),
                     [{"x": 1, "y": 1}, {"x": 2, "y": 2}, {"x": 3, "y": 3}],
                     )

    with engine.begin() as conn:
        result = conn.execute(text("SELECT x, y FROM test01"))
        rows = result.fetchall()
        assert rows[0].x == 1
        assert rows[1].x == 2
        assert rows[2].x == 3

def test_session(engine):
    """
    https://docs.sqlalchemy.org/en/20/tutorial/dbapi_transactions.html
    """
    pass