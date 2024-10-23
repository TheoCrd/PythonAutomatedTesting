from __future__ import annotations

import sys
from typing import Any

import pytest


@pytest.fixture
def capture_stdout(monkeypatch):
    buffer: dict[str, Any] = {"stdout": "", "write_calls": 0}

    def fake_write(s: str) -> None:
        buffer["stdout"] += s
        buffer["write_calls"] += 1

    monkeypatch.setattr(sys.stdout, "write", fake_write)
    return buffer


@pytest.fixture(scope="session")
def db_conn():
    db = create_db_instance()  # Replace with actual database instance creation
    url = "database_url"  # Replace with actual database URL
    with db.connect(
        url
    ) as conn:  # connection will be torn down after all tests finish
        yield conn


def create_db_instance():
    # Replace with actual database instance creation logic
    pass
