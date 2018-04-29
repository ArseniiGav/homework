import requests
import time
import json
import argparse
import sys

TOKEN = '7b23e40ad10e08d3b7a8ec0956f2c57910c455e886b480b7d9fb59859870658c4a0b8fdc4dd494db19099'


def params(user_ids='', user_id='', group_ids='', fields=''):
    params = {
        'access_token': TOKEN,
        'v': '5,73',
        'user_ids': user_ids,
        'user_id': user_id,
        'group_ids': group_ids,
        'fields': fields     
    }
    return params

def get_users_id(input_data):
    URL_users_get = 'https://api.vk.com/method/users.get'
    users_info = requests.get(URL_users_get, params(user_ids=input_data)).json()
    return users_info['response'][0]['id']


def get_request_without_errors(URL, user_id):
    
    def clean(data):
        data = []
        return data
    
    while True:
        data = requests.get(URL, params(user_id=user_id)).json()
        try:
            data['response']['items']
        except KeyError:
            if 'error' in data:
                if data['error']['error_code'] == 6:
                    print('Too many requests per second. Wait to remove the restriction of VK...')
                    time.sleep(1)
                    continue
                elif data['error']['error_code'] == 18:
                    print('id {}: This friend is locked or deleted.'.format(user_id))
                    return clean(data)
                elif data['error']['error_code'] == 15:
                    print('Access is denied {}'.format(user_id))
                    return clean(data)
                elif data['error']['error_code'] == 7:
                    print('You have not enough rights for this action')
                    return clean(data)         
        break
    return data['response']['items']


def groups_and_friends_search(user_id):
    URL_groups_get = 'https://api.vk.com/method/groups.get'
    URL_friends_get = 'https://api.vk.com/method/friends.get'
    groups = get_request_without_errors(URL_groups_get, user_id)
    friends = get_request_without_errors(URL_friends_get, user_id)
    return groups, friends


def unique_user_groups_search(user_id, set_of_users_groups):
    list_of_users_friends = groups_and_friends_search(user_id)[1]
    common_groups = set()
    i = 0
    
    def progress_func(i, list_of_users_friends):
        i += 1
        print('Progress: {} %'.format(round((i*100)/len(list_of_users_friends), 2)))
        return i
    
    
    def search_intersecting_groups(friend_id, set_of_users_groups):
        print("I'm connecting to the API to search for friend's groups...")
        groups_users_friend = set(groups_and_friends_search(friend_id)[0])
        intersecting_groups = set_of_users_groups & groups_users_friend
        return intersecting_groups


    for friend_id in list_of_users_friends:
        intersecting_groups = search_intersecting_groups(friend_id, set_of_users_groups)
        i = progress_func(i, list_of_users_friends)
        common_groups = common_groups | intersecting_groups
    unique_groups = set_of_users_groups - common_groups
    return unique_groups


def get_groups_info(unique_groups):
    unique_groups_list_with_str = []
    for group in list(unique_groups):
        unique_groups_list_with_str.append(str(group))
    time.sleep(1)
    URl_groups_get = 'https://api.vk.com/method/groups.getById'
    groups_info = requests.get(URl_groups_get, params(group_ids=', '.join(unique_groups_list_with_str),
                                                      fields='members_count')).json()
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
                print('Group name {} is not decoded'.format(group['name']))
                json.dump(group, f, indent=3)
            
    print('Done!')

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument ('--user_id', default=228922133, type=int)
    parser.add_argument ('--screen_name', type=str)
    
    return parser

def main():
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
    screen_name = namespace.screen_name
    if screen_name != None:
        user_id = get_users_id(screen_name)
    else:
        user_id = namespace.user_id
    set_of_users_groups = set(groups_and_friends_search(user_id)[0])
    unique_groups = unique_user_groups_search(user_id, set_of_users_groups)
    get_groups_info(unique_groups)
    write_in_json_file(unique_groups)

if __name__ == '__main__':
    main()