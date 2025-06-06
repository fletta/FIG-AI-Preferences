"""Miscellaneous helper functions."""

import sqlite3
from pathlib import Path


DB_PATH = Path('logs/run.sqlite')


def get_connection() -> sqlite3.Connection:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    return conn
