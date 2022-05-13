import requests

url_auth = 'https://crm.interra.ru/enter/'
data = {
    'login': 'exselles',
    'password': '254198denis'
}
result_data = []

sess = requests.Session()
p = sess.post(url_auth, data=data)
data_list = []


def collect_data(page=0):
    while True:
        page += 1
        url = f'https://crm.interra.ru/data/statement/?author=&calendar%5Bfrom%5D=&calendar%5Bto%5D=&city' \
              '=Первоуральск%2CНовоалексеевское%2CБилимбай&filterName=Все%20заявки&id=Все%20заявки&order=openTimeDESC' \
              f'&other=&priority=priorNon&stage=openned&subtype=&type=&worker=&page={page}'
        response = sess.get(url)
        data_tasks = response.json()
        if not data_tasks:
            break

        for items in data_tasks:
            if items['workers']:
                if items not in data_list:
                    data_list.append(items)
                    workers_fio = []

                    for workers in items['workers']:
                        workers_fio.append(workers.get('fio'))

                    result_data.append(
                        {
                            'fio_workers': workers_fio,
                            'tasks_url': f"https://crm.interra.ru/#statements/{items.get('id')}",
                            'note': items.get('note'),
                            'tasks_id': items.get('id'),
                            'address': items.get('client').get('address'),
                            'telephone': items.get('client').get('telephone'),
                        }
                        )
        return result_data


def main():
    collect_data()


if __name__ == '__main__':
    main()
