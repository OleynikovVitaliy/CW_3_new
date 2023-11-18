import json
from datetime import datetime
from operator import itemgetter
import operator

file = '../data/operations.json'
executed_state = 'EXECUTED'


def get_payment_type(payment: str):
    if 'счет' in payment.lower():
        return f'{payment[:5]}**{payment[-4:]}'
    else:
        payment_type = f'{payment.split()[len(payment.split()) - 1]}'
        card_type = f'{payment.replace(f" {payment_type}", "")}'
        payment_type = payment_type[:-10] + '** ****' + payment_type[12:]
        payment_type = f'{card_type} {payment_type[:4]} {payment_type[4:]}'
        return payment_type


def parse(operations):
    count = 0
    for i in operations:
        if count == 5:
            return
        if len(i) > 0 and i['state'] == executed_state:

            datetime_str = i['date'].split('T')[0]
            datetime_object = datetime.strptime(datetime_str, '%Y-%m-%d').date().strftime('%d.%m.%Y')
            cost = f'{i["operationAmount"]["amount"]} {i["operationAmount"]["currency"]["name"]}'
            print(f'{datetime_object} {i["description"]}')
            if 'открытие' in i['description'].lower():
                print(f'{get_payment_type(i["to"])}')
            else:
                print(f'{get_payment_type(i["from"])} -> {get_payment_type(i["to"])}')
            print(cost)
            print()
            count += 1


try:
    operations = list()
    with open(file, 'r', encoding="utf-8") as fd:
        operations = json.load(fd)
        fd.close()
    tmp = [date for date in operations if 'date' in date]
    tmp.sort(key=operator.itemgetter('date'), reverse=True)
    parse(tmp)
except Exception as _ex:
    print(f'Error: {_ex}')