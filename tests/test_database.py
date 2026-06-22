import os
import pytest
from database import init_db, save_record, get_top_records, DB_PATH


@pytest.fixture(autouse=True)
def setup_and_teardown():
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    init_db()
    yield
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)


def test_init_db_creates_table():
    init_db()
    from database import get_connection
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='records'")
    assert cur.fetchone() is not None
    conn.close()


def test_save_record():
    save_record("testuser", 5)
    records = get_top_records(10)
    assert len(records) == 1
    assert records[0][1] == "testuser"
    assert records[0][2] == 5


def test_save_record_empty_nickname():
    save_record("", 10)
    records = get_top_records(10)
    assert len(records) == 1


def test_save_record_zero_attempts():
    save_record("pro", 0)
    records = get_top_records(10)
    assert records[0][2] == 0


def test_get_top_records_ordering():
    save_record("bad", 100)
    save_record("good", 3)
    save_record("medium", 20)
    records = get_top_records(10)
    assert len(records) == 3
    assert records[0][1] == "good"
    assert records[0][2] == 3
    assert records[1][1] == "medium"
    assert records[2][1] == "bad"


def test_get_top_records_limit():
    for i in range(20):
        save_record(f"player{i}", i)
    records = get_top_records(5)
    assert len(records) == 5


def test_get_top_records_empty():
    records = get_top_records(10)
    assert records == []


def test_multiple_saves_same_user():
    save_record("alice", 10)
    save_record("alice", 5)
    records = get_top_records(10)
    assert len(records) == 2
    assert records[0][2] == 5
