from database.base.session import session
from database.base.models import User
from database.base.query import Query


def get_user_by_id_query(id_: int) -> Query:
    bound_params = {
        'id': id_
    }

    query = Query(
        '''
        SELECT id FROM user WHERE id=:id;
        ''',
        bound_params,
    )

    return query


def get_user_by_id(user_id: int) -> None | User:
    q = get_user_by_id_query(user_id)
    with session() as s:
        r = s.execute(q).fetchone()
        if r:
            return User(*r)


