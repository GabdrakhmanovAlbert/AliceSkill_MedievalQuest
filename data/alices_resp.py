import sqlalchemy
from data.db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin


class AlicesResp(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'alices_resp'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    text = sqlalchemy.Column(sqlalchemy.Text, nullable=True)  # что говорит алиса

    full_ans_num = sqlalchemy.Column(sqlalchemy.Integer, default=0)
    '''если здесь 0,
    то вопрос требует ВЫБРАТЬ вариант ответа, значит ответ пользователя сравниваем
    с choice_ans.ans где choice_ans.resp_id == alices_resp.id, иначе здесь номер вопроса где пользователь
    сам как то генерирует ответ - такие ответы сравниваются с full_ans.ans где full_ans.user_id == id
    пользователя от которого ответ пришёл и где full_ans.num == alices_resp.full_ans_num
    '''
    next_resp_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    ''' если ответ 
    не выбранный то смотрим здесь какую алисе реплику выдавать следующей'''
