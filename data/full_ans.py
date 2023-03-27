import sqlalchemy
from data.db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin

''' ответы, для которых нет вариантов выбора
    они заполняются сразу (не юзером), как только сгенерировались сс и a, b, c
    
    потом, когда юзер отвечает на вопрос, предполагающий полный ответ, по номеру вопроса
    и id юзера вытаскивается объект FullAns и сравнивается full_ans.ans и ответ пользователя'''


class FullAns(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'full_ans'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    num = sqlalchemy.Column(sqlalchemy.Integer)  # номер вопроса предполагающего полный ответ
    ans = sqlalchemy.Column(sqlalchemy.String)  # сам ответ
    user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("user.id"))
