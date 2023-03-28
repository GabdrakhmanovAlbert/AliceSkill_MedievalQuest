import sqlalchemy
from data.db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin


class User(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'user'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    last_resp_id = sqlalchemy.Column(sqlalchemy.Integer,
                                     sqlalchemy.ForeignKey("alices_resp.id"))  # id предшествующей реплики алисы
    system = sqlalchemy.Column(sqlalchemy.Integer)  # основание системы счисления
    a = sqlalchemy.Column(sqlalchemy.Integer)  # кавалерийцы
    b = sqlalchemy.Column(sqlalchemy.Integer)  # лучники
    c = sqlalchemy.Column(sqlalchemy.Integer)  # маги
    score = sqlalchemy.Column(sqlalchemy.Integer, default=0)
