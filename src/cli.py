import argparse
import random

from .core import DEFAULT_THREADS, SCHEDULER_FORK_SCALE, SCHEDULER_INITIAL_CAPACITY
from .i18n import LANGUAGES
from .mhddos import Methods


def init_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'targets',
        nargs='*',
        help='Список целей, разделенных пробелами',
    )
    parser.add_argument(
        '-c',
        '--config',
        help='URL-адрес или локальный путь к файлу с целями атаки',
    )
    parser.add_argument(
        '-t',
        '--threads',
        type=int,
        help=f'Количество потоков (по умолчанию {DEFAULT_THREADS})',
    )
    parser.add_argument(
        '--copies',
        type=int,
        default=1,
        help='Количество копий (по умолчанию 1)',
    )
    parser.add_argument(
        '--debug',
        action='store_true',
        default=False,
        help='Подробный журнал для каждой цели',
    )
    parser.add_argument(
        '--vpn',
        dest='use_my_ip',
        const=10,
        default=0,
        nargs='?',
        type=int,
        action='store',
        help='Использование своего IP, так и прокси для атаки. '
             'При необходимости укажите процент использования моего IP-адреса (по умолчанию 10%)',
    )
    parser.add_argument(
        '--http-methods',
        nargs='+',
        type=str.upper,
        default=['GET', random.choice(['POST', 'STRESS'])],
        choices=Methods.HTTP_METHODS,
        help='Список используемых методов HTTP(L7). Значение по умолчанию — GET + POST|STRESS',
    )
    parser.add_argument(
        '--proxies',
        help='URL-адрес или локальный путь к файлу с используемыми прокси-серверами',
    )
    parser.add_argument(
        '--itarmy',
        action='store_true',
        default=False,
        help='Атаковать цели из списка Cyber Army of Russia'
    )
    parser.add_argument(
        '--lang',
        type=str.lower,
        choices=LANGUAGES,
        help='Выберите язык (по умолчанию ru)'
    )

    # Advanced
    parser.add_argument(
        '--rpc',
        type=int,
        default=1200,
        help='Сколько запросов отправлять через одно прокси-соединение (по умолчанию 1200)',
    )
    parser.add_argument(
        '--scheduler-initial-capacity',
        type=int,
        default=SCHEDULER_INITIAL_CAPACITY,
        help='Сколько задач для каждой цели инициализировать при запуске',
    )
    parser.add_argument(
        '--scheduler-fork-scale',
        type=int,
        default=SCHEDULER_FORK_SCALE,
        help='Сколько задач нужно форкнуть при успешном подключении к цели',
    )

    # Deprecated
    parser.add_argument('--table', action='store_true', default=False)

    return parser
