import vk_api
import requests
import datetime
import time

session = requests.Session()
login, password = '89216010828', 'QhnE%oY)%1B5'
vk_session = vk_api.VkApi(login, password)

try:
    vk_session.auth(token_only=True)

except vk_api.AuthError as error_msg:
    print(error_msg)
    print()

while True:
    date = str(datetime.datetime(2021, 1, 1, 00, 00, 00, 00000) - datetime.datetime.now())
    result = '-'.join(date.split('.')[:-1])
    vk_session.method("status.set", {"text": '&#127876;' + result + ' &#9731;'})
    time.sleep(60)