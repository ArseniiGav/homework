#from urllib.parse import urlencode
import requests

APP_ID = "d802564ec794490faa8d4f25c33be51a"
AUTH_URL = 'https://oauth.yandex.ru/authorize/'

auth_data = {
        'response_type': 'token',
        'client_id': APP_ID,
} 

#print('?'.join((AUTH_URL, urlencode(auth_data))))

token = 'AQAAAAAa9IxEAAToBgmPhdBuCEYvheXojSk8RVQ'

class YaBase:
    
    def __init__(self, token):
        self.token = token
        
    def get_headers(self):
        return {
                'Authorization': 'OAuth {}'.format(self.token) 
        }

class YaMetrikaUser(YaBase):
    
    def get_counters(self):
        headers = self.get_headers()
        response = requests.get('https://api-metrika.yandex.ru/management/v1/counters',\
                               headers=headers)
        return[c['id'] for c in response.json()['counters']]
        
class Counter(YaBase):
    
    def __init__(self, counter_id, token):
        self.counter_id = counter_id
        super().__init__(token)
        
    def get_data(self):
        headers = self.get_headers()
        params = {
                'id': self.counter_id, 
                'metrics': 'ym:s:visits, ym:s:pageviews, ym:s:users'
                
        }       
        response = requests.get('https://api-metrika.yandex.ru/stat/v1/data', params,
                               headers=headers)
    
        try: 
            return response.json()['data'][0]['metrics']
        except IndexError as e:
            return 0
        
first_user = YaMetrikaUser(token)
counters = first_user.get_counters()
print(counters)
for counter_id in counters:
    counter = Counter(counter_id, first_user.token)
    data = counter.get_data()
    print("Количество визитов: {}, количество просмотров: {}, количество посетителей: {}"
          .format(data[0], data[1], data[2]))
