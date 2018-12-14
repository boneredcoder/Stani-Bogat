from pathlib import PurePath
from typing import NamedTuple

PREFIX = '?'
MODS = [
    365859941292048384,
    374537025983873024,
    261115722007183362,
    247028507903918083
]

class Path(NamedTuple):
    project = PurePath(__file__).parent.parent
    data = project.joinpath('data/')

    questions = data.joinpath('questions/')
    statistics = data.joinpath('statistics/')
    pending = data.joinpath('pending/')

    global_stats = statistics.joinpath('global/')

    general = questions.joinpath('general/')
    IT = questions.joinpath('IT/')


class File(NamedTuple):
    json = '/questions.json'
    players = 'top_players.json'
    authors = 'top_authors.json'
    pending_questions = 'pending_questions.json'


class Link(NamedTuple):
    github_repo = 'https://github.com/skilldeliver/Stani-Bogat'
    github_icon = 'https://avatars0.githubusercontent.com/u/9919?s=280&v=4'
    leader_board_icon = 'https://i.imgur.com/F7VUqZV.png'


class Sprite(NamedTuple):
    jokers = {'ooo': 'https://i.imgur.com/aTzsSyO.png',
              'oox': 'https://i.imgur.com/4CUYpvv.png',
              'oxo': 'https://i.imgur.com/NYLgn73.png',
              'xoo': 'https://i.imgur.com/8mUsj0G.png',
              'xxo': 'https://i.imgur.com/us4jqub.png',
              'xox': 'https://i.imgur.com/uuUM31U.png',
              'oxx': 'https://i.imgur.com/y1r9XGK.png',
              'xxx': 'https://i.imgur.com/ZPOM3Tc.png'
              }


class Emoji(NamedTuple):
    clock = '\u23f0'
    thumb_down = '👎'
    thumb_up = '👍'


class Color(NamedTuple):
    #TODO write comment what each color is
    info = 0x000000 # white
    rules = 0x3351B6
    top = 0x8a2be2
    how_add = 0xcae00d
    form = 0xcae00d
    wrong = 0xdd2e44
    right = 0x77b255
    commands = 0x3351B6


class Text(NamedTuple):
    invisible = u"\u2063"
    discord_servers = '🏴 Дискорд сървъри:'
    users = f':busts_in_silhouette: Потребители:'
    host = '💻 Хост:'
    used_technologies = '🛠️ Използвани технологии:'
    author = '📝 Автор:'
    me = 'Владислав Михов (skilldeliver)'
    top_contributors = '👷 Топ сътрудници(contributors):'
    conributors = ':one: skilldeliver \n:two: surister'
    top_players = 'ТОП 10 играчи с най-много спечелени пари.'
    top_authors = 'ТОП 10 потребители с най-много добавени въпроси.'
    rules = '📜 Правила:'
    right = 'Верен отговор!'
    wrong = 'Грешен отговор!'
    question_add = '**?** Добавяне на въпрос'
    form = 'Форма'
    added_questions = 'добавени въпроса.'
    money = 'лева.'
    main_commands = '📦 Основни команди.'
    game_commands = '🎮 Игрови команди.'
    statistics = '📊 Статистики - команди.'


class LargeText(NamedTuple):
    list_rules = '1. Един потребител може да бъде само в една игра.\n\
2. Можещ да играеш с бота само в сървър канал.\n\
3. Не може да искаш помощ от бот или приятел в игра.\n\
4. Грешен отговор - играта ти приключва и се запазват парите от достигнатата сигурна сума.'

    instructions = """\
За да добавите въпрос, изпълнете следните инструкции:
**1**. Копирайте и попълнета **формата**(по-долу).
**2**. Изпратете я на **лично**(тук) на бота.
**3**. **Pin**-нете съобщениeто в личният чат(тук).
**4**. Изпълнете командата **$добавям**(тук) или в сървъра.

**При повече въпроси**:
Всеки въпрос трябва да е в отделно съобщение с отделна форма.
// и не забравяйте да го pin-нете

~ ботът ще провери и събере всички pin-нати съобщения в личният Ви чат
~ ще unpin-не всяко от тях и ще реагира съответно с палец нагоре или надолу
~ накрая ще Ви изпрати кратко съобщение с повече информация
"""

    form = """\
```css
Име: [тук поставяте Вашето име или никнейм]
Фото: [линк към Ваша снимка или аватар](опционално)
Тема: [общо, ИТ] - изберете някое от изброените
Ниво: [число от 1 до 15]
Въпрос: [тук поставяте вашият въпрос]
Отговор: [тук поставяте верният отговор]
Друг: [тук поставяте друг неверен отговор]
Друг: [тук поставяте друг неверен отговор]
Друг: [тук поставяте друг неверен отговор]
```
// Не пишете квадратните скоби 😅
"""