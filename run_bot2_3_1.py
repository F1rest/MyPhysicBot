import requests
import vk_api
import random

from config import *

from config import TOKEN

vk_bot = vk_api.VkApi(token=TOKEN)
long_poll = vk_bot.method('messages.getLongPollServer', {'need_pts': 1, 'lp_version': 3})
server, key, ts = long_poll['server'], long_poll['key'], long_poll['ts']
print("Готов к работе")


# +str(long_poll)}

def write_msg(user_id, text):
    vk_bot.method('messages.send', {'user_id': user_id, 'message': text})


def write_msg_attach(user_id, text, att_url):
    vk_bot.method('messages.send',
                  {'user_id': user_id,
                   'attachment': att_url,
                   'message': text,
                   'random_id': random.randint(0, 1000)})


while True:
    long_poll = requests.get(
        'https://{server}?act={act}&key={key}&ts={ts}&wait=10000'.format(server=server,
                                                                         act='a_check',
                                                                         key=key,
                                                                         ts=ts)).json()
    update = long_poll['updates']

    if update[0][0] == 4:
        # print(update)
        user_id = update[0][3]
        user_name = vk_bot.method('users.get', {'user_ids': user_id})

        print(str(user_name[0]['first_name']) + ' ' +
              str(user_name[0]['last_name']) + ' написал(a) боту - ' + str(update[0][6]))
        text = update[0][6].lower()

        # if 'привет' in str(text):
        #     write_msg(user_id, 'Привет, ' + (user_name[0]['first_name']))
        #
        # elif 'help' in str(text):
        #     write_msg(user_id,
        #               'Комманды: 1.Привет   2.Красивая картинка   3.Огород, бублик, зима, детская (любую из этих четырех)')

        if 'красив' in str(text):
            write_msg_attach(user_id,
                             'Красивая картинка',
                             'photo-175296561_456239017')
        elif 'огород' in str(text):
            write_msg_attach(user_id,
                             'Лови',
                             'video258838355_456239161')
        elif 'бублик' in str(text):
            write_msg_attach(user_id,
                             'Держи',
                             'video459897331_456239046')
        elif 'зима' in str(text):
            write_msg_attach(user_id,
                             'Хватай',
                             'video258838355_456239156')
        elif 'детская' in str(text):
            write_msg_attach(user_id,
                             'Пока все, но я буду добавлять их)',
                             'video-172678394_456239682')
    ts = long_poll['ts']
