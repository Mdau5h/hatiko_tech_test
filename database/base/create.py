from database.base.session import session
from database.base.query import Query

create_user_table = '''
    CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY
    );
'''


def rollout():
    with session() as s:
        s.execute(Query(create_user_table))
