#from urllib.parse import urlencode
import requests

APP_ID = 6409525
AUTH_URL = 'https://oauth.vk.com/authorize'

auth_data = {
        'client_id': APP_ID,
        'display': 'page',
        'scope': 'friends,status',
        'response_type': 'token',
        'v': '5.73'
} 

#print('?'.join((AUTH_URL, urlencode(auth_data))))
TOKEN = 'dedf5dd081e0fc5f1420f5eae64a762e4ae7751d3181b6758d773d9f48ec37afc6ba14c4b10091aac8a7e'


def common_friends_search(source_uid, target_uids):
    params = {
        'access_token': TOKEN,
        'v': '5,73',
        'source_uid': source_uid,
        'target_uids': target_uids
    }
    response = requests.get('https://api.vk.com/method/friends.getMutual',
                            params).json()
    iteration = 0
    while iteration < len(target_uids.split(', ')):
        print('Идентификатор пользователя, с которым ищем общих друзей: ',
               response['response'][iteration]['id'])
        for ids_common_friends in response['response'][iteration]['common_friends']:
            print('ID общего друга данных пользователей: {}, ссылка на страницу: {}'
            .format(ids_common_friends, 'https://vk.com/id' + str(ids_common_friends)))
        iteration += 1

def input_data():
    source_uid = input('Введите id главного пользователя: ', )
    target_uids = input('Введите id пользователя(ей), с которыми будем искать\
                         общих друзей (можно вводить нескольких, через запятую): ', )
    common_friends_search(source_uid, target_uids)

input_data()
