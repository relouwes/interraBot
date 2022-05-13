import asyncio

from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import hbold, hlink
from main import collect_data
import time

bot = Bot(token='5378731915:AAHL2Osg0z_hEY89fFaeG1psf_NDmBEthOQ', parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

chat_id = "-1001767799407"
list_id = []


@dp.message_handler(commands='start')
async def start(message: types.Message):
    while True:
        data = collect_data()

        for item in data:
            if item not in list_id:
                for fio in item.get('fio_workers'):
                    match fio:
                        case 'Маврин Антон':
                            login = ' @LohPidrNetDruzei'
                        case 'Кривенков Денис':
                            login = ' @relouwes'
                        case 'Хурматуллин Ришат':
                            login = ' @N_109'
                        case _:
                            login = ''

                list_id.append(item)
                card = f"{hlink(item.get('note'), item.get('tasks_url'))}\n" \
                    f"{hbold('ФИО: ')} {', '.join(item.get('fio_workers')) + login}\n" \
                    f"{hbold('Адрес: ')} {item.get('address')}\n" \
                    f"{hbold('Телефон: ')} {'+' + item.get('telephone')}\n" \

                await bot.send_message(chat_id, card)
        await asyncio.sleep(60)


def main():
    executor.start_polling(dp)


if __name__ == '__main__':
    main()
