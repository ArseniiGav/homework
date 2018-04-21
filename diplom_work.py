import requests
import time
import json

TOKEN = '7b23e40ad10e08d3b7a8ec0956f2c57910c455e886b480b7d9fb59859870658c4a0b8fdc4dd494db19099'


def get_users_id(input_data):
    params = {
            'access_token': TOKEN,
            'v': '5,74',
            'user_ids': input_data,
    }

    users_info = requests.get('https://api.vk.com/method/users.get', params).json()
    return users_info['response'][0]['id']


def groups_and_friends_search(user_id, extended=0):
    params = {
        'access_token': TOKEN,
        'v': '5,73',
        'user_id': user_id,
        'extended': extended,
        'count': 1000
        }
    params_1 = {
        'access_token': TOKEN,
        'v': '5,73',
        'user_id': user_id,
        }
    groups = requests.get('https://api.vk.com/method/groups.get', params).json()
    friends = requests.get('https://api.vk.com/method/friends.get', params_1).json()
    return groups['response']['items'], friends['response']['items']


def unique_user_groups_search(user_id, set_of_users_groups):
    list_of_users_friends = groups_and_friends_search(user_id)[1]
    common_groups = set()
    i = 0
    for friend_id in list_of_users_friends:
        try:
            print('Подключаюсь к API для поиска групп друга...')
            groups_users_friend = set(groups_and_friends_search(friend_id)[0])
            intersecting_groups = set_of_users_groups & groups_users_friend
            i += 1
            print('Прогресс: {} %'.format(round((i*100)/len(list_of_users_friends), 2)))
        except KeyError:
            print('Ожидаем снятия ограничения ВК...')
            time.sleep(1)
            try:
                print('Подключаюсь к API для поиска групп друга...')
                groups_users_friend = set(groups_and_friends_search(friend_id)[0])
                intersecting_groups = set_of_users_groups & groups_users_friend
                i += 1
                print('Прогресс: {} %'.format(round((i*100)/len(list_of_users_friends), 2)))
            except KeyError:
                print('id {}: Этот друг заблокирован или удален'.format(friend_id))
                i += 1
                print('Прогресс: {} %'.format(round((i*100)/len(list_of_users_friends), 2)))
        common_groups = common_groups | intersecting_groups
    unique_groups = set_of_users_groups - common_groups
    return unique_groups


def get_groups_info(unique_groups):
    unique_groups_list_with_str = []
    for group in list(unique_groups):
        unique_groups_list_with_str.append(str(group))

    params = {
        'access_token': TOKEN,
        'v': '5,73',
        'group_ids': ', '.join(unique_groups_list_with_str),
        'fields': 'members_count'
        }
    time.sleep(1)
    groups_info = requests.get('https://api.vk.com/method/groups.getById', params).json()
    unique_groups_result_list = []
    
    for group in groups_info['response']:
        unique_groups_result_list.append(dict(name=group['name'], gid=group['id'],
                                              members_count=group['members_count']))
    return unique_groups_result_list


def write_in_json_file(unique_groups):
    with open('groups.json', 'w') as f:
        for group in get_groups_info(unique_groups):
            try:
                json.dump(group, f, indent=3, ensure_ascii=False)
            except UnicodeEncodeError:
                print('Название группы {} не декодируется'.format(group['name']))
                json.dump(group, f, indent=3)
            
    print('Готово!')


def main():
    input_data = input('Введите id пользователя или его screen name для поиска его уникальных групп: ', )
    try:
        int(input_data)
        user_id = input_data
    except ValueError:
        user_id = get_users_id(input_data)
    set_of_users_groups = set(groups_and_friends_search(user_id)[0])
    unique_groups = unique_user_groups_search(user_id, set_of_users_groups)
    get_groups_info(unique_groups)
    write_in_json_file(unique_groups)


main()