# import json
from data.db_session import global_init
from functools import reduce
import random
from string import ascii_uppercase


def get_ss():
    '''Return number from 2 to 36, except 10'''
    ss = random.randint(2, 36)
    if ss == 10:
        ss += random.randint(1, 26)
    return ss

def from10(num, NUM_FINGERS, TRANS_D):
    res_num = ''
    while num:
        dig = num % NUM_FINGERS
        dig = str(dig) if dig < 10 else TRANS_D[dig]
        res_num = dig + res_num
        num //= NUM_FINGERS
    return res_num


if __name__ == '__main__':
    global_init("quest.db")



def task1(event):
    ...


def task2(event):
    ...


def task3(event):
    ...


def task4(event):
    ...


def get_name(event, resp):
    '''Get name from user'''
    names, resp_text, tts = [], '', ''
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
                extra = 1
            else:
                resp_text = story[1]['text']
                tts = story[1]['tts']
                extra = 2
            resp['user_state_update'] = {}
            resp['user_state_update']['user'] = names[0]
            resp['user_state_update']['user']['full_name'] = _concat_name(resp['user_state_update']['user'])
    else:
        resp_text = 'Приветствую, друг!\nНазови пожалуйста своё имя:'
        extra = 0
    return (resp_text, tts, extra)


story = [
    get_name,
    {
        'text': """f'''Приветствую тебя, юный искатель приключений! 
Давай перенесёмся в средневековье.
Вы находитесь на службе в замке короля Дроздоборода. Вы - храбрый рыцарь по имени {event['state']['user']['user']['full_name']}, предводитель армии.
Сегодня король назначил вас дозорным, ваша задача вовремя уведомить короля о надвигающихся вражеских войсках.
Вы поднялись на самую верхушку дозорной башни. Тут вы можете наблюдать все окрестные границы и с лёгкостью заметить неприятельские войска.
К тому же оказалось, что сегодня вы дежурите не один.
В дозорной знакомый всему королевству человек. Это Витя, у него {event['user']['state']['num_fingers']} пальцев, и он очень дальнозоркий и потому Дроздобород часто отправляет его в дозор.
Вы улыбнулись ему и захотели поздороваться, когда вдруг заметили его напряжённое лицо. Если Витя сосредотачивал взгляд вдалеке, это могло означать лишь одно - он заметил неприятеля.
Благородный рыцарь, срочно передай королю, что я заметил на горизонте {event['user']['state']['SS_VITYA']['cavalry']} кавалерийцев, {event['user']['state']['SS_VITYA']['archery']} лучников и {event['user']['state']['SS_VITYA']['wizard']} магов.
Вопрос к тебе, храбрый рыцарь. Сколько воинов каждого типа увидел Витя?'''""",
        'tts': """f'''Приветствую тебя, юный искатель приключений! <speaker audio="alice-sounds-human-cheer-1.opus">
Давай перенесёмся в средневековье. <speaker audio="alice-music-harp-1.opus">
Вы находитесь на службе в замке короля Дроздоборода. Вы - храбрый рыцарь по имени {event['state']['user']['user']['full_name']}, предводитель армии.
Сегодня король назначил вас дозорным, ваша задача вовремя уведомить короля о надвигающихся вражеских войсках.
Вы поднялись на самую верхушку дозорной башни. Тут вы можете наблюдать все окрестные границы и с лёгкостью заметить неприятельские войска.
К тому же оказалось, что сегодня вы дежурите не один.
В дозорной знакомый всему королевству человек. Это Витя, у него {event['user']['state']['num_fingers']} пальцев, и он очень дальнозоркий и потому Дроздобород часто отправляет его в дозор.
Вы улыбнулись ему и захотели поздороваться, когда вдруг заметили его напряжённое лицо. Если Витя сосредотачивал взгляд вдалеке, это могло означать лишь одно - он заметил неприятеля.
Благородный рыцарь, срочно передай королю, что я заметил на горизонте {event['user']['state']['SS_VITYA']['cavalry']} кавалерийцев, {event['user']['state']['SS_VITYA']['archery']} лучников и {event['user']['state']['SS_VITYA']['wizard']} магов.
Вопрос к тебе, храбрый рыцарь. Сколько воинов каждого типа увидел Витя?'''""",
    },
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
    global story

    resp =  {
        'version': event['version'],
        'session': event['session'],
        'response': {
            'text': '',
            'tts': '',
            'end_session': False,

        },
        'session_state': {
            'story_index': 0,
        }
    }

    if event['session']['new']:
        TRANS_D = {n: al for n, al in zip(range(10, 36), ascii_uppercase)}
        NUM_FINGERS = get_ss()
        CAV_ARCH_WIZ_10 = (random.randint(5, 150), random.randint(5, 150), random.randint(5, 150))
        CAV_ARCH_WIZ_VITYAS = tuple((from10(num, NUM_FINGERS, TRANS_D) for num in CAV_ARCH_WIZ_10))
        resp['user_state_update'] = {}
        resp['user_state_update']['num_fingers'] = NUM_FINGERS
        resp['user_state_update']['SS_VITYA'] = {s:num for s, num in zip(('cavalry', 'archery', 'wizard'), CAV_ARCH_WIZ_VITYAS)}
        resp['user_state_update']['SS'] = {s:num for s, num in zip(('cavalry', 'archery', 'wizard'), CAV_ARCH_WIZ_10)}
    elif event['state']['session'].get('story_index'):
        resp['session_state']['story_index'] = event['state']['session']['story_index']
    obj = story[resp['session_state']['story_index']]
    if hasattr(obj, '__call__'):
        resp['response']['text'], resp['response']['tts'], extra = obj(event, resp)
    else:
        resp['response']['text'] = eval(obj['text'], globals={'event': event, 'resp': resp})
        resp['response']['tts'] = eval(obj['tts'], globals={'event': event, 'resp': resp})
        extra = 1
    
    resp['session_state']['story_index'] += extra
    return resp
