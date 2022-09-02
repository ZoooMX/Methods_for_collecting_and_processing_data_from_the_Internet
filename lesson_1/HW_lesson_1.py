import requests
from pprint import pprint
'''
1. Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для конкретного 
пользователя, сохранить JSON-вывод в файле *.json.
'''

# вариант из документации GitHub https://docs.github.com/en/rest/repos/repos#list-repositories-for-a-user
url = 'https://api.github.com/user/repos'
headers = {'Accept': 'application/vnd.github+json', 'Authorization': 'Bearer  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'}

response = requests.get(url)
if response.ok:
    pass
response = requests.get(url, headers=headers)

j_data_1 = response.json()


# вариант, который нашел на просторах
url = 'https://api.github.com/user/repos'
username = 'ZoooMX'
token = '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'
response = requests.get(url)
if response.ok:
    pass
response = requests.get(url, auth=(username, token))

j_data_2 = response.json()
print(j_data_1 == j_data_2) # проверка на соответствие друг другу двух способов

pprint(j_data_2)

'''
2. Изучить список открытых API (https://www.programmableweb.com/category/all/apis). 
Найти среди них любое, требующее авторизацию (любого типа). Выполнить запросы к нему, пройдя авторизацию. 
Ответ сервера записать в файл.
''' #на сайте велись тех.работы, пошел работать с ВК

# запрос токена с опциями группы - https://oauth.vk.com/authorize?client_id=51416068&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=groups&response_type=token&v=5.131
url_vk = 'https://api.vk.com/method/groups.get?user_id=180193374&' \
         'extended=1&count=5&access_token=vk1.a.vrkex8JcyQJpUNzU_Daa_' \
         'K3wPrUNueB33eQArHSWjKHw0WUjWVbltI1bUxlPwmlpS6-zpsLVmmOcLGKE8vi-' \
         'mhHPtOpByyfIpVaV9WlfYOjqtKg9DcojCoTXJDVdYGBKhiuh5ESjZaTTpUTgkj5fPlW' \
         'NBYihF9S0MP57_spkjRrKMk7XS23ikWoUxT3dMb_W&expires_in=86400&user_id=180' \
         '193374&expires_in=86400&user_id=180193374&v=5.131'
response = requests.get(url_vk)
if response.ok:
    pass
j_data_vk = response.json()
pprint(j_data_vk)

#при запуске на неизвестной VK машине не выдает инфу, результат сохранил в текстовик с именем: Run_from_PyCharm_VK.txt