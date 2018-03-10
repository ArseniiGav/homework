import requests
import chardet
import os

def translate_it(lang_from, path_to_file, path_to_tranlated_file, lang_to='ru'):
    """
    YANDEX translation plugin

    docs: https://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/

    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]

    :param text: <str> text for translation.
    :return: <str> translated text.
    """
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_list = os.listdir(path = current_dir)
    for file in file_list:
        if file.lower() == path_to_file.lower():
            with open(os.path.join(current_dir, file), 'rb') as f:
                data = f.read()
                result = chardet.detect(data)
                data = data.decode(result['encoding'])
                
                params = {
                'key': key,
                'lang': lang_from.lower() + '-' + lang_to,
                'text': data,
                }
                response = requests.get(url, params=params).json()
                translated_data = ' '.join(response.get('text', []))
            with open(path_to_tranlated_file, 'tw', encoding='utf-8') as f:
                f.write(translated_data)
            
def input_data():
    print('Справка: вводите код языка: для русского - ru, \
           для немецкого - de, \
           для французского - fs, \
           для испанского - es')
    lang_from = input('Введите язык, с которого перевести текст: ', )
    path_to_file = input('Введите название файла, текст которого хотите перевести: ', )
    path_to_tranlated_file = input('Введите название файла, в котором хотите сохранить перевод: ')
    translate_it(lang_from, path_to_file, path_to_tranlated_file, lang_to='ru') #, path_to_tranlated_file)
    

input_data()
