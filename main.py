import time

import requests
import json

url_auth = 'https://crm.interra.ru/enter/'
data = {
    'login': 'exselles',
    'password': '254198denis'
}
list_id = []
check_id = []

sess = requests.Session()
p = sess.post(url_auth, data=data)


def collect_data():
    while True:
        url = 'https://crm.interra.ru/data/statement/?author=&calendar%5Bfrom%5D=&calendar%5Bto%5D=&city' \
              '=Первоуральск%2CНовоалексеевское%2CБилимбай&filterName=Все%20заявки&id=Все%20заявки&order=openTimeDESC' \
              '&other=&priority=priorNon&stage=openned&subtype=&type=&worker=&page=1'
        response = sess.get(url)
        data_tasks = response.json()
        for items in data_tasks:
            if items['workers']:
                if items['id'] not in list_id:
                    tasksID = items['id']
                    list_id.append(tasksID)
                    url_id = f'https://crm.interra.ru/#statements/{tasksID}'
                    for i, count_workers in enumerate(items['workers']):
                        print(items['workers'][i]['fio'], url_id)
        time.sleep(1)

def main():
    collect_data()


if __name__ == '__main__':
    main()
