import sqlite3
import os
from pathlib import Path
from config import config
from database.base.query import Query


class session:
    def __init__(self, db_name: str = None) -> None:
        root_path = Path(__file__).resolve().parents[2]
        self.db_name = os.path.join(root_path, db_name or config.DB_NAME + '.db')
        self.connection = sqlite3.connect(self.db_name)

    def execute(self, query: Query, commit: bool = False) -> sqlite3.Cursor:
        if self.connection is None:
            self.connection = sqlite3.connect(self.db_name)

        cursor = self.connection.cursor()

        if query.params:
            result = cursor.execute(query.raw_sql, query.params)
        else:
            result = cursor.execute(query.raw_sql)

        if commit:
            self.commit()
            return result

        return result

    def commit(self) -> None:
        self.connection.commit()
        self.close_connection()

    def close_connection(self):
        self.connection.close()
        self.connection = None

    def rollback(self) -> None:
        self.connection.rollback()
        self.close_connection()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.rollback()
            return

        self.commit()
