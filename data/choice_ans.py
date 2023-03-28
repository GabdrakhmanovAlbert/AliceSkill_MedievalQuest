import sqlalchemy
from data.db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin


class ChoiceAns(SqlAlchemyBase, SerializerMixin):  # ответы которые мы сами занесли в бд, юзеру надо только выбрать
    __tablename__ = 'choice_ans'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    is_correct = sqlalchemy.Column(sqlalchemy.Boolean)  # если тру то user.score += 1
    ans = sqlalchemy.Column(sqlalchemy.String)  # сам ответ
    resp_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("alices_resp.id"))

    next_resp_id = sqlalchemy.Column(sqlalchemy.Integer,
                                     sqlalchemy.ForeignKey("alices_resp.id"))  # которую реплику дальше выдавать
