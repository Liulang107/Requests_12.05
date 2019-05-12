import requests


def translate_it(source_file, result_file, from_lang, to_lang='ru'):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param to_lang:
    :return:
    """

    API_KEY = 'trnsl.1.1.20190505T182807Z.f6dbdddd0edd52a9.f07fa2f49c932fc97866472295fd1cd1b4a565cc'
    URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

    with open(source_file) as f:
        text = f.read()

    params = {
        'key': API_KEY,
        'text': text,
        'lang': '{}-{}'.format(from_lang, to_lang)
    }

    response = requests.get(URL, params=params)
    result = ''.join(response.json()['text'])

    with open(result_file, 'w') as f:
        f.write(result)

    return result


translate_it(source_file='DE.txt', result_file='Translation_from_DE.txt', from_lang='de')
translate_it(source_file='ES.txt', result_file='Translation_from_ES.txt', from_lang='es')
translate_it(source_file='FR.txt', result_file='Translation_from_FR.txt', from_lang='fr')