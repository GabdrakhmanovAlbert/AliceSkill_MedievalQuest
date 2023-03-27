# import json
from functools import reduce
import random 

user_name = None
ss_fingers = random.randint(2, 36)
if ss_fingers == 10:
    ss_fingers += random.randint(1, 26)
# story_index = 0


def task1(event):
    ...


def task2(event):
    ...


def task3(event):
    ...


def task4(event):
    ...


def get_name(event):
    '''Get name from user'''
    names, resp_text = [], ''
    if event['request']['command'] or event['request']['original_utterance']:
        for ent in event['request']['nlu']['entities']:
            if ent['type'] == 'YANDEX.FIO':
                names += [ent['value']]
        if not names:
            resp_text = 'Друг, я не разобрала здесь твоего имени'
            extra = 0
        else:
            if len(names) > 1:
                resp_text = 'Будем считать, что остальных имён я не слышала. Возьму первое сказанное вами имя!'
            else:
                resp_text = story[1]
            user_name = names[0]
            user_name['full_name'] = _concat_name(user_name)
            
            extra = 2
    else:
        resp_text = 'Приветствую, друг!\nНазови пожалуйста своё имя:'
        extra = 0
    return (resp_text, extra)


story = [
    get_name,
    '''Приветствую тебя, юный искатель приключений! Давай перенесёмся в средневековье.
Вы находитесь на службе в замке короля Дроздоборода. Вы - храбрый рыцарь по имени {name}, предводитель армии. Сегодня король назначил вас дозорным, ваша задача вовремя уведомить короля о надвигающихся вражеских войсках.''',
    '''Вы поднялись на самую верхушку дозорной башни. Тут вы можете наблюдать все окрестные границы и с лёгкостью заметить неприятельские войска.
К тому же оказалось, что сегодня вы дежурите не один. В дозорной знакомый всему королевству человек. Это Витя, у него {rand_num} пальцев, и он очень дальнозоркий и потому Дроздобород часто отправляет его в дозор.''',
    '''Вы улыбнулись ему и захотели поздороваться, когда вдруг заметили его напряжённое лицо. Если Витя сосредотачивал взгляд вдалеке, это могло означать лишь одно - он заметил неприятеля.''',
    '''Благородный рыцарь, срочно передай королю, что я заметил на горизонте <a> кавалерийцев, <b> лучников и <c> магов.''',
    '''Вопрос к тебе, храбрый рыцарь. Сколько воинов каждого типа увидел Витя?''',
    task1,
    '''Вы прибегаете к королю. Восстановите пробелы в речи героя (Использовать цифры нельзя, числительные прописываются в соответствующих падежах).''',
    task2,
    '''"Видимо пора применить совет моей покойной пра-прабабушки" - с хмурым видом сказал Дроздобород - "Слушай меня, верный рыцарь. Собери кавалерийцев, в количестве среднее геометрического между вражескими магами и лучниками, магов, в количестве 250 промилле от количества всех врагов, и лучников, как среднее арифметическое между каждым вражеским типом войск и каждым союзным типом войск."''',
    '''Рассчитайте и введите количество кавалерийцев, лучников и магов через пробел.''',
    task3,
    ''' Итак, вы собрали войско по инструкциям Дроздоборода. Теперь вам, как командиру армии, следует провести для своих подчинённых напутственную речь.''',
    task4,
    '''И вот наконец, начинается ожесточённый бой'''
]


def _get_capitalise(names: dict, s: str) -> str:
    return names.get(s, '').capitalize()


def _concat_name(names):
    return reduce(lambda x, y: _get_capitalise(names, x) + _get_capitalise(names, y), ['last_name', 'first_name', 'patronic_name'])


def main(event, context):
    '''Точка входа'''
    # здесь можем также реализовать выбор сложности (также как с именем)
    global user_name, story, ss_fingers

    resp_dict =  {
        'version': event['version'],
        'session': event['session'],
        'response': {
            'text': '',
            'end_session': False
        },
        'session_state': {
            'story_index': 0,
        }
    }

    if event['state']['session'].get('story_index'):
        resp_dict['session_state']['story_index'] = event['state']['session']['story_index']

    obj = story[resp_dict['session_state']['story_index']]
    if hasattr(obj, '__call__'):
        resp_dict['response']['text'], extra = obj(event)
    else:
        resp_dict['response']['text'] = obj.format(name=user_name['full_name'], rand_num=ss_fingers)
        extra = 1
    
    resp_dict['session_state']['story_index'] += extra

    return resp_dict


