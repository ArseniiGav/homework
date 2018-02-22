import json
import chardet


def encoding_def(input_name):
    with open(input_name, 'rb') as f:
        data = f.read()
        result = chardet.detect(data)
        return result


def search_for_top_words(input_name):
    with open(input_name, encoding = encoding_def(input_name)['encoding']) as f:
        news = json.load(f)
        list_of_words = []
        dict_of_repetitive_words = {}
        for word in news["rss"]["channel"]["description"].split(' '):
            if len(word) > 6:
                list_of_words.append(word)
        for item in news["rss"]["channel"]["items"]:
            for word in item["description"].split(' '):
                if len(word) > 6:
                    list_of_words.append(word)
            for word in item["title"].split(' '):
                if len(word) > 6:
                    list_of_words.append(word)           
        iteration = 0
        while iteration < len(list_of_words):
            number_of_repeat = 0
            for word in list_of_words:
                if word == list_of_words[iteration]:
                    number_of_repeat += 1
                    dict_of_repetitive_words[word] = number_of_repeat
            iteration += 1        
        dict_of_repetitive_words_sort = sorted(dict_of_repetitive_words.items(),\
        key = lambda item: item[1], reverse = True)
        return dict_of_repetitive_words_sort[:10]

def print_top_words(dict_of_repetitive_words_sort):
    for i in dict_of_repetitive_words_sort:
        print('Слово: "{}", количество повторений: {}'.format(i[0], i[1]))
            
def input_name():
    input_name = input("Введите имя файла: newsafr.json, newsit.json, newsfr.json или newscy.json: ", )
    dict_of_repetitive_words_sort = search_for_top_words(input_name)
    print_top_words(dict_of_repetitive_words_sort)

    
input_name()

          